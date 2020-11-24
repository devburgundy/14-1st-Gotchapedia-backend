from django.urls import path
from .views      import MovieInfoView, MovieUserView

urlpatterns= [
    path('/movies/user', MoviesUserView.as_view()),
    path('<int:movie_id>', MovieInfoView.as_view())
]
