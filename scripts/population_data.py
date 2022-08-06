import requests
import pandas as pd
import numpy as np
import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation, combine_dataframe,format_dataframe
from scripts.additional_features import create_land_features
     
indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']

world_bank_columns = ['population', 'total_land_sqkm', 'forest_%','crop_%','agricultural_%','arable_%','cereal_grain_hectare', 'rural_pop_%','urban_pop_%']


def return_pop_figures(data_filter_list):
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
    world_bank_df = format_dataframe (world_bank_df, data_filter_list)


    # first chart plots the total population of the world from 1960 to current  available data
    

    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'population',
        title = 'Total Population',
        )
    
    # second cahrt plots the total urban vs rural population of the world from 1960  to current available data

    #reshape for combined plot
    df_rural_urban = world_bank_df.melt(id_vars = ['date'], value_vars=['Urban','Rural'],var_name = 'urban_rural', value_name = 'population_new')

    graph_two= px.line(df_rural_urban,
        x ='date',
        y = 'population_new',
        color = 'urban_rural',
        title = 'Rural vs. Urban Population Growth',
        labels = {
            "population_new": "population",
            "urban_rural": "Location"
        }
        )
    graph_two.update_layout(legend=dict(
        yanchor="top",
        y=0.99,
        xanchor="left",
        x=0.01
    ))
        

    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    # figures.append(graph_three)
    # figures.append(graph_four)

    return figures