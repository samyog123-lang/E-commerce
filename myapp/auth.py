from flask import Blueprint, render_template, flash, redirect, url_for, request
from .forms import LoginForm, SignupForm
from .models import Customer
from . import db
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)

# --- LOGIN ---
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash('Already logged in', 'info')
        # Redirect admin straight to dashboard
        if current_user.email == "npanthi@gmail.com":
            return redirect(url_for('admin.admin_dashboard'))
        return redirect(url_for('views.home'))

    form = LoginForm()
    if form.validate_on_submit():
        user = Customer.query.filter_by(email=form.email.data).first()

        # ✅ Use check_password() instead of verify_password()
        if user and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash(f'Logged in as {user.username}', 'success')

            # Admin redirect
            if user.email == "npanthi@gmail.com":
                return redirect(url_for('admin.admin_dashboard'))

            return redirect(url_for('views.home'))

        flash('Invalid email or password', 'danger')
        return redirect(url_for('auth.login'))

    return render_template('login.html', form=form)


# --- SIGNUP ---
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        flash('Already logged in', 'info')
        return redirect(url_for('views.home'))

    form = SignupForm()
    if form.validate_on_submit():
        # Check if email is already registered
        existing_user = Customer.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already exists', 'warning')
            return redirect(url_for('auth.signup'))

        # Create new user
        new_user = Customer(
            email=form.email.data,
            username=form.username.data
        )
        # ✅ Use set_password() to hash the password
        new_user.set_password(form.password1.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully. Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


# --- LOGOUT ---
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
