import pandas as pd
import aiohttp
import asyncio
from scripts.top_10_calc import top_10_population_2021, top_10_rural_population_2021, top_10_urban_population_2021, top_10_ag_land_2018,top_10_pop_vs_other


def data_filter(df, data_filter_choice):
    """
    a function that chooses which filter function to use based on the filter drop down choice submitted by the user. It then returns the dataframe filtered based on that choice.

    Args:
        df (datframe): current dataframe to be filtered
        data_filter_choice (list): the choice of dropdown filter

    Returns:
        dataframe: the dataframe filtered based on the filter choice and function that filters the dataframe.
    """

    if data_filter_choice == 'World':
        df = df[df['country'].isin(['World'])]
    elif data_filter_choice == 'Top 10 Largest Population':
        df = top_10_population_2021(df)
    elif data_filter_choice ==  'Top 10 Largest Urban Population':
        df = top_10_urban_population_2021(df)
    elif data_filter_choice ==   'Top 10 Largest Rural Population':
        df = top_10_rural_population_2021(df)
    elif data_filter_choice ==   'Top 10 Largest Agricultural Land (sq. km)':
        df = top_10_ag_land_2018(df)
    else:
        df = top_10_pop_vs_other(df)

    return df




def data_wrangle(df):
    """
    passes a compiled dataframe from the APIs and cleans it up based on unecessary features and date column. Also removed the country dictionary feature for just a country name.

    Args:
        df (dataframe): the dataframe to be cleaned

    Returns:
        dataframe: the input dataframe, now cleaned up
    """


    df.drop(columns=['countryiso3code','indicator','obs_status','decimal', 'unit'], inplace=True, axis=1)

    df["date"] = pd.to_datetime(df["date"]).dt.year
    df["date"] = pd.to_numeric(df["date"])
    
        #turn country feature into just country name
    for i, country in enumerate(df['country']):
        df.loc[i,'country'] = country['value']

    
    return df





def indicator_url_creation(indicators):
    """
    creates the urls for each API by using a list of indicators that get added onto the end of the URL. The URLs then get requested and the json information is transformed into a pandas DF and put into list for further use.

    Args:
        indicators (list): a list of the API indicicators to be used for each URL

    Returns:
        list: a list of all the dataframes ingested from the API, appended into a list 
    """
    async def main():
        async with aiohttp.ClientSession() as session:
            tasks = []
            for indicator in indicators:
                task = asyncio.ensure_future(get_indicator_data(session, indicator))
                tasks.append(task) 

            dataframe_list = await asyncio.gather(*tasks)
        
        return dataframe_list

    async def get_indicator_data(session, indicator):
        url = 'http://api.worldbank.org/v2/countries/indicators/' + indicator 

        data = []
        for page in range(1,18):
            payload = {'format': 'json', 'per_page': '1000', 'date':'1960:2022', 'page':page} 

            async with session.get(url, params=payload) as response:    
                results_data = await response.json()
                data+=results_data[1]

        return pd.DataFrame(data)

    dataframe_list = asyncio.run(main())
    
    return dataframe_list


def combine_dataframe(dataframe_list, world_bank_columns):
    """
    this function takes the list of dataframes created by the indicator_url_creation function and combines them into a single dataframe.

    Args:
        dataframe_list (list): the list of dataframes created by the indicator_url_creation function.
        world_bank_columns (list): the column names used to create the dataframe

    Returns:
        dataframe: a combined dataframe from the list of dataframes gathered through API requests.
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

def format_dataframe(world_bank_df, data_filter_choice):
    """
    a function that creates new columns, drops unecessary ones, and filters the data based on user input.

    Args:
        world_bank_df (dataframe): _description_
        data_filter_choice (string): the string that the form returns from the user's filter input submission.

    Returns:
        datframe: finalized dataframe to be used for graph creation
    """

    world_bank_df['Urban'] = world_bank_df['urban_pop_%']*world_bank_df['population'] / 100

    world_bank_df['Rural'] = world_bank_df['rural_pop_%']*world_bank_df['population'] / 100

    world_bank_df.drop(labels=['urban_pop_%','rural_pop_%'],axis=1,inplace=True)

    world_bank_df = data_filter(world_bank_df, data_filter_choice)

    return world_bank_df