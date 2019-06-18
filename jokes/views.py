# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import generics
from .models import Jokes
from .serializers import JokesSerializer
from django.shortcuts import render

# Create your views here.

class ListJokesView (generics.ListCreateAPIView):
	queryset = Jokes.objects.all()
	serializer_class = JokesSerializer