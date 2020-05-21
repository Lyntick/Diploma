from rest_framework import serializers
from .models import Statistic


class StatisticListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistic
        fields = '__all__'
