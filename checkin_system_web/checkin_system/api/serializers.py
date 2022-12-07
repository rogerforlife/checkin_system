from checkin_system.models import Checkindata, Hrdata
from rest_framework import serializers


class HrdataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hrdata
        fields = '__all__'


class CheckindataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Checkindata
        fields = '__all__'
