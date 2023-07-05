import uuid

from django.core import validators
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Название', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Program(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', unique=True)
    duration = models.IntegerField(verbose_name='Продолжительность (дней)')
    short_description = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена (руб.)',
        validators=[
            validators.MinValueValidator(0),
        ]
    )

    class Meta:
        verbose_name = 'Программа тренировок'
        verbose_name_plural = 'Программы тренировок'


class Week(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)


class Workout(models.Model):  # тренировка
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)


class MuscleGroup(models.Model):  # группа мышц
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)


class Exercise(models.Model):  # упражнение
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    muscle_group = models.ForeignKey('MuscleGroup', on_delete=models.CASCADE)
