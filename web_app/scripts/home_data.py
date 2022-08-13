import pandas as pd
import numpy as np
import plotly.express as px
import requests

country_list = ['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Dem. People's Rep.", 'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']

def data_wrangle(df):

    df.drop(columns=['indicator','obs_status','decimal', 'unit'], inplace=True, axis=1)

    df["date"] = pd.to_datetime(df["date"]).dt.year
    df["date"] = pd.to_numeric(df["date"])
    
        #turn country feature into just country name
    for i, country in enumerate(df['country']):
        df.loc[i,'country'] = country['value']

    df = df[df['country'].isin(country_list)]
    
    
    return df


     
indicators = ['SP.POP.TOTL']


def return_index_figure():
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

        world_bank_columns = ['population']

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