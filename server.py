"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)


AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
      <html>
        <body>
        Hi! This is the home page. <br>
        <a href="http://0.0.0.0:5000/hello">Take me to submit name</a>
        </body>
      </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Compliments:
            <select name="compliments">
            <option value="awesome">Awesome</option>
            <option value="terrific">Terrific</option>
            <option value="fantastic">Fantastic</option>
            <option value="neato">Neato</option>
            <option value="fantabulous">Fantabulous</option>
            <option value="wowza">Wowza</option>
            <option value="oh-so-not-meh">Oh-Not-So-Meh</option>
            <option value="brilliant">Brilliant</option>
            <option value="ducky">Ducky</option>
            <option value="coolio">Coolio</option>
            <option value="incredible">Incredible</option>
            <option value="wonderful">Wonderful</option>
            <option value="smashing">Smashing</option>
            <option value="lovely">Lovely</option>
          </select>
          <input type="submit" value="Submit">
          <br>
          <a href="http://0.0.0.0:5000/diss">Orrrrr you can go here!</a>

        </form>
      </body>
    </html>
    """

@app.route("/diss")
def get_diss():
  """Prompt user for diss."""

  return """
  <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Disses:
            <select name="disses">
            <option value="boo">Boo</option>
            <option value="lame">Lame</option>
            <option value="icky">Icky</option>
          </select>
          <input type="submit" value="Submit">

        </form>
      </body>
    </html>
    """

@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    niceness = request.args.get("compliments")
    insult = request.args.get("disses")
    # compliment = choice(AWESOMENESS)

    if insult ==  None:
       return """
        <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
            Hi, {}! I think you're {}!
          </body>
        </html>
        """.format(player, niceness)
    else:
        return """
        <!doctype html>
        <html>
          <head>
            <title>A Compliment</title>
          </head>
          <body>
            Hi, {}! I think you're {}!
          </body>
        </html>
        """.format(player, insult)



if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
