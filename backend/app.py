from flask import Flask
from routes.login import login_bp
from routes.register import register_bp

app = Flask(__name__)


app.register_blueprint(register_bp, url_prefix='/api')
app.register_blueprint(login_bp, url_prefix='/api')


@app.route('/')
def home():
    return {"message": "Welcome to PointConnect!"}


if __name__ == '__main__':
    app.run(debug=True)
