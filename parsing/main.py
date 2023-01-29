# ----- importing dependencies ----- #

import psycopg2
import sql_commands
import requests
import bs4
import random
import time
import sys

###########################

from datetime import datetime
from random_user_agent.user_agent import UserAgent

# ----- ---------------------- ----- #

# ----- adding to sys.path postgres_manager module folder ----- #

sys.path.append('../')

# ----- importing postgres_manager ----- #

import postgres_manager as pm

# ----- ------------------------------------------------- ----- #

# -------- main class -------- #

class MainParser:




	# instance initialization
	def __init__(self):
		self.cursor = pm.cursor
		self.user_agents = UserAgent(software_names = ['chrome'], operating_systems = ['windows', 'linux'], limit = 1000).get_user_agents()




	# creating important tables
	def create_basic_tables(self):
		self.cursor.execute(sql_commands.create_basic_tables)




	# parse top 250 movies links
	def parse_links(self):
		parse_content = bs4.BeautifulSoup(requests.get('https://m.imdb.com/chart/top').content, 'html.parser')
		for element in parse_content.find_all('div', {'class': ['col-xs-12', 'col-md-6']}):
			try:
				movie_link = 'https://m.imdb.com' + element.select('.col-xs-12 > .media > .btn-full')[0]['href']
				self.cursor.execute(f"SELECT link FROM film_links WHERE link = '{movie_link}'")
				if self.cursor.fetchone() == None:
					self.cursor.execute(f"INSERT INTO film_links (link, status) VALUES ('{movie_link}', False)")
			except Exception as e:
				pass



	##############################################################			




	# parsing important movie data
	def parse_movie_data(self, parse_content):
		movie_title = parse_content.find('h1', {'class': ['sc-b73cd867-0', 'fbOhB']}).text.replace("'", "''")
		movie_picture = parse_content.find('img', {'class': 'ipc-image'})['src']
		movie_description = parse_content.find('span', {'class': ['sc-16ede01-2', 'gXUyNh']}).text.replace("'", "''")
		movie_runtime = parse_content.find('div', {'class': ['sc-80d4314-2', 'iJtmbR']}).select('ul > .ipc-inline-list__item')[-1].text
		movie_date = parse_content.find('div', {'class': ['sc-80d4314-2', 'iJtmbR']}).select('ul > .ipc-inline-list__item')[0].text[0:4]
		create_at = datetime.now()

		# insert data to the table
		self.cursor.execute(sql_commands.insert_movie_data % (movie_title, movie_picture, movie_description, movie_runtime, movie_date, create_at))
		return self.cursor.fetchone()



	# parsing movie directors
	def parse_directors(self, parse_content, movie_id):
		movie_directors = parse_content.find_all('ul', {'class': ['ipc-inline-list', 'ipc-inline-list--show-dividers', 'ipc-inline-list--inline', 'ipc-metadata-list-item__list-content', 'baseAlt']})[2].select('li')
		for director in movie_directors:
			try:
				filtered_director = director.text.replace("'", "''")
				director_row = ()
				self.cursor.execute(f"SELECT name FROM directors WHERE name = '{filtered_director}'")

				if director.text == '' or director.text == 'Writers':
					continue
				elif self.cursor.fetchone() == None:
					self.cursor.execute(sql_commands.insert_director_data % (filtered_director))
				else:
					self.cursor.execute(f"SELECT * FROM directors WHERE name = '{filtered_director}'")

				director_row = self.cursor.fetchone()
				self.cursor.execute(f"SELECT * FROM movies WHERE id = '{movie_id}'")
				movie_row = self.cursor.fetchone()
				self.cursor.execute(sql_commands.insert_director_movies_data % (director_row[0], movie_row[0]))
			except:
				pass
	



	# parsing movie stars (actors)
	def parse_stars(self, parse_content, movie_id):
		movie_actors = parse_content.find_all('ul', {'class': ['ipc-inline-list', 'ipc-inline-list--show-dividers', 'ipc-inline-list--inline', 'ipc-metadata-list-item__list-content', 'baseAlt']})[4].select('li')
		for actor in movie_actors:
			filtered_actor = actor.text.replace("'", "''")
			actor_row = ()

			self.cursor.execute(f"SELECT name FROM actors WHERE name = '{filtered_actor}'")
			if self.cursor.fetchone() == None:
				self.cursor.execute(sql_commands.insert_actor_data % (filtered_actor))
			else:
				self.cursor.execute(f"SELECT * FROM actors WHERE name = '{filtered_actor}'")

			actor_row = self.cursor.fetchone()
			self.cursor.execute(f"SELECT * FROM movies WHERE id = '{movie_id}'")
			movie_row = self.cursor.fetchone()
			self.cursor.execute(sql_commands.insert_actor_movies_data % (actor_row[0], movie_row[0]))




	# parsing movie genres
	def parse_genres(self, parse_content, movie_id):
		movie_genres = parse_content.find_all('a', {'class': ['sc-16ede01-3', 'bYNgQ', 'ipc-chip', 'ipc-chip--on-baseAlt']})
		for genre in movie_genres:
			genre_row = ()

			self.cursor.execute(f"SELECT genre FROM genres WHERE genre = '{genre.text}'")
			if self.cursor.fetchone() == None:
				self.cursor.execute(sql_commands.insert_genre_data % (genre.text))
			else:
				self.cursor.execute(f"SELECT * FROM genres WHERE genre = '{genre.text}'")

			genre_row = self.cursor.fetchone()
			self.cursor.execute(f"SELECT * FROM movies WHERE id = '{movie_id}'")
			movie_row = self.cursor.fetchone()
			self.cursor.execute(sql_commands.insert_genre_movies_data % (genre_row[0], movie_row[0]))




	# parsing iteration
	def parsing_iteration(self, link):
		parse_content = bs4.BeautifulSoup(requests.get(link, headers = {'User-Agent': random.choice(self.user_agents)['user_agent']}).content, 'html.parser')		
		movie_id = self.parse_movie_data(parse_content)[0]
		self.parse_directors(parse_content, movie_id)
		self.parse_stars(parse_content, movie_id)
		self.parse_genres(parse_content, movie_id)




	# starting all parsing processes
	def start_parsing_process(self):
		self.cursor.execute('SELECT * FROM film_links')
		for link in self.cursor.fetchall():
			if link[2] == False:
				try:
					self.parsing_iteration(link[1])
				except:
					print('error ocurred, repeating...')
					self.parsing_iteration(link[1])
				self.cursor.execute(f"UPDATE film_links SET status = true WHERE link = '{link[1]}'")
			else:
				print('already parsed')
				

# -------- ---------- -------- #





# ----- script executing ----- #

if __name__ == '__main__':

	parser = MainParser()
	parser.create_basic_tables()
	parser.parse_links()
	parser.start_parsing_process()

# ----- ---------------- ----- #