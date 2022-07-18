from django.contrib import admin

from polls.models import (Answer,  # isort:skip
                          Question, UserPoint, UserQuestion)


class AnswerInline(admin.TabularInline):
    """
    Класс AnswerInline позволяет редактировать
    модель Answer на той же странице, что и модель Question.
    """
    model = Answer
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Класс QuestionAdmin для редактирования
    модели Question в интерфейсе админ-зоны.
    """
    list_display = (
        'title',
        'is_active'
    )
    inlines = [AnswerInline]


@admin.register(UserQuestion)
class UserQuestionAdmin(admin.ModelAdmin):
    """
    Класс UserQuestionAdmin для редактирования
    модели UserQuestion в интерфейсе админ-зоны.
    """
    list_display = (
        'user',
        'question'
    )
    list_filter = ('user',)
    search_fields = ('user',)


@admin.register(UserPoint)
class UserPointAdmin(admin.ModelAdmin):
    """
    Класс UserPointAdmin для редактирования
    модели UserPoint в интерфейсе админ-зоны.
    """
    list_display = (
        'user',
        'vote',
        'count_answer'
    )
    list_filter = ('user',)
    search_fields = ('user',)
