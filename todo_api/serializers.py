from rest_framework import serializers
from .models import Todo

# Create the serializer


class TodoSerializer(serializers.ModelSerializer):

    completed = serializers.BooleanField(source='isCompleted')

    class Meta:
        model = Todo
        fields = ['id', 'title', 'description',
                  'date_created', 'updated_at', 'completed']
