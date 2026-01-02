from app import create_app, db
from app.models import User, Shipment

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Shipment': Shipment}

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created successfully")
