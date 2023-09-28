
from rest_framework import serializers
from MyJobApp.models import JobTable
class JobTableSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobTable
        fields='__all__'
