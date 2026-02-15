"""
Action Plan Generator - Creates personalized weekly plans
"""

import random
from datetime import datetime, timedelta

class ActionPlanGenerator:
    def __init__(self):
        self.activities = {
            'anxiety': [
                "Practice 5-minute box breathing",
                "Write down your worries and challenge them",
                "Try progressive muscle relaxation",
                "Go for a mindful walk",
                "Listen to calming music"
            ],
            'stress': [
                "Do 10 minutes of yoga",
                "Take a technology break",
                "Organize your workspace",
                "Talk to a friend",
                "Take a warm bath"
            ],
            'sleep': [
                "Avoid screens 1 hour before bed",
                "Create a bedtime routine",
                "Try a sleep meditation",
                "Read a book (not on phone)",
                "Drink chamomile tea"
            ],
            'focus': [
                "Try Pomodoro technique (25 min work, 5 min break)",
                "Create a to-do list",
                "Remove phone distractions",
                "Work in a quiet space",
                "Take short movement breaks"
            ],
            'mood': [
                "Write 3 things you're grateful for",
                "Do something kind for someone",
                "Listen to uplifting music",
                "Spend time in nature",
                "Call a loved one"
            ]
        }
    
    def generate_plan(self, user_data):
        """Generate personalized weekly action plan"""
        
        # Determine focus areas from user needs
        focus_areas = user_data.get('needs', ['stress'])[:2]
        
        # Map needs to activity categories
        category_map = {
            'Anxiety': 'anxiety',
            'Stress': 'stress',
            'Sleep Issues': 'sleep',
            'Focus Issues': 'focus',
            'Low Mood': 'mood',
            'Loneliness': 'mood',
            'General Wellness': 'mood'
        }
        
        # Get activity categories
        activity_categories = []
        for need in focus_areas:
            cat = category_map.get(need, 'stress')
            if cat not in activity_categories:
                activity_categories.append(cat)
        
        if not activity_categories:
            activity_categories = ['stress', 'mood']
        
        # Generate weekly plan
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekly_plan = []
        
        for i, day in enumerate(days):
            # Rotate through categories
            category = activity_categories[i % len(activity_categories)]
            activity = random.choice(self.activities[category])
            
            weekly_plan.append({
                'day': day,
                'activity': activity,
                'category': category,
                'duration': random.choice([5, 10, 15, 20])
            })
        
        # Generate daily challenge
        daily_challenge = {
            'title': random.choice(["Mindful Moment", "Gratitude Practice", "Kindness Act", "Digital Detox"]),
            'description': random.choice([
                "Take 2 minutes to focus on your breath",
                "Write down one thing you're grateful for",
                "Do something nice for someone without expecting anything back",
                "Spend 30 minutes without your phone"
            ])
        }
        
        return {
            'weekly_plan': weekly_plan,
            'daily_challenge': daily_challenge,
            'focus_areas': focus_areas
        }