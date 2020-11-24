from django.urls import path, include

urlpatterns = [
    path('user', include('users.urls')),
    path('movie', include('movie.urls')),
    path('analysis', include('analysis.urls')),
    path('comment', include('comment.urls'))
]
