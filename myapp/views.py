from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app, session
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .forms import ChangePasswordForm
from . import db
from .models import Customer, Order  # <-- fixed
import os
from datetime import datetime, timedelta


views = Blueprint('views', __name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# -------------------- HOME --------------------
@views.route('/')
@login_required
def home():
    return render_template('index.html')

# -------------------- PROFILE --------------------
@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ChangePasswordForm()

    if request.method == 'POST':
        # ----------- PROFILE PICTURE -----------
        if 'profile_pic' in request.files:
            file = request.files['profile_pic']
            if file and allowed_file(file.filename):
                # Secure the filename
                filename = secure_filename(file.filename)

                # Absolute path to save
                upload_folder = os.path.join(current_app.root_path, 'static/images/profile_pics')
                os.makedirs(upload_folder, exist_ok=True)  # Ensure folder exists

                filepath = os.path.join(upload_folder, filename)
                file.save(filepath)

                # Update database
                current_user.profile_pic = filename
                db.session.commit()
                flash('✅ Profile picture updated!')

        # ----------- PASSWORD CHANGE -----------
        if form.validate_on_submit():
            if not current_user.verify_password(form.current_password.data):
                flash('❌ Current password is incorrect')
                return redirect(url_for('views.profile'))

            current_user.password = form.new_password.data
            db.session.commit()
            flash('✅ Password changed successfully!')
            return redirect(url_for('views.profile'))

    return render_template('profile.html', form=form)

@views.route('/shop')
@login_required  # optional, if you want only logged-in users
def shop():
    return render_template('shop.html',products=all_products)

@views.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    if not cart_items:
        message = "Your cart is empty!"
    else:
        message = ""
    return render_template('cart.html', cart_items=cart_items, message=message)

@views.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    # Get product from form (convert ID to int)
    product = {
        "id": int(request.form.get("id")),
        "name": request.form.get("name"),
        "price": request.form.get("price"),
        "image": request.form.get("image"),
    }

    # Get current cart or empty list
    cart = session.get('cart', [])

    # Append product
    cart.append(product)

    # Save back to session
    session['cart'] = cart

    # Redirect to cart page
    return redirect(url_for('views.cart'))

# products.py
all_products = [
    {"id": 1, "name": "Apple iPhone 14", "price": "रु99,999", "image": "https://images.unsplash.com/photo-1661447117654-5d8a2b2a0b6f"},
    {"id": 2, "name": "MacBook Pro 16", "price": "रु299,999", "image": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"},
    {"id": 3, "name": "Sony WH-1000XM5 Headphones", "price": "रु49,999", "image": "https://images.unsplash.com/photo-1591122332193-d7b7d36ef2b8"},
    {"id": 4, "name": "Samsung Galaxy S23", "price": "रु109,999", "image": "https://images.unsplash.com/photo-1677184638217-9b29f27f4ec7"},
    {"id": 5, "name": "Nike Air Max 270", "price": "रु19,999", "image": "https://images.unsplash.com/photo-1612461234519-4d57b5f88f44"},
    {"id": 6, "name": "Adidas Ultraboost", "price": "रु21,999", "image": "https://images.unsplash.com/photo-1600180758895-d6b1a8f7e798"},
    {"id": 7, "name": "Dell XPS 13 Laptop", "price": "रु149,999", "image": "https://images.unsplash.com/photo-1580910051070-15f8e3d83c68"},
    {"id": 8, "name": "Canon EOS R5 Camera", "price": "रु439,999", "image": "https://images.unsplash.com/photo-1606813909395-cb489fe22d9a"},
    {"id": 9, "name": "Logitech MX Master 3", "price": "रु11,999", "image": "https://images.unsplash.com/photo-1615559601203-0d2232baf47b"},
    {"id": 10, "name": "Amazon Echo Dot 5th Gen", "price": "रु5,999", "image": "https://images.unsplash.com/photo-1598332901093-9f8d30f93f0d"},
    {"id": 11, "name": "PlayStation 5", "price": "रु69,999", "image": "https://images.unsplash.com/photo-1606819054492-145ba45a2a65"},
    {"id": 12, "name": "Xbox Series X", "price": "रु69,999", "image": "https://images.unsplash.com/photo-1615393567302-b2b0f9aa9476"},
    {"id": 13, "name": "Kindle Paperwhite", "price": "रु14,999", "image": "https://images.unsplash.com/photo-1605708904505-7e3f9c805e48"},
    {"id": 14, "name": "GoPro Hero 10", "price": "रु49,999", "image": "https://images.unsplash.com/photo-1624287550047-79d78008f29e"},
    {"id": 15, "name": "Apple Watch Series 8", "price": "रु49,999", "image": "https://images.unsplash.com/photo-1661425561647-84d2c56d2fae"},
    {"id": 16, "name": "Samsung Galaxy Watch 5", "price": "रु39,999", "image": "https://images.unsplash.com/photo-1665683796394-5a8c7e7f9f44"},
    {"id": 17, "name": "Bose QuietComfort 45", "price": "रु39,999", "image": "https://images.unsplash.com/photo-1585386959984-a415522c2f1f"},
    {"id": 18, "name": "Microsoft Surface Laptop 5", "price": "रु149,999", "image": "https://images.unsplash.com/photo-1654784942337-08de8dff6bc1"},
    {"id": 19, "name": "iPad Pro 12.9", "price": "रु109,999", "image": "https://images.unsplash.com/photo-1592194996308-7b43878e84a6"},
    {"id": 20, "name": "HP Spectre x360", "price": "रु119,999", "image": "https://images.unsplash.com/photo-1614373611760-8b70b9e7b5e1"},
    {"id": 21, "name": "Sony PlayStation Controller", "price": "रु8,499", "image": "https://images.unsplash.com/photo-1583077044002-5b1f1e66d3f4"},
    {"id": 22, "name": "Samsung Galaxy Buds 2", "price": "रु7,999", "image": "https://images.unsplash.com/photo-1622112540201-1a3c05bfe425"},
    {"id": 23, "name": "Apple AirPods Pro 2", "price": "रु24,999", "image": "https://images.unsplash.com/photo-1611066177505-5a6f0ee7b7c4"},
    {"id": 24, "name": "Razer DeathAdder V2 Mouse", "price": "रु8,499", "image": "https://images.unsplash.com/photo-1620245535155-40c449179d38"},
    {"id": 25, "name": "Logitech G502 Mouse", "price": "रु5,499", "image": "https://images.unsplash.com/photo-1596125312560-9d53d4a2d89e"},
    {"id": 26, "name": "ASUS ROG Strix Laptop", "price": "रु199,999", "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c"},
    {"id": 27, "name": "Nintendo Switch OLED", "price": "रु34,999", "image": "https://images.unsplash.com/photo-1623731134577-3db2e8b0f55c"},
    {"id": 28, "name": "Google Pixel 7", "price": "रु79,999", "image": "https://images.unsplash.com/photo-1676436323215-f9d0c2a6a1dc"},
    {"id": 29, "name": "OnePlus 11", "price": "रु79,999", "image": "https://images.unsplash.com/photo-1675150210411-7bb814a06b27"},
    {"id": 30, "name": "DJI Mavic 3 Drone", "price": "रु2,99,999", "image": "https://images.unsplash.com/photo-1626480668918-d1d8e6a07fc6"},
    {"id": 31, "name": "Samsung QLED TV 65\"", "price": "रु149,999", "image": "https://images.unsplash.com/photo-1619489461471-2a0bc3f4df95"},
    {"id": 32, "name": "LG OLED TV 55\"", "price": "रु129,999", "image": "https://images.unsplash.com/photo-1624112168917-6b58d7e4f17b"},
    {"id": 33, "name": "Sony Bravia 65\" TV", "price": "रु179,999", "image": "https://images.unsplash.com/photo-1613141191362-c8a4f0b9de1c"},
    {"id": 34, "name": "Apple Mac Mini M2", "price": "रु99,999", "image": "https://images.unsplash.com/photo-1622374202546-f3b9c3a2f1d5"},
    {"id": 35, "name": "Amazon Fire TV Stick 4K", "price": "रु5,999", "image": "https://images.unsplash.com/photo-1624480791101-8b7f6e9e1d9c"},
    {"id": 36, "name": "JBL Flip 6 Speaker", "price": "रु12,999", "image": "https://images.unsplash.com/photo-1623994703562-6340f1b0c3d2"},
    {"id": 37, "name": "Anker Soundcore Liberty Air 2", "price": "रु9,999", "image": "https://images.unsplash.com/photo-1623768129637-0f1e8c0f6a3b"},
    {"id": 38, "name": "Samsung Galaxy Tab S8", "price": "रु74,999", "image": "https://images.unsplash.com/photo-1624678916505-42f9e0a9c2b3"},
    {"id": 39, "name": "Apple iMac 24\"", "price": "रु129,999", "image": "https://images.unsplash.com/photo-1623246919180-2b2f8f2c4a5e"},
    {"id": 40, "name": "Lenovo ThinkPad X1", "price": "रु139,999", "image": "https://images.unsplash.com/photo-1623211123450-7b1f3f4a1d4e"},
    {"id": 41, "name": "Garmin Forerunner 245", "price": "रु29,999", "image": "https://images.unsplash.com/photo-1624356129800-5d4b7c1b3f6e"},
    {"id": 42, "name": "Fitbit Charge 5", "price": "रु12,999", "image": "https://images.unsplash.com/photo-1624445551234-4a6c7b2e1d5c"},
    {"id": 43, "name": "Canon EOS 5D Mark IV", "price": "रु249,999", "image": "https://images.unsplash.com/photo-1623456789012-2f3b4c5d6e7f"},
    {"id": 44, "name": "Nikon Z6 II Camera", "price": "रु199,999", "image": "https://images.unsplash.com/photo-1623678901234-3f4b5c6d7e8f"},
    {"id": 45, "name": "Apple TV 4K", "price": "रु17,999", "image": "https://images.unsplash.com/photo-1623789012345-1a2b3c4d5e6f"},
    {"id": 46, "name": "Roku Streaming Stick+", "price": "रु5,999", "image": "https://images.unsplash.com/photo-1623890123456-7b8c9d0e1f2a"},
    {"id": 47, "name": "Samsung Galaxy Book 3", "price": "रु119,999", "image": "https://images.unsplash.com/photo-1623990012345-5f6a7b8c9d0e"},
    {"id": 48, "name": "HP Omen 16 Gaming Laptop", "price": "रु149,999", "image": "https://images.unsplash.com/photo-1624001234567-2f3a4b5c6d7e"},
    {"id": 49, "name": "Apple MacBook Air M2", "price": "रु99,999", "image": "https://images.unsplash.com/photo-1624101234567-3a4b5c6d7e8f"},
    {"id": 50, "name": "Sony Alpha a7 IV", "price": "रु249,999", "image": "https://images.unsplash.com/photo-1624201234567-4b5c6d7e8f9a"}
]
@views.route('/checkout/<int:product_id>', methods=['GET', 'POST'])
@login_required
def checkout(product_id):
    product = next((p for p in all_products if p["id"] == product_id), None)
    if not product:
        flash("Product not found!")
        return redirect(url_for('views.shop'))

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        address = request.form.get('address')
        payment = request.form.get('payment')

        # ---------------- KHALTI PAYMENT ----------------
        if payment.lower() == 'khalti':

            # Save checkout info temporarily
            session['checkout_data'] = {
                "name": name,
                "email": email,
                "address": address
            }

            txn_id = f"{current_user.id}_{product['id']}_{os.urandom(4).hex()}"
            amount = int(product['price'].replace('रु','').replace(',','')) * 100

            return redirect(
                f"https://khalti.com/payment/start?amount={amount}"
                f"&txn_id={txn_id}"
                f"&success={url_for('views.khalti_success', _external=True)}"
                f"&fail={url_for('views.khalti_fail', _external=True)}"
            )

        # ---------------- COD / OFFLINE ----------------
        else:
            new_order = Order(
                user_id=current_user.id,
                product_id=product["id"],
                product_name=product["name"],
                product_price=product["price"],
                product_image=product["image"],
                name=name,
                email=email,
                address=address,
                payment_method=payment,
                payment_status="Pending"
            )
            db.session.add(new_order)
            db.session.commit()

            return redirect(url_for('views.order_success', order_id=new_order.id))

    return render_template('checkout.html', product=product)
@views.route('/khalti-success')
@login_required
def khalti_success():
    txn_id = request.args.get('txn_id')
    if not txn_id:
        flash("Invalid transaction!")
        return redirect(url_for('views.shop'))

    try:
        product_id = int(txn_id.split('_')[1])
    except:
        flash("Invalid transaction ID!")
        return redirect(url_for('views.shop'))

    product = next((p for p in all_products if p["id"] == product_id), None)
    if not product:
        flash("Product not found!")
        return redirect(url_for('views.shop'))

    # Get stored checkout info
    data = session.pop('checkout_data', None)
    if not data:
        flash("Session expired. Please try again.")
        return redirect(url_for('views.shop'))

    new_order = Order(
        user_id=current_user.id,
        product_id=product["id"],
        product_name=product["name"],
        product_price=product["price"],
        product_image=product["image"],
        name=data["name"],
        email=data["email"],
        address=data["address"],
        payment_method="Khalti",
        payment_status="Paid"
    )
    db.session.add(new_order)
    db.session.commit()

    flash("✅ Payment successful and order placed!")
    return redirect(url_for('views.order_success', order_id=new_order.id))
@views.route('/khalti-fail')
@login_required
def khalti_fail():
    flash("❌ Payment failed. Try again.")
    return redirect(url_for('views.cart'))
@views.route('/order-success/<int:order_id>')
@login_required
def order_success(order_id):
    order = Order.query.get_or_404(order_id)
    return render_template('order_success.html', order=order)

