from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import random

def home(request):
    return render(request, "index_templates/home.html")
def quiz(request):
    questions = Question.objects.all()
    return render(request, "index_templates/index.html", {'questions': questions})


def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle(question_objs)
        for question_obj in question_objs:
            data.append({
                "uid": question_obj.uid,
                "question": question_obj.question,
                "marks": question_obj.marks,
                "answers": question_obj.get_answers()

            })

        payload = {'status': True, 'data': data}

        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Something wet wrong")