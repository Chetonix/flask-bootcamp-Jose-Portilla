# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome to Pig Latin Translator for your Dog name! Go to /pig_latin/name to see the translation.</h1>"

@app.route('/pig_latin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1] == 'y':
        pig_latin_name = name[0:-1] + 'iful'
    else:
        pig_latin_name = name + 'y'

    return f"<h2>Your Dog name should be {pig_latin_name}</h2>" 

if __name__ == '__main__':
    # Fill me in!
    app.run()
