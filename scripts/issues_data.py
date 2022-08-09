import requests
import pandas as pd
import numpy as np
import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation,  combine_dataframe, format_dataframe
from scripts.additional_features import create_land_features, create_econ_features

indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'SL.AGR.EMPL.MA.ZS', 
    'SL.AGR.EMPL.FE.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS', 'SH.DYN.MORT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.CO2E.KT', 'SI.POV.DDAY']

world_bank_columns = ['population', 'total_land_sqkm', 'forest_%','crop_%',
    'agricultural_%','arable_%','cereal_grain_hectare', 'rural_pop_%','urban_pop_%', 'male_employement_ag', 'female_employment_ag', 'fertilizer_consump','cereal_yield_kgPerHectare', 'total_gdp_ag_forestry_fishing', 'mortality_under5', 'Total_Greenhouse_gases', 'CO2_emmission','Poverty_under1_90_per_day']


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
    world_bank_df = create_land_features(world_bank_df)
    world_bank_df = create_econ_features(world_bank_df)
    world_bank_df = format_dataframe (world_bank_df, data_filter_choice)
    
    
    # first chart plots 
    
    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'Total_Greenhouse_gases',
        title = 'Total Greenhouse Gases (kt of CO2 equivalent)',
        color = 'country'
        )
    
    # second cahrt plots 


    graph_two= px.line(world_bank_df,
        x ='date',
        y = 'CO2_emmission',
        title = 'Total CO2_emmission ()',
        color = 'country'
        )


    # third chart plots 


    graph_three = px.line(world_bank_df,
        x ='date',
        y = "Poverty_under1_90_per_day",
        title = 'Poverty Rate under $1.90 a day',
        color = 'country'
        )


    # fourth chart plots 




    graph_four= px.line(world_bank_df,
        x ='date',
        y = "mortality_under5",
        title = 'Mortality under 5 years old',
        color = 'country'
        )



    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    figures.append(graph_three)
    figures.append(graph_four)

    return figures