from rest_framework import serializers
from jokes.models import Jokes


class JokesSerializer (serializers.ModelSerializer):
	class Meta : 
		model = Jokes
		fields = '__all__'
		extra_kwargs = {
		'url': {
			'view_name': 'jokes:joke-detail',
			}
		}