from rest_framework import serializers
from .models import Survey


class TodoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Survey
            fields = ('id','project','name','location','accomodation','guests','rating','checkin','checkout')