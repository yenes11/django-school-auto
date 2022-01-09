from django.shortcuts import render, redirect
from .models import Quiz
from django.views.generic import ListView
from django.http import JsonResponse
from sorular.models import Question
from sonuc.models import Result
from sorular.models import Answer

def QuizListView(request):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        current_user = request.user.pk
        user_sinif = request.user.ogrenciler.sinifi.pk

        context = {
            'obj1' :  Quiz.objects.raw(f'SELECT id FROM sinav_quiz WHERE sinif_id={user_sinif} EXCEPT SELECT quiz_id FROM sonuc_result WHERE user_id={current_user}'),
        }
        return render(request, 'sinav/main.html', context)


def quiz_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        quiz = Quiz.objects.get(pk=pk)
        return render(request, 'sinav/sinav.html', {'obj': quiz})

def quiz_data_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        quiz = Quiz.objects.get(pk=pk)
        questions = []
        for q in quiz.get_question():
            answers = []
            for a in q.get_answers():
                answers.append(a.text)
            questions.append({str(q): answers})
        return JsonResponse(
            {
                'data': questions,
                'time': quiz.time,
            }
        )

def save_quiz_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('base') 
    else:
        print(request.POST)
        if request.is_ajax():
            questions = []
            data = request.POST
            data_ = dict(data.lists())
            data_.pop('csrfmiddlewaretoken')

            for k in data_.keys():
                print('key:', k)
                question = Question.objects.get(text=k)
                questions.append(question)
            print(questions)

            user = request.user
            quiz = Quiz.objects.get(pk=pk)

            score = 0
            multiplier = 100 / quiz.soru_sayisi
            results = []
            correct_answer = None

            for q in questions:
                a_selected = request.POST.get(q.text)
                
                if a_selected != "":
                    question_answers = Answer.objects.filter(question=q)
                    for a in question_answers:
                        if a_selected == a.text:
                            if a.correct:
                                score += 1
                                correct_answer = a.text
                        else:
                            if a.correct:
                                correct_answer = a.text
                    results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
                else:
                    results.append({str(q): 'not answered'})
            score_ = score * multiplier
            Result.objects.create(quiz=quiz, user=user, score=score_)

        return JsonResponse({'text': 'works'})