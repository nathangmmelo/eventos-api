from flask import Flask
from database import init_db
from routes.users import users_bp
from routes.events import events_bp
from routes.tickets import tickets_bp

app = Flask(__name__)

init_db()

app.register_blueprint(users_bp)
app.register_blueprint(events_bp)
app.register_blueprint(tickets_bp)

if __name__ == '__main__':
    app.run(debug=True)