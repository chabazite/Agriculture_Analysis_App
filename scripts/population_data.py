import requests
import pandas as pd
import numpy as np
import plotly.express as px

world_default = ['World']


def top_filter(filter):
    pass


def data_wrangle(df):

    df.drop(columns=['indicator','obs_status','decimal', 'unit'], inplace=True, axis=1)

    df["date"] = pd.to_datetime(df["date"]).dt.year
    df["date"] = pd.to_numeric(df["date"])
    
        #turn country feature into just country name
    for i, country in enumerate(df['country']):
        df.loc[i,'country'] = country['value']

    df = df[df['country'].isin(world_default)]
    
    
    return df


     
indicators = ['SP.POP.TOTL','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']


def return_pop_figures():
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    # loop to create a list of URLs from api indicators
    urls = []
    for indicator in indicators:
        url = 'http://api.worldbank.org/v2/countries/indicators/' + indicator 
        urls.append(url)
    dataframe_list = []

    # loop to get request each url and iterate through 18 pages of json data, then turn into a list of dataframes.

    for url in urls:
        data = []
        try:  
            for page in range(1,18):
                payload = {'format': 'json', 'per_page': '1000', 'date':'1960:2022', 'page':page}     
                r = requests.get(url, params=payload)
                data+=r.json()[1]

            dataframe_list.append(pd.DataFrame(data))

        except:
            print('could not load data', url)

        world_bank_columns = ['population','rural_pop_%','urban_pop_%',]

        world_bank_df = None

    #format and combine datframes into a single dataframe
    for i, df in enumerate(dataframe_list):
      df = data_wrangle(df)

    
      if world_bank_df is not None:
        world_bank_df.insert(loc=len(world_bank_df.columns),column=world_bank_columns[i], 
        value=df['value'])
      else:
        world_bank_df = pd.DataFrame(df)
        world_bank_df.rename(columns={'value' : world_bank_columns[i]}, inplace=True)
    
    world_bank_df['total_urban_pop'] = world_bank_df['urban_pop_%']*world_bank_df['population'] / 100

    world_bank_df['total_rural_pop'] = world_bank_df['rural_pop_%']*world_bank_df['population'] / 100

    # first chart plots the total population of the world from 1960 to current  available data
    

    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'population',
        title = 'Total Population',
        )
    
    # second cahrt plots the total urban vs rural population of the world from 1960  to current available data

    #reshape for combined plot
    df_rural_urban = world_bank_df.melt(id_vars = ['date'], value_vars=['total_urban_pop','total_rural_pop'],var_name = 'urban_rural', value_name = 'population')

    graph_two= px.line(df_rural_urban,
        x ='date',
        y = 'population',
        color = 'urban_rural'
        )
   
    

    # graph_three = []

    # graph_three.append(
    #             go.Scatter(
    #     x =world_bank_df['date'],
    #     y = world_bank_df['total_rural_pop'],
    #     mode = 'lines'
    #     )
    # )





    # graph_four = []

    # graph_four.append(
    #             go.Scatter(
    #     x =[0,1,2,3,4,5],
    #     y = [0, 2, 4, 6, 8, 10],
    #     mode = 'lines'
    #     )
    # )


    

    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    # figures.append(graph_three)
    # figures.append(graph_four)

    return figures