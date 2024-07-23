from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question
from .email import send_email


def index(request):
    if request.method == 'POST':
        # Get form data
        answer1 = request.POST.get('q1')
        print(answer1)
        answer2 = request.POST.get('q2')
        print(answer2)
        answer3 = request.POST.get('q3')
        print(answer3)
        answer4 = request.POST.get('q4')
        print(answer4)
        answer5 = request.POST.get('q5')
        print(answer5)
        content = f"Answer 1: {answer1}\nAnswer 2: {answer2}\nAnswer 3: {answer3}\nAnswer 4: {answer4}\nAnswer 5: {answer5}"
        # Send email
        send_email(content)
        return render(request, 'survey/index.html')
        #return HttpResponse('Email sent successfully!')  # or render another template
    return render(request, 'survey/index.html')