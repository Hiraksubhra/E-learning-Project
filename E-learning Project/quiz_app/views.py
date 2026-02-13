from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .models import AIQuiz
from .ai_service import generate_quiz_json
from django.shortcuts import render, get_object_or_404, redirect
import json
from .models import Course


@method_decorator(csrf_exempt, name='dispatch')
class GenerateQuizView(APIView):
    def post(self, request):
        topic = request.data.get('topic')
        if not topic:
            return Response({"error": "Topic is required"}, status=400)

        data = generate_quiz_json(topic)
        if not data:
             return Response({"error": "AI failed"}, status=500)

        quiz = AIQuiz.objects.create(title=data['title'], topic=topic, quiz_data=data)
        
        return Response({
            "quiz_id": quiz.id,
            "title": quiz.title,
            "questions": data['questions']
        }, status=201)

from django.http import JsonResponse
from .models import QuizResult

@csrf_exempt
def save_quiz_result(request):
    """Saves the quiz result to MongoDB"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            result = QuizResult.objects.create(
                topic=data.get('topic'),
                score=data.get('score'),
                total_questions=data.get('total_questions'),
                percentage=data.get('percentage')
            )
            return JsonResponse({'message': 'Result saved successfully!'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def get_quiz_history(request):
    """Fetches all past quiz results"""
    results = QuizResult.objects.all().order_by('-date_taken').values()
    return JsonResponse(list(results), safe=False)

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
@login_required(login_url='login_page')
def course_player(request, course_slug):
    # Fetch from DB
    course = get_object_or_404(Course, slug=course_slug)

    # Prepare JSON Data
    # We create a dictionary because the Django Model Object itself isn't JSON serializable
    course_data = {
        "title": course.title,
        "instructor": course.instructor,
        "description": course.description,
        "modules": course.modules, # This is already a list (JSONField)
    }

    # Render
    return render(request, 'player.html', {
        'course': course,  # For the <title> tag
        'course_data': json.dumps(course_data) # For the JavaScript
    })

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# quiz_app/views.py

def login_page(request):
    """Renders the login HTML page"""
    if request.user.is_authenticated:
        return redirect('dashboard') # Redirect if already logged in
    return render(request, 'login.html')

def login_req(request):
    """Processes the login data"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login_page') # Reload the login page to show error

    return redirect('login_page')

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('index')

def index(request):
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def courses_list(request):
    # Fetch all courses from MongoDB/Database
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})

def analytics(request):
    return render(request, 'analytics.html')

def settings(request):
    return render(request, 'settings.html')

def about(request):
    """Renders the About Us page"""
    return render(request, 'about.html')

def contact(request):
    """Renders the Contact Us page"""
    return render(request, 'contact.html')

def courses_home(request):
    """Renders the Course page"""
    return render(request, 'courses_home.html')