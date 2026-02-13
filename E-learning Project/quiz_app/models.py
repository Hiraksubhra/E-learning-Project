from django.db import models

class AIQuiz(models.Model):
    title = models.CharField(max_length=255)
    topic = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    # Stores the generated quiz as a flexible JSON object
    quiz_data = models.JSONField() 

    def __str__(self):
        return self.title

class QuizResult(models.Model):
    topic = models.CharField(max_length=200)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    percentage = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This forces the MongoDB collection name to be "Quizzes"
        db_table = 'Quizzes'

    def __str__(self):
        return f"{self.topic}: {self.score}/{self.total_questions}"


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)  # URL-friendly name (e.g., 'web-design-101')
    instructor = models.CharField(max_length=100)
    thumbnail = models.URLField(blank=True)
    description = models.TextField(blank=True)

    # It will store the entire nested list of modules and video links.
    modules = models.JSONField(default=list) 

    def __str__(self):
        return self.title
