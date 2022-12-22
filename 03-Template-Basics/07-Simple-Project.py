# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template("07-solution-index.html")


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.

    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.
    report = False
    username = request.args.get('username')
    lower = any(c.islower() for c in username)
    upper = any(c.isupper() for c in username)
    num_end = username[-1].isdigit() 
    if lower and upper and num_end:
        report = True
    return render_template("07-solution-report.html", report=report, lower=lower, upper=upper, num_end=num_end )

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
