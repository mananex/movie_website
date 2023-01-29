# ----- importing dependencies ----- #

from django.urls import path
from .views import *

# ----- ---------------------- ----- #

# ---- "actors" page links (urlpatterns) ---- #

urlpatterns = [
	path('', directors_page),
	path('<int:director_id>', director)
]

# ---- -------------------------------- ---- #