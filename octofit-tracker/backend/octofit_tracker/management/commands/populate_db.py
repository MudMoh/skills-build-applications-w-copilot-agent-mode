import pymongo
from datetime import date
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the octofit_db MongoDB database with test data.'

    def handle(self, *args, **options):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client["octofit_db"]

        # Insert test users
        db.users.insert_many([
            {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": None},
            {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": None},
        ])

        # Insert test teams
        db.teams.insert_many([
            {"name": "Team Alpha", "members": ["alice@example.com"]},
            {"name": "Team Beta", "members": ["bob@example.com"]},
        ])

        # Insert test activities
        db.activity.insert_many([
            {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "date": str(date.today()), "points": 10},
            {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "date": str(date.today()), "points": 8},
        ])

        # Insert test leaderboard
        db.leaderboard.insert_many([
            {"user_id": "alice@example.com", "points": 10, "rank": 1},
            {"user_id": "bob@example.com", "points": 8, "rank": 2},
        ])

        # Insert test workouts
        db.workouts.insert_many([
            {"name": "Pushups", "description": "Do 20 pushups", "suggested_by": "Coach"},
            {"name": "Situps", "description": "Do 30 situps", "suggested_by": "Coach"},
        ])

        self.stdout.write(self.style.SUCCESS('Test data inserted into octofit_db.'))
