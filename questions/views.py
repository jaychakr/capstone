from django.shortcuts import render

# Create your views here.

from .models import Question, Answer
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    questions = Question.objects.all().order_by('-created_at')
    paginator = Paginator(questions, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "questions/index.html", {
        "questions": page_obj
    })

def question(request):
    if request.method == "POST":
        description = request.POST["question"]
        question = Question(description=description)
        question.save()
        return redirect(reverse("index"))

@csrf_exempt
def answer(request, id):
    if request.method == "POST":
        data = json.loads(request.body)
        description = data.get("answer")
        question = Question.objects.get(id=id)
        answer = Answer(question=question, description=description)
        answer.save()
        return HttpResponse("Successfully added answer to question!");
