from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from itsdangerous import Serializer
from .models import QuizModel
from demoapp.forms import QuizModelForm

#QuizForm    
def hom(request):
    if request.method == "POST":
        questions=QuizModel.objects.all()
        score=0
        correct=0
        wrong=0
        total=0
        for q in questions:
            total+=1
            if q.ans == request.POST.get(q.question):
                score+=1
                correct+=1
            else:
                wrong+=1
        context = {
            'score':f'{score}/{total}',
            'correct':correct,
            'wrong':wrong,
            'total':total
        }
        return render(request,'res.html',context)
    else:
        questions = QuizModel.objects.all()
        context = {'questions':questions}
        return render(request,'hom.html',context)  
    
def addquestion(request):
    form = QuizModelForm()
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('addquestion')
    context={'form':form}
    return render(request,'addqns.html',context)

