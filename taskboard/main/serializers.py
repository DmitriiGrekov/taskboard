from rest_framework import serializers
from .models import TaskModel


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = TaskModel
        fields = ('user',
                  'title',
                  'content',
                  'date_saved',
                  'date_create',
                  'date_ending',)
