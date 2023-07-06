from django.contrib import admin

from programs import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)


@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'duration', 'price')
    list_filter = ('name', 'category', 'duration', 'price')


class MuscleGroupInline(admin.TabularInline):
    model = models.Exercise.muscle_group.through
    verbose_name = u"Группа мышц"
    verbose_name_plural = u"Группы мышц"


@admin.register(models.MuscleGroup)
class MuscleGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)


@admin.register(models.Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_muscle_groups')
    inlines = (
        MuscleGroupInline,
    )


@admin.register(models.Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ('id', 'program', 'name')
    list_filter = ('name', 'program')


@admin.register(models.Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('id', 'week', 'status')
    list_filter = ('week', 'status')


@admin.register(models.TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    list_display = ('id', 'workout', 'exercise')
    list_filter = ('workout', 'exercise')
