from flask import render_template, redirect, url_for, flash
from app import login_required

@login_required
def index():
    return render_template('index.html')