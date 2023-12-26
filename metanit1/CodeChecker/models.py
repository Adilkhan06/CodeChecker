

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class admin_panel(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=40)



class Condition(models.Model):
    code_condition = models.TextField()

    def __str__(self):
        return f'Condition {self.pk}'


class Task(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(default='http://127.0.0.1:8000/tasks//')
    condition = models.ForeignKey(Condition, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title


class Lecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    lecture_link = models.URLField(default='http://127.0.0.1:8000/lectures/')
    assignment_link = models.URLField(default='http://127.0.0.1:8000/tasks/')
    video_url = models.URLField(default='https://www.youtube.com/')
    info = models.TextField(default='.')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lecture_detail', args=[str(self.id)])

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Task_completed(models.Model):
    Customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Task_id = models.TextField(blank=True, null=True)


class FAQ(models.Model):
    user_name = models.CharField(max_length=100, default='Anonymous')
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
