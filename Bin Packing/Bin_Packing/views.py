"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template
from flask import request, redirect
from Bin_Packing import app
from .Bin import firstFitDecr
from .Bin import firstFit
from .Bin import bestFit

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/', methods=['POST'])
def calc():
    capacity = int(request.form['binCap'])
    weights  = request.form['vals']
    algorithm = request.form['RadioBtn']

    a_list = weights.split()
    map_obj = map(int, a_list)
    ints= list(map_obj)

    bins = 0
    if algorithm == 'First Fit':
         bins = firstFit(ints, capacity)
    elif algorithm == 'First Fit Decreasing':
         bins = firstFitDecr(ints, capacity)
    elif algorithm == 'Best Fit':
         bins = bestFit(ints, capacity)


    return render_template(
        'index.html',
        title='Calculate',
        year=datetime.now().year,
        values = weights,
        algorithm = algorithm,
        capacity = capacity,
        binLen = len(bins),
        binsArr = bins
    )

