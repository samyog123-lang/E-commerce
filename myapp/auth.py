from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import LoginForm, SignupForm
from .models import Customer
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in', 'info')
        if current_user.email == "npanthi@gmail.com":
            return redirect(url_for('admin.admin_dashboard'))
        return redirect(url_for('views.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash(f'Logged in as {user.username}', 'success')


            if user.email == "npanthi@gmail.com":
                return redirect(url_for('admin.admin_dashboard'))

            return redirect(url_for('views.home'))

        flash('Invalid email or password', 'danger')
        return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)



@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash('Already logged in', 'info')
        return redirect(url_for('views.home'))

    form = SignupForm()
    if form.validate_on_submit():

        existing_user = Customer.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists', 'warning')
            return redirect(url_for('auth.signup'))

        new_user = Customer(
            email=form.email.data,
            username=form.username.data
        )

        new_user.set_password(form.password1.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
