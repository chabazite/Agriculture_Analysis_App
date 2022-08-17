import pandas as pd
import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation, combine_dataframe,format_dataframe

indicators = ['SP.POP.TOTL','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']

world_bank_columns = ['population', 'rural_pop_%','urban_pop_%']

  
def return_index_figure():
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """
    
    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df = format_dataframe (world_bank_df)


    # sort date for animation frames
    world_bank_df["date"] = pd.to_numeric(world_bank_df["date"])
    world_bank_df.sort_values(by=['date'],inplace=True) 

    # first chart plots the total population of the world from 1960 to current  available data

    graph_one = px.choropleth(world_bank_df,
            locations = 'countryiso3code',
            color = 'population',
            hover_name = 'country',
            animation_frame='date',    
            color_continuous_scale='Plasma',
            range_color=(0,400000000),
            projection = 'equirectangular',
            height=600   
        )

    return graph_one