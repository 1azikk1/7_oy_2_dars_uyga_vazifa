from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Student
from .forms import CourseForm, LoginForm, RegisterForm, StudentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    students = Student.objects.all()
    context = {
        'title': "Asosiy Sahifa",
        'students': students,
    }
    return render(request, 'courses.html', context)


def students_by_course(request, course_id):
    students = Student.objects.filter(course_id=course_id)
    course = Course.objects.get(pk=course_id)
    context = {
        'course': course,
        'students': students,
        "title": f"{course.title}: talabalar!"
    }
    return render(request, 'index.html', context)


@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {
        'student': student,
        'title': f"{student.course.title}: {student.name}"
    }
    return render(request, 'student_detail.html', context)


@login_required
def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
        'title': course.description,
    }
    return render(request, 'detail.html', context)


@permission_required('education.add_course', '404')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, "Kurs muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        'form': form,
        'title': "Kurs qo'shish"
    }
    return render(request, 'add_course.html', context)


@permission_required('education.change_course', '404')
def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Dars muvaffaqiyatli tarzda o'zgartirildi!")
            return redirect('course_detail', course_id=course.pk)

    form = CourseForm(instance=course)

    context = {
        'form': form,
        'course': course,
        'photo': course.photo
    }
    return render(request, 'add_course.html', context)


@permission_required('education.delete_course', '404')
def delete_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Kurs muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'course': course,
        'title': f"{course.title} kursini o'chirish!"
    }
    messages.warning(request, "Ushbu kursni o'chirmoqchimisiz?")
    return render(request, 'delete_confirm.html', context)


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"{user.username} tabriklaymiz, muvaffaqiyatli tarzda ro'yhatdan o'tdingiz!")
            return redirect('user_login')
    else:
        form = RegisterForm()

    context = {
        'form': form,
        'title': "Ro'yhatdan o'tish"
    }
    return render(request, 'auth/register.html', context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, f"{user.username} web sahifamizga xush kelibsiz!")
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    context = {
        'form': form,
        'title': "Saytga kirish"
    }
    return render(request, 'auth/login.html', context)


def user_logout(request):
    logout(request)
    messages.success(request, "Siz web sahifamizdan chiqib ketdingiz!")
    return redirect('user_login')


def error_404(request):
    return render(request, '404.html', status=404)


@permission_required('education.add_student', '404')
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, "Talaba muvaffaqiyatli tarzda qo'shildi!")
            return redirect('home')
    else:
        form = StudentForm()
    context = {
        'form': form,
        'title': "Student qo'shish!"
    }
    return render(request, 'add_student.html', context)


@permission_required('education.delete_student', '404')
def delete_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Talaba muvaffaqiyatli tarzda o'chirildi!")
        return redirect('home')

    context = {
        'student': student,
        'title': "Talabani o'chirish"
    }
    messages.warning(request, "Ushbu talabani o'chirib tashlamoqchimisiz?")
    return render(request, 'delete_confirm_student.html', context)


@permission_required('education.change_student', '404')
def update_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Talaba muvaffaqiyatli tarzda o'zgartirildi")
            return redirect('student_detail', student_id=student.pk)

    form = StudentForm(instance=student)

    context = {
        'student': student,
        'form': form
    }
    return render(request, 'add_student.html', context)

