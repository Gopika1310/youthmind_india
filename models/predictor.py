"""
INNOVATIVE FEATURE 2: Wellness Timeline Predictor
Predicts future mood trends based on past data
"""

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
from datetime import datetime, timedelta

class WellnessPredictor:
    def __init__(self):
        self.model = LinearRegression()
        self.poly = PolynomialFeatures(degree=2)
    
    def predict_trend(self, mood_history):
        """
        Predict future mood trends
        mood_history: list of dicts with 'date' and 'mood_score'
        """
        if len(mood_history) < 3:
            return None
        
        # Prepare data
        df = pd.DataFrame(mood_history)
        df['days'] = (pd.to_datetime(df['date']) - pd.to_datetime(df['date'].min())).dt.days
        
        X = df['days'].values.reshape(-1, 1)
        y = df['mood_score'].values
        
        # Polynomial features
        X_poly = self.poly.fit_transform(X)
        
        # Train model
        self.model.fit(X_poly, y)
        
        # Predict next 7 days
        future_days = np.array([df['days'].max() + i for i in range(1, 8)]).reshape(-1, 1)
        future_days_poly = self.poly.transform(future_days)
        predictions = self.model.predict(future_days_poly)
        
        # Calculate trend
        trend = "improving" if predictions[-1] > y[-1] else "declining" if predictions[-1] < y[-1] else "stable"
        
        # Generate insights
        insights = []
        if trend == "improving":
            insights.append("📈 Your wellbeing is trending upward! Keep up the good work!")
        elif trend == "declining":
            insights.append("📉 We noticed a slight dip. Let's try some new strategies this week.")
        
        # Find patterns
        if len(mood_history) > 7:
            # Check weekend vs weekday pattern
            weekend_moods = df[df['date'].dt.dayofweek.isin([5,6])]['mood_score'].mean()
            weekday_moods = df[~df['date'].dt.dayofweek.isin([5,6])]['mood_score'].mean()
            
            if not np.isnan(weekend_moods) and not np.isnan(weekday_moods):
                if weekend_moods > weekday_moods * 1.2:
                    insights.append("🎉 You seem happier on weekends! Maybe plan more fun activities?")
                elif weekday_moods > weekend_moods * 1.2:
                    insights.append("💪 You're more productive on weekdays! Weekend routines could help.")
        
        return {
            'predictions': predictions.tolist(),
            'trend': trend,
            'confidence': self.model.score(X_poly, y),
            'insights': insights
        }