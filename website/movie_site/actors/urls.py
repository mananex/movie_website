# ------ importing dependencies ------ # 

from django.urls import path
from .views import actors_page, actor

# ------ ---------------------- ------ # 

# ---- "actors" page links (urlpatterns) ---- #

urlpatterns = [
	path('', actors_page),
	path('<int:actor_id>', actor),
]

# ---- -------------------------------- ---- #