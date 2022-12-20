from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/about_me')
def about():
    return "<h2>I am a dazzling boy!</h2>"

@app.route('/about/<user>')
def user_info(user):
    return f"<h3>Hello {user}</h3>"

if __name__ == '__main__':
    app.run()


