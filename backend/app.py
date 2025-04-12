from flask import Flask
import os
from oauth import oauth
from routes.login import login_bp
from routes.register import register_bp

app = Flask(__name__)
app.secret_key = os.getenv(
    "FLASK_SECRET_KEY", "a3f5c8d9e2b4a6c7d8f9e0a1b2c3d4e5")
print(f"Secret Key: {app.secret_key}")

# Initialize OAuth with the app
oauth.init_app(app)

app.register_blueprint(register_bp, url_prefix='/api')
app.register_blueprint(login_bp, url_prefix='/api')


@app.route('/')
def home():
    return {"message": "Welcome to PointConnect!"}


if __name__ == '__main__':
    app.run(debug=True)
