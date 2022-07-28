from dashboard_app import app
from flask import render_template, request, Response, jsonify
import json,  plotly
from scripts.home_data import return_index_figure
from scripts.population_data import return_pop_figures
from scripts.economics_data import return_econ_figures
from scripts.land_data import return_land_figures
from scripts.issues_data import return_issues_figures

@app.route('/')
@app.route('/index')

def index():

	figures = return_index_figure()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html', ids=ids,
		figuresJSON=figuresJSON)



@app.route('/population')

def population_page():

	figures = return_pop_figures()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('population.html', ids=ids,
		figuresJSON=figuresJSON)



@app.route('/economics')

def economics_page():

	figures = return_econ_figures()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('economics.html', ids=ids,
		figuresJSON=figuresJSON)


@app.route('/global_issues')

def global_issues_page():

	figures = return_issues_figures()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('global_issues.html', ids=ids,
		figuresJSON=figuresJSON)


@app.route('/land_use')

def land_use_page():

	figures = return_land_figures()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('land_use.html', ids=ids,
		figuresJSON=figuresJSON)
