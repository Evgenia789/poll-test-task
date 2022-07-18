from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Question(models.Model):
    """
    Класс Question для создания вопросов.
    """
    title = models.CharField(
        max_length=200,
        verbose_name='Вопрос',
        help_text='Введите вопрос'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(verbose_name="Опубликован")

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.title


class Answer(models.Model):
    """
    Класс Answer для создания ответов.
    """
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )
    answer = models.CharField(
        max_length=200,
        verbose_name='Ответ',
        help_text='Введите вариант ответа'
    )
    vote = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer


class UserQuestion(models.Model):
    """
    Класс UserQuestion, определяет на
    какие вопросы ответил пользователь.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Вопрос'
    )

    class Meta:
        verbose_name = 'Вопрос на который ответил пользователь'
        verbose_name_plural = 'Вопросы на которые ответил пользователь'
        constraints = [models.UniqueConstraint(
            fields=['user', 'question'],
            name='unique_question'
        )]

    def __str__(self):
        return (
            f'Пользователь: {self.user.username} '
            f'ответил на вопрос: {self.question.title}'
        )


class UserPoint(models.Model):
    """
    Класс UserPoint, определяет для каждого пользователя количество
    ответов на вопросы и заработанной валюты за эти ответы, которую
    можно потратить на изменение цвета фона профиля пользователя.
    """
    COLORS = [
        ('Синий', 'primary'),
        ('Серый', 'secondary'),
        ('Зеленый', 'success'),
        ('Красный', 'danger'),
        ('Желтый', 'warning'),
        ('Бирюзовый', 'info'),
        ('Белый', 'white')
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    vote = models.IntegerField(default=0)
    count_answer = models.IntegerField(default=0)
    color = models.CharField(
        max_length=200,
        choices=COLORS,
        default='white'
    )

    class Meta:
        ordering = ['-count_answer']
        verbose_name = 'Баллы пользователя'
        verbose_name_plural = 'Баллы пользователей'

    def __str__(self):
        return (
            f'Пользователь: {self.user.username} '
            f'ответил на вопросов: {self.count_answer} '
            f'заработал валюты: {self.vote} '
        )
