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

    #these function wrangle data from APIs
    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df = create_land_features(world_bank_df)
    world_bank_df = format_dataframe(world_bank_df, data_filter_choice)
  
    
    world_bank_df['sq_km_agriculture_per_person'] =world_bank_df['agriculture_sqkm']/world_bank_df['population']

    
    # first chart plots 
    if data_filter_choice == 'World':

        # first chart plots 
        graph_one = px.line(world_bank_df,
            x ='date',
            y = 'agriculture_sqkm',
            title = 'Total Agricultural Land (sq. km)',
            color = 'country',
            labels = {
                "agriculture_sqkm": "Land (sq. km)"
            }
            )

        # second chart plots 

        graph_two= px.scatter(world_bank_df, x="arable_sqkm", y="crop_sqkm",
	             size="population", color="date",
                     hover_name="country", log_x=False, size_max=60,
                     title = 'Arable vs. Crop Land (sq. km) in terms of Population',
                                 labels = {
                "crop_sqkm": "Crop Land (sq. km)",
                "arable_sqkm": "Arable Land (sq. km)"
            })


        # third chart plots 

        graph_three = px.line(world_bank_df,
            x ='date',
            y = "sq_km_agriculture_per_person",
            title = 'Agricultural Land per Person',
            color = 'country',
            labels = {
                "sq_km_agriculture_per_person": "Agricultural Land (sq. km) per person"
            }
            )


        # fourth chart plots 

        graph_four= px.line(world_bank_df,
            x ='date',
            y = "cereal_grain_sqkm",
            title = 'Cereal Land (sq. km)',
            color = 'country',
            labels = {
                "creal_grain_sqkm": "Cereal Crop Land (sq. km)"
            }
            )

        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        figures.append(graph_three)
        figures.append(graph_four)   
    
    elif data_filter_choice == "Top 10 Largest Population vs. Other":
        graph_one = px.line(world_bank_df,
            x ='date',
            y = 'agriculture_sqkm',
            title = 'Total Agricultural Land (sq. km)',
            color = 'country',
            labels = {
                "agriculture_sqkm": "Land (sq. km)"
            }
            )

        # second cahrt plots 

        graph_two= px.scatter(
           world_bank_df.query('date==2018'), x="arable_sqkm", y="crop_sqkm",
	             size="population", color="country",
                     hover_name="country", log_x=False, size_max=60,
                     title = '2018 Arable vs. Crop Land (sq. km) in terms of Population',
                     labels = {
                "crop_sqkm": "Crop Land (sq. km)",
                "arable_sqkm": "Arable Land (sq. km)"
            })


        # third chart plots 

        graph_three = px.line(world_bank_df,
            x ='date',
            y = "sq_km_agriculture_per_person",
            title = 'Agricultural Land per Person',
            color = 'country',
            labels = {
                "sq_km_agriculture_per_person": "Agricultural Land (sq. km) per person"
            }
            )


        # fourth chart plots 

        graph_four= px.line(world_bank_df,
            x ='date',
            y = "cereal_grain_sqkm",
            title = 'Cereal Land (sq. km)',
            color = 'country',
            labels = {
                "creal_grain_sqkm": "Cereal Crop Land (sq. km)"
            }
            )




        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        figures.append(graph_three)
        figures.append(graph_four)
    
    else:
        graph_one = px.line(world_bank_df,
            x ='date',
            y = 'agriculture_sqkm',
            title = 'Total Agricultural Land (sq. km)',
            color = 'country',
             labels = {
                "agriculture_sqkm": "Land (sq. km)"
            }
            )

        # second cahrt plots 

        graph_two= px.scatter(
           world_bank_df.query('date==2018'), x="arable_sqkm", y="crop_sqkm",
	             size="population", color="country",
                     hover_name="country", log_x=False, size_max=60,
                     title = 'Arable vs. Crop Land (sq. km) in terms of Population',
                     labels = {
                "crop_sqkm": "Crop Land (sq. km)",
                "arable_sqkm": "Arable Land (sq. km)"
            })


        # third chart plots 

        graph_three = px.line(world_bank_df,
            x ='date',
            y = "sq_km_agriculture_per_person",
            title = 'Agricultural Land per Person',
            color = 'country',
            labels = {
                "sq_km_agriculture_per_person": "Agricultural Land (sq. km) per person"
            }
            )


        # fourth chart plots 

        graph_four= px.line(world_bank_df,
            x ='date',
            y = "cereal_grain_sqkm",
            title = 'Cereal Land (sq. km)',
            color = 'country',
            labels = {
                "creal_grain_sqkm": "Cereal Crop Land (sq. km)"
            }
            )




        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        figures.append(graph_three)
        figures.append(graph_four)

    return figures