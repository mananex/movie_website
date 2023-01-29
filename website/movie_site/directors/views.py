# ------ importing dependencies ------ #

import sys
import postgres_manager as pm

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# ------ ---------------------- ------ #

# ----- ------------------------------------------------- ----- #

# load all directors page
def directors_page(request):
	pm.cursor.execute('SELECT id, name FROM directors')
	template_parameters = { 'directors': pm.cursor.fetchall()}
	return render(request, 'directors/directors_page.html', template_parameters)

# load selected director data
def director(request, director_id):
	try:
		#######################
		pm.cursor.execute(f'''SELECT movies.id, movies.title, movies.picture, directors.name
							  FROM director_movies 
							  INNER JOIN movies ON director_movies.movie_id = movies.id 
							  INNER JOIN directors ON director_movies.director_id = directors.id
							  WHERE director_movies.director_id = {director_id}''')
		director_data = pm.cursor.fetchall()
		#######################
		
		template_parameters = { 'director_data': director_data }
		return render(request, 'directors/director.html',template_parameters)
	except:
		raise Http404()

