import uuid

from django.core import validators
from django.db import models


class Category(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Название', unique=True, db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Program(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='programs')
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

    def __str__(self):
        return '{} | {} дней '.format(self.name, self.duration)


class MuscleGroup(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Название', unique=True)

    class Meta:
        verbose_name = 'Группа мышц'
        verbose_name_plural = 'Группы мышц'

    def __str__(self):
        return self.name


class Exercise(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    muscle_group = models.ManyToManyField('MuscleGroup', verbose_name='Мышечная группа',
                                          related_name='exercises')
    name = models.CharField(verbose_name='Название', unique=True)
    video_instruction = models.CharField(verbose_name='Видео инструкция (URL)', null=True, blank=True)

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return '{} | {}'.format(self.name, '')

    def get_muscle_groups(self):
        return ' | '.join([group.name for group in self.muscle_group.all()])

    get_muscle_groups.short_description = 'Группы мышц'


class Week(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    name = models.IntegerField(verbose_name='Номер', unique=True)
    program = models.ForeignKey('Program', on_delete=models.CASCADE, verbose_name='Программа', related_name='weeks')

    class Meta:
        verbose_name = 'Неделя'
        verbose_name_plural = 'Недели'


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    status = models.BooleanField(verbose_name='Статус (завершена/не завершена)', default=False)
    week = models.ForeignKey('Week', on_delete=models.CASCADE, related_name='workouts', verbose_name='Неделя')

    class Meta:
        verbose_name = 'Тренировка'
        verbose_name_plural = 'Тренировки'


class TrainingExercise(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, db_index=True, default=uuid.uuid4)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, verbose_name='Упражнение',
                                 related_name='training_exercises')
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE, verbose_name='Тренировка',
                                related_name='training_exercises')
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

    class Meta:
        verbose_name = 'Упражнение на тренировке'
        verbose_name_plural = 'Упражнения на тренировке'
