from django.db import models

from .common import DIFFICULTY

CATEGORY = [
    ('mobility_legs', 'Mobilidade - Pernas'),
    ('mobility_arms', 'Mobilidade - Braços'),
    ('mobility_trunk', 'Mobilidade - Tronco'),
    ('warmup', 'Aquecimento'),
    ('legs', 'Fortalecimento - Pernas'),
    ('arms', 'Fortalecimento - Braços'),
    ('trunk', 'Fortalecimento - Tronco'),
    ('stretching', 'Alongamento'),
]


class Exercise(models.Model):
    name = models.CharField(max_length=100)

    description = models.TextField()

    sets_reps = models.CharField(max_length=50, null=True, blank=True)
    rest_time = models.CharField(max_length=50, null=True, blank=True)

    tutorial_link = models.URLField()
    difficulty = models.CharField(choices=DIFFICULTY, default='Easy')

    category = models.CharField(choices=CATEGORY, max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class TrainingExercise(models.Model):
    training = models.ForeignKey('Training', on_delete=models.CASCADE)
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)  # Controla a ordem (0, 1, 2...)

    class Meta:
        ordering = ['order']  # O Django sempre vai devolver os exercícios ordenados por este campo


class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Adicionamos o 'through' para avisar o Django que a relação agora tem uma ordem
    exercises = models.ManyToManyField(Exercise, through=TrainingExercise)
    difficulty = models.CharField(choices=DIFFICULTY, default='Easy')

    def __str__(self):
        return self.name
