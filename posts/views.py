# posts/views.py
from rest_framework import viewsets
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer
from .sentiment_analysis import create_sentiment_analysis_model

sentiment_model = create_sentiment_analysis_model()

def analyze_sentiment(text):
    # Preprocess text if necessary
    # ...
    sentiment_score = sentiment_model.predict(text)  # Use your sentiment analysis model here
    return sentiment_score
# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer