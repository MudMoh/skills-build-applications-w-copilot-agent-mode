# Test data for octofit_db based on monafit tracker example
# This file can be imported in scripts or used for reference

test_data = {
    "users": [
        {"email": "alice@example.com", "name": "Alice", "password": "alicepass", "team_id": None},
        {"email": "bob@example.com", "name": "Bob", "password": "bobpass", "team_id": None},
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["alice@example.com"]},
        {"name": "Team Beta", "members": ["bob@example.com"]},
    ],
    "activity": [
        {"user_id": "alice@example.com", "activity_type": "run", "duration": 30, "date": "2025-05-13", "points": 10},
        {"user_id": "bob@example.com", "activity_type": "walk", "duration": 60, "date": "2025-05-13", "points": 8},
    ],
    "leaderboard": [
        {"user_id": "alice@example.com", "points": 10, "rank": 1},
        {"user_id": "bob@example.com", "points": 8, "rank": 2},
    ],
    "workouts": [
        {"name": "Pushups", "description": "Do 20 pushups", "suggested_by": "Coach"},
        {"name": "Situps", "description": "Do 30 situps", "suggested_by": "Coach"},
    ]
}
