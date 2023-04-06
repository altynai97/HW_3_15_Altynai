import os
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .models import Course, Student, User
from .forms import CourseForm, StudentForm, CourseUpdateForm, StudentUpdateForm, UserRegisterForm, UserLoginForm
from app import db


def index():
    title = 'Онлайн Курсы'
    courses = Course.query.all()
    return render_template('index.html', title=title, courses=courses)


@login_required
def admin_course_create():
    form = CourseForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_course = Course()
            form.populate_obj(new_course)
            db.session.add(new_course)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            print(form.errors)
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При сохранении категории произошла ошибка{". ".join(text_list)}', 'Ошибка!')
    return render_template('admin/form.html', form=form)


def course_detail(course_id):
    course = Course.query.get(course_id)
    title = course.name
    return render_template('movie_detail.html', course=course, title=title)


@login_required
def admin_student_create():
    form = StudentForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_student = Student()
            form.populate_obj(new_student)
            db.session.add(new_student)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            print(form.errors)
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При сохранении категории произошла ошибка{". ".join(text_list)}', 'Ошибка!')
    return render_template('admin/form.html', form=form)


@login_required
def admin_course_list():
    courses_list = Course.query.all()
    return render_template('admin/course_list.html', courses_list=courses_list)


@login_required
def admin_student_list():
    students_list = Student.query.all()
    return render_template('admin/student_list.html', students_list=students_list)


@login_required
def admin_course_update(course_id):
    course = Course.query.get(course_id)
    form = CourseUpdateForm(meta={'csrf': False}, obj=course)
    if request.method == 'POST':
        form.populate_obj(course)
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('courses_list'))
    else:
        print(form.errors)
    return render_template('admin/form.html', form=form)


@login_required
def admin_student_update(student_id):
    student = Student.query.get(student_id)
    form = StudentUpdateForm(meta={'csrf': False}, obj=student)
    if request.method == 'POST':
        form.populate_obj(student)
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('admin_students_list'))
    else:
        print(form.errors)
    return render_template('admin/student_form.html', form=form)


@login_required
def admin_course_delete(course_id):
    course = Course.query.get(course_id)
    if request.method == 'POST':
        db.session.delete(course)
        db.session.commit()
        return redirect(url_for('admin_movie_list'))
    return render_template('admin/course_delete.html', course=course)


@login_required
def admin_student_delete(student_id):
    student = Student.query.get(student_id)
    if request.method == 'POST':
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('admin_students_list'))
    return render_template('admin/student_delete.html', student=student)


def user_register():
    form = UserRegisterForm()
    title = 'Регистрация'
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Пользователь {new_user.username} успешно зарегистрирован!', 'Успех!')
            return redirect(url_for('user_login'))
        else:
            text_list = []
            for field, errors in form.errors.items():
                text_list.append(f'{field} : {", ".join(errors)}')
            flash(f'При регистрации произошла ошибка{". ".join(text_list)}', 'Ошибка!')

    return render_template('accounts/index.html', form=form, title=title)


def user_login():
    form = UserLoginForm()
    title = 'Авторизация'
    if request.method == 'POST':
        if form.validate_on_submit():
            username = form.username.data
            password = form.password.data
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Вы успешно вошли в систему', 'Успех!')
                return redirect(url_for('index'))
            else:
                flash('Неверные логин и пароль', 'Ошибка!')

    return render_template('accounts/index.html', form=form, title=title)


def user_logout():
    logout_user()
    return redirect(url_for('user_login'))
