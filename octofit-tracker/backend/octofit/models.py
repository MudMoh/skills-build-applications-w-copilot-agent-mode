from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    team_id = models.CharField(max_length=100, null=True, blank=True)

class Team(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)

class Activity(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    points = models.IntegerField()

class Leaderboard(models.Model):
    _id = models.ObjectIdField()
    user_id = models.CharField(max_length=100)
    points = models.IntegerField()
    rank = models.IntegerField()

class Workout(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_by = models.CharField(max_length=100)
