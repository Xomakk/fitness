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


class MuscleGroup(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Группа мышц'
        verbose_name_plural = 'Группы мышц'


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    muscle_group = models.ForeignKey('MuscleGroup', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class Week(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    status = models.BooleanField(verbose_name='Статус (завершена/не завершена)', default=False)
    week = models.ForeignKey('Week', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class TrainingExercise(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
    number_repetitions = models.IntegerField(
        verbose_name='Количество повторений',
        validators=[
            validators.MinValueValidator(0),
        ]
    )
    warmup_approach = models.IntegerField(
        verbose_name='Количество разминочных подходов',
        validators=[
            validators.MinValueValidator(0),
        ]
    )
    working_approach = models.IntegerField(
        verbose_name='Количество рабочих подходов',
        validators=[
            validators.MinValueValidator(0),
        ]
    )
