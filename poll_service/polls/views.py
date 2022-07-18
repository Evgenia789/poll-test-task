from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from polls.models import (Answer,  # isort:skip
                          Question, UserPoint, UserQuestion)

User = get_user_model()


def index(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, settings.PAGE_COUNT)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'polls/index.html', context)


@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/question_detail.html', context)


def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question,
        'question_id': question.id
    }
    try:
        if UserQuestion.objects.filter(
            user=request.user,
            question=question
        ).exists():
            raise Exception('Вы уже отвечали на этот вопрос')
        selected_answer = question.answer_set.get(pk=request.POST['answer'])
    except (KeyError, Answer.DoesNotExist):
        context['error_message'] = "Вы не выбрали ответ"
        return render(request, 'polls/question_detail.html', context)
    except (Exception):
        context['error_message'] = "Вы уже отвечали на этот вопрос"
        return render(request, 'polls/question_detail.html', context)
    else:
        selected_answer.vote += 1
        selected_answer.save()
        UserQuestion.objects.get_or_create(
                user=request.user,
                question=question
            )
        if UserPoint.objects.filter(user=request.user).exists():
            user = UserPoint.objects.get(user=request.user)
            user.vote += 1
            user.count_answer += 1
            user.save()
        else:
            UserPoint.objects.get_or_create(
                user=request.user,
                vote=1,
                count_answer=1
            )
        return redirect(reverse('polls:results', args=(question.id,)))


@login_required
def all_users(request):
    users = UserPoint.objects.all()
    context = {
        'users': users
    }
    return render(request, 'polls/users.html', context)


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    colors = UserPoint._meta.get_field('color').choices
    context = {
        'user': user,
        'colors': colors
    }
    try:
        user_obj = UserPoint.objects.get(user=request.user)
    except (UserPoint.DoesNotExist):
        context['vote'] = 0
        context['color'] = 'white'
        context['error_message'] = "Недостаточно средств, необходимо 3"
        return render(request, 'polls/profile.html', context)
    else:
        context['vote'] = user_obj.vote
        context['color'] = user_obj.color
    if request.method == 'POST':
        try:
            if user_obj.vote < 3:
                raise Exception('Недостаточно средств, необходимо 3')
        except Exception:
            context['error_message'] = "Недостаточно средств, необходимо 3$"
            return render(request, 'polls/profile.html', context)
        else:
            seleted_option = request.POST.get('color', '')
            user_obj.color = seleted_option
            user_obj.save()
            user_obj.vote -= 3
            user_obj.save()
    return render(request, 'polls/profile.html', context)
