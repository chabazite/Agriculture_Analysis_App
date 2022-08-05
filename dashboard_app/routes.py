from dashboard_app import app
from flask import render_template, request, Response, jsonify
import json,  plotly
from scripts.home_data import return_index_figure
from scripts.population_data import return_pop_figures
from scripts.economics_data import return_econ_figures
from scripts.land_data import return_land_figures
from scripts.issues_data import return_issues_figures

data_filter_list = ['World','Top 10 Highest Population', 'Top 10 Highest Urban Population', 'Top 10 Highest Rural Population', 'Top 10 largest agricultural land (sq. km)', "Top 10 Highest Population vs. Other"]



@app.route('/')
@app.route('/index')

def index():

	figures = return_index_figure()

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html',figuresJSON=figuresJSON)



@app.route('/population', methods = ['POST','GET'])

def population_page():
	
	#Parse the Post request for filter groups
	if (request.method == 'POST') and request.form:
		figures = return_pop_figures(request.form)

	# GET request returns WORLD for initial page log
	else:
		figures = return_pop_figures(['World'])

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('population.html', ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'])


@app.route('/land_use')

def land_use_page():

	figures = return_land_figures()

    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('land_use.html', ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'])


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

	return render_template('global_issues.html', ids=ids,						figuresJSON=figuresJSON)