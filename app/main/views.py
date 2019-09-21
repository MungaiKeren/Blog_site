from flask import render_template
from . import main
from ..requests import get_quotes

@main.route('/')
def index():
    title = "Bloggy-site"
    # Getting the quotes
    quote_message = get_quotes('quote')

    return render_template('index.html',title=title,quote_message=quote_message)