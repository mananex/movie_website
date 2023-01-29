# ----- Importing dependencies ----- #

import sqlite3
import bs4
import configs
import requests

# ----- ---------------------- ----- #



# ------ Sqlite database initialization ------ #

sqlite = sqlite3.connect(configs.SQLITE_DATABASE)
cursor = sqlite.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS movies(movie_name TEXT,
													movie_date INT,
													movie_rating REAL,
													movie_director TEXT,
													movie_description TEXT)''')
sqlite.commit()

# ------ ------------------------------- ------ #



# ------- Beautiful soup initialization ------- #

parse_page = requests.get(configs.PAGE_FOR_PARSE).content
parse_content = bs4.BeautifulSoup(parse_page, 'html.parser')

# ------- ----------------------------- ------- #



# --------------- Start parsing --------------- #

for element in parse_content.find_all('div', {'class': ['col-xs-12', 'col-md-6']}):
	try:
		movie_link = element.select('.col-xs-12 > .media > .btn-full')[0]['href']
		parse_movie_page = requests.get('https://m.imdb.com' + movie_link).content
		parse_movie_content = bs4.BeautifulSoup(parse_movie_page, 'html.parser')

		movie_name = element.select('.col-xs-12 > .media > .btn-full > span > h4')[0].find_all(text = True, recursive = False)[1].translate(dict.fromkeys(range(32)))
		movie_date = int(element.select('.col-xs-12 > .media > .btn-full > span > h4 > .unbold')[1].text.translate(dict.fromkeys(range(40, 42))))
		movie_rating = float(element.select('.col-xs-12 > .media > .btn-full > span > p > .imdb-rating')[0].text)
		movie_director = parse_movie_content.find_all('a', {'class': 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link'})[0].text
		movie_description = parse_movie_content.find_all('span', {'class': 'sc-16ede01-2'})[0].text

		cursor.execute(f'SELECT movie_name FROM movies WHERE movie_name == "{movie_name}"')
		if cursor.fetchone() == None:
			cursor.execute('INSERT INTO movies VALUES (?, ?, ?, ?, ?)', (f'{movie_name}', movie_date, movie_rating, f'{movie_director}', f'{movie_description}'))
			sqlite.commit()

	except Exception as e:
		print(e)

# --------------- ------------- --------------- #
