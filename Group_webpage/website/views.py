from flask import Blueprint, render_template, request, flash, jsonify

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html", current_page='home')

@views.route('/pi_page', methods=['GET'])
def pi_page():
    return render_template('PI_page.html', current_page='pi_page')

@views.route('/members', methods=['GET'])
def members():
    return render_template('members.html', current_page='members')

@views.route('/opportunities', methods=['GET'])
def opportunities():
    return render_template('opportunities.html', current_page='opportunities')

@views.route('/publications', methods=['GET'])
def publications():
    return render_template('publications.html', current_page='publications')