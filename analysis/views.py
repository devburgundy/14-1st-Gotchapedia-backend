import json
import jwt
import requests
import numpy

from django.views import View
from django.http import JsonResponse
from django.conf import settings

from users.models import User
from users.utils import login_decorator
from movie.models import Movie
from .models import Star

class StarratingView(View):
    @login_decorator
    def get(self, request):
        if request.GET.get('id', None) != None:
            movie_id       = request.GET.get('id', None)
            moviequeryset  = Star.objects.filter(movie_id=movie_id)

            rating = {}
            for star in numpy.arange(0.5, 5.5, 0.5):
                rating[star] = moviequeryset.filter(point=star).count()
            return JsonResponse({'movie':rating}, status=200)

        else:
            user_id       = request.user
            userqueryset  = Star.objects.filter(user_id=user_id)

            rating = {}
            for star in numpy.arange(0.5, 5.5, 0.5):
                rating[star] = userqueryset.filter(point=star).count()
            return JsonResponse({'user':rating}, status=200)
