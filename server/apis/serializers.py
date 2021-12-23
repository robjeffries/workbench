from rest_framework import serializers
from .models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('host','log','user','time','request_method','request','proto','status','bytes')