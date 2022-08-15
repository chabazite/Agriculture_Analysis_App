from dashboard_app import app
from flask import render_template, request, session
from flask_session import Session
import json,  plotly
from scripts.dataframe_compile import indicator_url_creation,combine_dataframe
from scripts.home_data import return_index_figure
from scripts.population_data import return_pop_figures
from scripts.economics_data import return_econ_figures
from scripts.land_data import return_land_figures
from scripts.issues_data import return_issues_figures


data_filter_list = ['World','Top 10 Largest Population', 'Top 10 Largest Urban Population', 'Top 10 Largest Rural Population', 'Top 10 largest agricultural land (sq. km)', "Top 10 Largest Population vs. Other"]

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)


@app.route('/')
@app.route('/index')

def index():
	indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'SL.AGR.EMPL.MA.ZS', 
    'SL.AGR.EMPL.FE.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS', 'SH.DYN.MORT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.CO2E.KT', 'SI.POV.UMIC']

	world_bank_columns = ['population', 'total_land_sqkm', 'forest_%','crop_%',
    'agricultural_%','arable_%','cereal_grain_hectare', 'rural_pop_%','urban_pop_%', 'male_employement_ag', 'female_employment_ag', 'fertilizer_consump','cereal_yield_kgPerHectare', 'total_gdp_ag_forestry_fishing', 'mortality_under5', 'Total_Greenhouse_gases', 'CO2_emmission','%Poverty_under5_50_per_day']

	dataframe_list = indicator_url_creation(indicators)

	world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)

	session['world_bank_df'] = world_bank_df


	figures = return_index_figure(world_bank_df)

	

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	return render_template('index.html',figuresJSON=figuresJSON)



@app.route('/population', methods = ['POST','GET'])

def population_page():
	
	world_bank_df = session.get('world_bank_df', None)

	#Parse the Post request for filter groups
	if (request.method == 'POST') and request.form:
		figures = return_pop_figures(world_bank_df,request.form.get('Radio1'))
		choice = request.form.get('Radio1')
	# GET request returns WORLD for initial page log
	else:
		figures = return_pop_figures(world_bank_df,'World')
		choice = 'World'
    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	url = '/population'

	return render_template('population.html', ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'], choice = choice, url = url)


@app.route('/land_use', methods = ['POST','GET'])

def land_use_page():

	world_bank_df = session.get('world_bank_df', None)

	#Parse the Post request for filter groups
	if (request.method == 'POST') and request.form:
		figures = return_land_figures(world_bank_df,request.form.get('Radio1'))
		choice = request.form.get('Radio1')
	# GET request returns WORLD for initial page log
	else:
		figures = return_land_figures(world_bank_df,'World')
		choice = 'World'
    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	url = '/land_use'

	return render_template('land_use.html', ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'], choice = choice, url = url)


@app.route('/economics', methods = ['POST','GET'])

def economics_page():

	#Parse the Post request for filter groups
	if (request.method == 'POST') and request.form:
		figures = return_econ_figures(request.form.get('Radio1'))
		choice = request.form.get('Radio1')
	# GET request returns WORLD for initial page log
	else:
		figures = return_econ_figures('World')
		choice = 'World'
    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	url = '/economics'

	return render_template('economics.html',  ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'], choice = choice, url = url)


@app.route('/global_issues', methods = ['POST','GET'])

def global_issues_page():

	#Parse the Post request for filter groups
	if (request.method == 'POST') and request.form:
		figures = return_issues_figures(request.form.get('Radio1'))
		choice = request.form.get('Radio1')
	# GET request returns WORLD for initial page log
	else:
		figures = return_issues_figures('World')
		choice = 'World'
    # plot ids for the html id tag
	ids = ['figure-{}'.format(i) for i, _ in enumerate(figures)]

	# Convert the plotly figures to JSON for javascript in html template
	figuresJSON = json.dumps(figures, cls=plotly.utils.PlotlyJSONEncoder)

	url = '/global_issues'

	return render_template('global_issues.html', ids=ids,
		figuresJSON=figuresJSON, data_filter_list = data_filter_list, active_btns = ['World'], choice = choice, url = url)