# ------ importing dependencies ------ #

import sys
import postgres_manager as pm

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

# ------ ---------------------- ------ #

# ----- ------------------------------------------------- ----- #

# load all actors page
def actors_page(request):
	pm.cursor.execute('SELECT id, name FROM actors')
	template_parameters = {'actors': pm.cursor.fetchall()}
	return render(request, 'actors/actors_page.html', template_parameters)

# load selected actor data
def actor(request, actor_id):
	try:
		#######################
		pm.cursor.execute(f'''SELECT movies.id, movies.title, movies.picture, actors.name
							  FROM actor_movies 
							  INNER JOIN movies ON actor_movies.movie_id = movies.id
							  INNER JOIN actors ON actor_movies.actor_id = actors.id
							  WHERE actor_movies.actor_id = {actor_id};''')
		actor_data = pm.cursor.fetchall()
		#######################

		template_parameters = { 'actor_data': actor_data }
		return render(request, 'actors/actor.html', template_parameters)
	except:
		raise Http404()
