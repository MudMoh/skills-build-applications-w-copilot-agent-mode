from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    team_id = serializers.CharField(allow_null=True, required=False)

class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(), required=False)

class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    activity_type = serializers.CharField(max_length=50)
    duration = serializers.IntegerField()
    date = serializers.DateField()
    points = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user_id = serializers.CharField()
    points = serializers.IntegerField()
    rank = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    suggested_by = serializers.CharField()
