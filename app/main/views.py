from flask import render_template
from . import main

@main.route
def index():
    title = "Welcome to blog-site"

    return render_template('index.html',title=title)