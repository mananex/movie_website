# ----- importing dependencies ----- #

from django.urls import path
from .views import genres_page, genre
# ----- ---------------------- ----- #

# ---- "actors" page links (urlpatterns) ---- #

urlpatterns = [
	path('', genres_page),
	path('<int:genre_id>', genre)
]

# ---- -------------------------------- ---- #