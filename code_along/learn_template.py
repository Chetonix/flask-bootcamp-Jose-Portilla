from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    name = "Chetonix"

    return render_template('learn_template.html', host = name)

if __name__ == '__main__':
    app.run(debug=True)
