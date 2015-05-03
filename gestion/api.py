from rest_framework import serializers

from .models import *


class MemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Memory