"""
INNOVATIVE FEATURE 1: AI Mood Predictor
Uses NLP to analyze text and predict emotional state
"""

import numpy as np
from transformers import pipeline
import streamlit as st

class MoodPredictor:
    def __init__(self):
        # Load lightweight model (cached)
        self.classifier = None
    
    @st.cache_resource
    def _load_model():
        return pipeline(
            "text-classification",
            model="bhadresh-savani/bert-base-uncased-emotion",
            return_all_scores=True
        )
    
    def predict_mood(self, text):
        """Predict mood from text input"""
        if not text:
            return None
        
        model = self._load_model()
        results = model(text)[0]
        
        # Sort by score
        results.sort(key=lambda x: x['score'], reverse=True)
        
        return {
            'primary_emotion': results[0]['label'],
            'confidence': results[0]['score'],
            'all_emotions': {r['label']: r['score'] for r in results}
        }
    
    def get_mood_color(self, emotion):
        """Get color for visualization"""
        colors = {
            'joy': '#FFD700',
            'sadness': '#4169E1',
            'anger': '#DC143C',
            'fear': '#800080',
            'love': '#FF69B4',
            'surprise': '#FFA500'
        }
        return colors.get(emotion, '#808080')