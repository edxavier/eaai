from rest_framework import serializers
from django.contrib.auth.models import User
from sistemas.models import Categoria

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Categoria
		fields = ('url','id','name','description','user',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields = ('url','username','first_name','email',)