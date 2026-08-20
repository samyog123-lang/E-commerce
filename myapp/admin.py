from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from datetime import datetime, timedelta
from .models import Customer, Order

# Create blueprint for admin
admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')  # admin dashboard route
@login_required
def admin_dashboard():
    if current_user.email != "npanthi@gmail.com":
        flash("Access Denied: Admins only", "danger")
        return redirect(url_for('views.home'))

    total_users = Customer.query.count()
    total_orders = Order.query.count()

    total_revenue = 0
    for o in Order.query.all():
        try:
            price = float(o.product_price.replace('रु','').replace(',',''))
            total_revenue += price
        except:
            continue

    # Orders last 7 days
    labels = []
    orders_per_day = []
    for i in range(6,-1,-1):
        day = datetime.utcnow() - timedelta(days=i)
        labels.append(day.strftime('%a %d'))
        count = Order.query.filter(
            Order.created_at >= datetime(day.year, day.month, day.day),
            Order.created_at < datetime(day.year, day.month, day.day) + timedelta(days=1)
        ).count()
        orders_per_day.append(count)

    recent_orders = Order.query.order_by(Order.created_at.desc()).limit(5).all()

    return render_template(
        'admin.html',
        total_users=total_users,
        total_orders=total_orders,
        total_revenue=total_revenue,
        labels=labels,
        orders_per_day=orders_per_day,
        recent_orders=recent_orders
    )
