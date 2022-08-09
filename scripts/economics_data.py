import requests
import pandas as pd
import numpy as np
import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation,  combine_dataframe, format_dataframe
from scripts.additional_features import create_land_features, create_econ_features

indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'SL.AGR.EMPL.MA.ZS', 
    'SL.AGR.EMPL.FE.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS']

world_bank_columns = ['population', 'total_land_sqkm', 'forest_%','crop_%','agricultural_%','arable_%','cereal_grain_hectare', 'rural_pop_%','urban_pop_%', 'male_employement_ag', 'female_employment_ag', 'fertilizer_consump','cereal_yield_kgPerHectare', 'total_gdp_ag_forestry_fishing']



def return_econ_figures(data_filter_choice):
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
    world_bank_df = format_dataframe(world_bank_df, data_filter_choice)

    world_bank_df = create_econ_features(world_bank_df)
    world_bank_df['sq_km_agriculture_per_person'] =world_bank_df['agriculture_sqkm']/world_bank_df['population']


    # first chart plots 
    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'cereal_yield_kgPerHectare',
        title = 'Total Yield Cereal Grain (per Hectare)',
        color = 'country'
        )
    
    # second chart plots 
    graph_two= px.line(world_bank_df,
        x ='date',
        y = 'Total_fertilizer',
        title = 'Total Fertilizer Consumption (kg)',
        color = 'country'
        )


    # third chart plots 
    graph_three = px.line(world_bank_df,
        x ='date',
        y = "cereal_yield_per_person",
        title = 'Cereal Production kg per Hectare per Person',
        color = 'country'
        )


    # fourth chart plots 
    graph_four= px.line(world_bank_df,
        x ='date',
        y = "Total_fertilizer_per_person",
        title = 'Fertilizer User (kg per person)',
        color = 'country'
        )



    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    figures.append(graph_three)
    figures.append(graph_four)

    return figures