
from myapp import create_app, db
from myapp.models import Customer, Order

app = create_app()
app.app_context().push()  

db.create_all()
print("Database tables created successfully!")

if not Customer.query.filter_by(email="npanthi@gmail.com").first():
    admin = Customer(email="npanthi@gmail.com", username="npanthi12")
    admin.password = "npanthi@123#"  # set password
    db.session.add(admin)
    db.session.commit()
    print(" Admin user created!")
