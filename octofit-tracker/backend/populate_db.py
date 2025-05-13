import pymongo
from datetime import date

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["octofit_db"]


# Clear collections before inserting test data
db.users.delete_many({})
db.teams.delete_many({})
db.activity.delete_many({})
db.leaderboard.delete_many({})
db.workouts.delete_many({})

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

print("Test data inserted into octofit_db.")
