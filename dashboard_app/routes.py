from dashboard_app import app
from flask import render_template, request, Response, jsonify
import json,  plotly
from scripts.data import return_figures


@app.route('/')
@app.route('/index')

def index():

    return render_template('index.html')