"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, request
from lib.slack import Message, ResponseSchedule
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Hello World!'


@app.route('/schedule', methods=['POST'])
def schedule():
    msg = Message.parse(request)
    bot = ResponseTranslate(msg)
    return bot.translate()

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
