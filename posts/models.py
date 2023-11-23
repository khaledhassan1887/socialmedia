from django.db import models
from django.contrib.auth.models import User
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# models.py

from django.db import models
from django.utils.translation import gettext_lazy as _

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name=_("Content"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))


    def get_similar_posts(self):
        # Get all posts excluding the current post
        all_posts = Post.objects.exclude(id=self.id)
        # Extract content from posts
        post_contents = [post.content for post in all_posts]
        # Add current post content to the list
        post_contents.append(self.content)
        # Convert content into TF-IDF vectors
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(post_contents)
        # Calculate cosine similarities
        cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        # Get indices of similar posts
        similar_posts_indices = cosine_similarities.argsort()[0][::-1]
        # Get 5 most similar posts
        similar_posts = [all_posts[index] for index in similar_posts_indices[:5]]
        return similar_posts

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
