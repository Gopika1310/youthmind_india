"""
Helper functions for YouthMind India
"""

import json
import os
from datetime import datetime

def save_user_data(user_id, data):
    """Save user data to JSON file"""
    os.makedirs('data/users', exist_ok=True)
    with open(f'data/users/{user_id}.json', 'w') as f:
        json.dump(data, f, indent=2)

def load_user_data(user_id):
    """Load user data from JSON file"""
    try:
        with open(f'data/users/{user_id}.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def format_date(date_str):
    """Format date string"""
    date = datetime.fromisoformat(date_str)
    return date.strftime("%B %d, %Y")

def get_mood_emoji(score):
    """Convert numeric score to emoji"""
    if score >= 8:
        return "😊"
    elif score >= 6:
        return "🙂"
    elif score >= 4:
        return "😐"
    elif score >= 2:
        return "🙁"
    else:
        return "😞"