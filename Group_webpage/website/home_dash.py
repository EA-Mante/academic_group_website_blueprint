from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash, make_response
from werkzeug.utils import secure_filename
from . import db 
import json

home_dash = Blueprint("home_dash", __name__)

@home_dash.route('/members', methods=['GET'])
def members():
    return render_template('members.html')

@home_dash.route('/opportunities', methods=['GET'])
def opportunities():
    return render_template('opportunities.html')

@home_dash.route('/publications', methods=['GET'])
def publications():
    return render_template('publications.html')