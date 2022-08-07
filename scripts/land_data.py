import requests
import pandas as pd
import numpy as np
import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation, combine_dataframe, format_dataframe
from scripts.additional_features import create_land_features

indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']

world_bank_columns = ['population', 'total_land_sqkm', 'forest_%','crop_%','agricultural_%','arable_%','cereal_grain_hectare', 'rural_pop_%','urban_pop_%']


def return_land_figures(data_filter_choice):
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df = create_land_features(world_bank_df)
    world_bank_df = format_dataframe (world_bank_df, data_filter_choice)

    
    # first chart plots 
    
    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'forest_sqkm',
        title = 'Total Forest (sq km)',
        color = 'country'
        )
    
    # second cahrt plots 


    graph_two= px.line(world_bank_df,
        x ='date',
        y = 'agriculture_sqkm',
        title = 'Total Agricultural Land (sq km)',
        color = 'country'
        )


    # third chart plots 

    
    graph_three = px.line(world_bank_df,
        x ='date',
        y = "sq_km_agriculture_per_person",
        title = 'Agricultural Land per Person',
        color = 'country'
        )


    # fourth chart plots 

    

    graph_four= px.line(world_bank_df,
        x ='date',
        y = "cereal_grain_sqkm",
        title = 'Cereal Land (sqkm)',
        color = 'country'
        )


        

    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    figures.append(graph_three)
    figures.append(graph_four)

    return figures