import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation,  combine_dataframe, format_dataframe
from scripts.additional_features import create_issue_features, mortality_rate

indicators = ['SP.POP.TOTL','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS','SH.DYN.MORT', 'EN.ATM.GHGT.KT.CE', 'SI.POV.UMIC']

world_bank_columns = ['population', 'rural_pop_%','urban_pop_%', 'mortality_under5', 'Total_Greenhouse_gases', '%Poverty_under5_50_per_day']


def return_issues_figures(data_filter_choice):
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df = create_issue_features(world_bank_df)
    world_bank_df = format_dataframe (world_bank_df, data_filter_choice)
    world_bank_df = mortality_rate(world_bank_df)
    
    # first chart plots 
    
    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'Total_Greenhouse_gases',
        title = 'Total Greenhouse Gases (kt of CO2 equivalent)',
        color = 'country',
        labels = {
                "Total_Greenhouse_gases": "Greenhouse Gases"
            }
        )
    
    # second cahrt plots 


    graph_two = px.line(world_bank_df,
        x ='date',
        y = 'Total_mortality_under_5',
        title = 'Mortality Rates under 5(per 1000 births)',
        color = 'country',
        labels = {
                "Total_mortality_under_5": "Mortality under 5 (per 1000 births)"
            }
        )


    # third chart plots 


    graph_three = px.scatter(world_bank_df,
        x ='Rural',
        y = "Population_under_5_50_per_day",
        title = 'Poverty Rate under $5.50 a day in Rural Population',
        color = 'country',
        labels = {
                "Population_under_5_50_per_day": "Population under $5.50 per day"
            }
        )


    # fourth chart plots 




    graph_four= px.scatter(world_bank_df,
        x ='Population_under_5_50_per_day',
        y = "Total_mortality_under_5",
        title = 'Mortality vs Poverty',
        color = 'country',
        labels = {
                "Total_mortality_under_5": "Mortality Rate under 5 (per 1000 births)",
                "Population_under_5_50_per_day": "Population under $5.50 per day"
            }
        )



    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    figures.append(graph_three)
    figures.append(graph_four)

    return figures