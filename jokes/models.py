# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Jokes (models.Model):
	joke_id = models.AutoField(primary_key = True)
	joke_content = models.TextField(max_length = 2000)

	def __str__(self):
		return "{}".format(self.joke_id)

