# ----- importing dependencies ----- #

from django.urls import path
from .views import main_page, main_page_movie

# ----- ---------------------- ----- #

# ---- "actors" page links (urlpatterns) ---- #

urlpatterns = [
	path('', main_page),
	path('<int:movie_id>', main_page_movie)
]

# ---- -------------------------------- ---- #