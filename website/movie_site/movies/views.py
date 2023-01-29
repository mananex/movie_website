# ------ importing dependencies ------ # 

import sys
import postgres_manager as pm

from django.shortcuts import render
from django.http import HttpResponse, Http404

# ------ ---------------------- ------ # 

# ----- ------------------------------------------------- ----- #

# ---- return array with unique items ---- #
def unique_array(array):
	return_array = []
	for value in array:
		if value not in return_array:
			return_array.append(value)
	return return_array
# ---- ------------------------------ ---- #

# main page loading 
def main_page(request):
	pm.cursor.execute('SELECT * FROM movies;')
	template_parameters = {'movies': pm.cursor.fetchall()}
	return render(request, 'movies/main_page.html', template_parameters)


# loading selected movie data
def main_page_movie(request, movie_id):
	try:
		#######################
		pm.cursor.execute(f'SELECT * FROM movies WHERE id = {movie_id};')
		movie_data = pm.cursor.fetchone()
		if movie_data == None:
			raise Http404()
		#######################
		pm.cursor.execute(f'''SELECT movies.id,
									 movies.title,
									 movies.picture,
									 movies.description,
									 movies.runtime,
									 movies.release_date,
									 directors.name, 
									 actors.name, 
									 genres.genre,
									 director_movies.director_id,
									 actor_movies.actor_id,
									 genre_movies.genre_id
							  FROM movies
							  INNER JOIN director_movies ON director_movies.movie_id = movies.id
							  INNER JOIN directors ON directors.id = director_movies.director_id
							  INNER JOIN actor_movies ON actor_movies.movie_id = movies.id
							  INNER JOIN actors ON actors.id = actor_movies.actor_id
							  INNER JOIN genre_movies ON genre_movies.movie_id = movies.id
							  INNER JOIN genres ON genres.id = genre_movies.genre_id
							  WHERE movies.id = {movie_id}''')
		movie_data = pm.cursor.fetchall() 
		#######################

		template_parameters = { 'movie_data': movie_data,
							    'directors_data': unique_array([[i[9], i[6]] for i in movie_data]),
							    'actors_data': unique_array([[i[10], i[7]] for i in movie_data]),
							    'genres_data': unique_array([[i[11], i[8]] for i in movie_data]) }
		return render(request, 'movies/movie.html', template_parameters)
	except:
		raise Http404()


def page_not_found(request, exception):
	return HttpResponseNotFound(f'<p>Page error: {exception}</p>')
