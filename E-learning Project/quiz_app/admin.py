from django.contrib import admin
from .models import QuizResult

# This makes the table visible in the admin panel
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('topic', 'score', 'total_questions', 'percentage', 'date_taken')
    list_filter = ('topic', 'date_taken')
