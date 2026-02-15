"""
INNOVATIVE FEATURE 3: Smart Resource Recommender with RAG
Uses vector search for intelligent recommendations
"""

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class WellnessRecommender:
    def __init__(self):
        self.resources = self._load_resources()
        self.vectorizer = TfidfVectorizer(max_features=1000)
        self._build_index()
    
    def _load_resources(self):
        """Load resources from JSON"""
        resources = [
            {
                "id": 1,
                "title": "5-Minute Breathing Exercise",
                "description": "Quick breathing technique for instant calm",
                "tags": "breathing anxiety stress quick relaxation",
                "format": "audio",
                "duration": 5,
                "category": "anxiety"
            },
            {
                "id": 2,
                "title": "Morning Yoga Flow",
                "description": "Gentle 15-minute yoga routine",
                "tags": "yoga physical exercise morning stress",
                "format": "video",
                "duration": 15,
                "category": "stress"
            },
            {
                "id": 3,
                "title": "Sleep Meditation",
                "description": "Guided meditation for better sleep",
                "tags": "sleep meditation relaxation night",
                "format": "audio",
                "duration": 20,
                "category": "sleep"
            },
            {
                "id": 4,
                "title": "Understanding Anxiety",
                "description": "Educational article about anxiety",
                "tags": "anxiety education understanding mental health",
                "format": "text",
                "read_time": 8,
                "category": "anxiety"
            },
            {
                "id": 5,
                "title": "Focus Music Playlist",
                "description": "Instrumental music for concentration",
                "tags": "focus music study concentration productivity",
                "format": "audio",
                "duration": 60,
                "category": "focus"
            },
            {
                "id": 6,
                "title": "Art Therapy Ideas",
                "description": "Simple drawing exercises for emotional expression",
                "tags": "art creative expression therapy drawing",
                "format": "video",
                "duration": 12,
                "category": "creativity"
            },
            {
                "id": 7,
                "title": "Gratitude Journaling",
                "description": "Guide to starting a gratitude practice",
                "tags": "journaling gratitude writing positivity",
                "format": "text",
                "read_time": 5,
                "category": "wellness"
            },
            {
                "id": 8,
                "title": "Nature Sounds",
                "description": "Calming nature sounds for relaxation",
                "tags": "nature relaxation calm meditation sleep",
                "format": "audio",
                "duration": 30,
                "category": "relaxation"
            }
        ]
        return resources
    
    def _build_index(self):
        """Build search index"""
        # Combine tags for each resource
        self.corpus = [r['tags'] for r in self.resources]
        self.tfidf_matrix = self.vectorizer.fit_transform(self.corpus)
    
    def get_recommendations(self, needs, interests, top_n=5):
        """Get personalized recommendations"""
        # Create query from needs and interests
        query = ' '.join(needs + interests)
        
        # Vectorize query
        query_vec = self.vectorizer.transform([query])
        
        # Calculate similarities
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]
        
        # Get top indices
        top_indices = np.argsort(similarities)[-top_n:][::-1]
        
        recommendations = []
        for idx in top_indices:
            if similarities[idx] > 0.1:
                rec = self.resources[idx].copy()
                rec['relevance_score'] = float(similarities[idx])
                recommendations.append(rec)
        
        return recommendations
    
    def get_similar_resources(self, resource_id, n=3):
        """Find similar resources"""
        if resource_id > len(self.resources):
            return []
        
        idx = resource_id - 1
        resource_vec = self.tfidf_matrix[idx]
        similarities = cosine_similarity(resource_vec, self.tfidf_matrix)[0]
        
        similar_indices = np.argsort(similarities)[-n-1:-1][::-1]
        
        similar = []
        for sim_idx in similar_indices:
            if sim_idx != idx:
                similar.append(self.resources[sim_idx])
        
        return similar