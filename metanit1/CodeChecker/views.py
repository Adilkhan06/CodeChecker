import io
import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserProfileForm, CustomPasswordChangeForm
from .models import Task_completed

from django.contrib.auth import login
from django.contrib.auth import logout

from .forms import SignUpForm, SignInForm
from .models import FAQ
from .forms import FAQForm
from .models import Task
from .models import Lecture


def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    return render(request, 'lecture_detail.html', {'lecture': lecture})

def lecture_list(request):
    lectures = Lecture.objects.all()
    return render(request, 'lecture_list.html', {'lectures': lectures})

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html', {'task': task})

# Compiler
def base(request):
    return render(request, 'base.html')

def compiler(request):
    return render(request, 'compiler.html')

def about(request):
    return render(request, 'about.html')




def runcode(request):
    global original_stdout, codeareadata, output
    if request.method == "POST":
        codeareadata = request.POST['codearea']
        output = ""

        try:
            # Redirect stdout to capture output
            original_stdout = sys.stdout
            sys.stdout = sys.stderr = sys.stdout = sys.stderr = io.StringIO()

            exec(codeareadata)

            # Retrieve the captured output
            output = sys.stdout.getvalue()

        except Exception as e:
            output = str(f"{codeareadata} is not correct")

        finally:
            # Reset stdout
            sys.stdout = original_stdout

    return render(request, 'compiler.html', {"code": codeareadata, "output": output})


class HttpResponseNotFound:
    pass


def save_completed_task(user, task_id):
    completed_task = Task_completed(Customuser=user, Task_id=task_id)
    completed_task.save()

def iscorrect(code, task_id, user):
    task = Task.objects.get(pk=task_id)

    if Task_completed.objects.filter(Customuser=user, Task_id=task_id).exists():
        return "Уже выполнено"

    expected_input = task.condition.code_condition if task.condition else 'print("Hello")'
    is_correct = expected_input in code.strip()

    if is_correct:
        save_completed_task(user, task_id)

    return "Правильно" if is_correct else "Неправильно"

def run_task_code(request, task_id):
    global original_stdout, codeareadata, output

    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        return HttpResponseNotFound("Task not found")

    codeareadata = ""

    if request.method == "POST":
        codeareadata = request.POST.get('codearea', '')
        output = ""

        try:
            original_stdout = sys.stdout
            sys.stdout = sys.stderr = sys.stdout = sys.stderr = io.StringIO()

            exec(codeareadata, globals(), locals())

            output = sys.stdout.getvalue()

        except Exception as e:
            output = str(f"{codeareadata} is not correct")

        finally:
            sys.stdout = original_stdout

    return render(request, 'task_detail.html', {"task": task, "code": codeareadata, "output": output, "iscorrect": iscorrect(codeareadata, task.id, request.user)})










def faq_list(request):
    query = request.GET.get('q', '')
    if query:
        faqs = FAQ.objects.filter(question__icontains=query)
    else:
        faqs = FAQ.objects.all()

    return render(request, 'faq_list.html', {'faqs': faqs, 'query': query})

def add_faq(request):
    if request.method == 'POST':
        form = FAQForm(request.POST)
        if form.is_valid():
            faq = form.save(commit=False)
            faq.save()
            return redirect('faq_list')
    else:
        form = FAQForm()
    return render(request, 'add_faq.html', {'form': form})


def view_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)

    if request.method == 'POST':
        form = FAQForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
    else:
        form = FAQForm(instance=faq)

    return render(request, 'view_faq.html', {'faq': faq, 'form': form})





@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        elif password_form.is_valid():
            password_form.save()
            messages.success(request, 'Password changed successfully')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating profile. Please correct the errors below.')
    else:
        user_form = UserProfileForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'password_form': password_form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('basepage')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

def user_logout(request):
    logout(request)
    return redirect('basepage')





