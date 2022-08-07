import requests
import pandas as pd
from scripts.top_10_calc import top_10_population_2021, top_10_rural_population_2021, top_10_urban_population_2021, top_10_ag_land_2018,top_10_pop_vs_other


def data_filter(df, data_filter_choice):
    """
    a function that chooses which filter function to use based on the filter drop down choice submitted by the user. It then returns the list of countries based on that choices.

    Args:
        df (datframe): current dataframe to be filtered
        data_filter_choice (list): the choice of dropdown filter

    Returns:
        a list of countries based on the filter choice and function that filters the dataframe.
    """

    data_filter_list = []
    if data_filter_choice == 'World':
        data_filter_list = ['World']
    elif data_filter_choice == 'Top 10 Highest Population':
        data_filter_list = top_10_population_2021(df)
    elif data_filter_choice ==  'Top 10 Highest Urban Population':
        data_filter_list = top_10_urban_population_2021(df)
    elif data_filter_choice ==   'Top 10 Highest Rural Population':
        data_filter_list = top_10_rural_population_2021(df)
    elif data_filter_choice ==   'Top 10 largest agricultural land (sq. km)':
        data_filter_list = top_10_ag_land_2018(df)
    # else:
    #     data_filter_choice = top_10_pop_vs_other(df, world_bank_columns)

    return data_filter_list




def data_wrangle(df):
    """
    _summary_

    Args:
        df (_type_): _description_
        data_filter_list (_type_): _description_

    Returns:
        _type_: _description_
    """


    df.drop(columns=['indicator','obs_status','decimal', 'unit'], inplace=True, axis=1)

    df["date"] = pd.to_datetime(df["date"]).dt.year
    df["date"] = pd.to_numeric(df["date"])
    
        #turn country feature into just country name
    for i, country in enumerate(df['country']):
        df.loc[i,'country'] = country['value']

    
    return df



def indicator_url_creation(indicators):
    """
    _summary_

    Args:
        indicators (_type_): _description_
    """
     # loop to create a list of URLs from api indicators
    urls = []
    for indicator in indicators:
        url = 'http://api.worldbank.org/v2/countries/indicators/' + indicator 
        urls.append(url)

    # loop to get request each url and iterate through 18 pages of json data, then turn into a list of dataframes.

    dataframe_list = []

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
    
    return dataframe_list


def combine_dataframe(dataframe_list, world_bank_columns):
    """
    _summary_

    Args:
        dataframe_list (_type_): _description_
        world_bank_columns (_type_): _description_

    Returns:
        _type_: _description_
    """
    
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
    

    return world_bank_df

def format_dataframe(world_bank_df, data_filter_list):
    """
    _summary_

    Args:
        world_bank_df (_type_): _description_
        data_filter_list (_type_): _description_

    Returns:
        _type_: _description_
    """

    world_bank_df['Urban'] = world_bank_df['urban_pop_%']*world_bank_df['population'] / 100

    world_bank_df['Rural'] = world_bank_df['rural_pop_%']*world_bank_df['population'] / 100

    world_bank_df.drop(labels=['urban_pop_%','rural_pop_%'],axis=1,inplace=True)

    data_filter_choice = data_filter(world_bank_df, data_filter_list)

    world_bank_df = world_bank_df[world_bank_df['country'].isin(data_filter_choice)]

    return world_bank_df