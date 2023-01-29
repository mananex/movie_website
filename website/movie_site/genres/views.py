# ------ importing dependencies ------ # 

import sys
import postgres_manager as pm

from django.shortcuts import render
from django.http import HttpResponse, Http404

# ------ ---------------------- ------ # 

# ----- ------------------------------------------------- ----- #

# load all genres page
def genres_page(request):
	pm.cursor.execute('SELECT id, genre FROM genres;')
	template_parameters = {'genres': pm.cursor.fetchall()}
	return render(request, 'genres/genres_page.html', template_parameters)

# load selected genre movies
def genre(request, genre_id):
	try:
		#######################
		pm.cursor.execute(f'''SELECT movies.title, movies.picture, movies.id, genres.genre
						   	  FROM genre_movies 
						   	  INNER JOIN movies ON genre_movies.movie_id = movies.id
						   	  INNER JOIN genres ON genre_movies.genre_id = genres.id
						   	  WHERE genre_movies.genre_id = {genre_id};''')
		genre_data = pm.cursor.fetchall()
		#######################

		template_parameters = { 'genre_data': genre_data }
		return render(request, 'genres/genre.html', template_parameters)
	except:
		raise Http404()