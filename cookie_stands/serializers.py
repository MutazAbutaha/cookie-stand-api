from rest_framework import serializers
from .models import cookie_stands


class cookie_standserializer(serializers.ModelSerializer):
    class Meta:
        model = cookie_stands
        fields = "__all__"
