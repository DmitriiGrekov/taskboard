from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class AdvUser(AbstractUser):
    """Модель пользователя"""

    def __str__(self):
        return self.first_name + " " + self.last_name + " -> " + self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        unique_together = ('email',)


class TaskModel(models.Model):
    """Модель записи пользователя"""
    user = models.ForeignKey(AdvUser,
                             verbose_name=("Пользователь"),
                             on_delete=models.CASCADE)
    title = models.CharField(("Заголовок записи"), 
                              max_length=120)
    content = models.TextField(("Описание записи"))
    date_create = models.DateField(("Дата создания"),
                                   auto_now=False,
                                   auto_now_add=True)
    date_saved = models.DateField(("Дата последнего сохранения"),
                                   auto_now=True)
    date_ending = models.DateField(("Дата окончания"))

    def __str__(self):
        return f"{self.user.username} -> {self.title}"
    
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

