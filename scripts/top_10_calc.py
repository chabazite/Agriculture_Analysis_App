import pandas as pd

country_list = [ 'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Dem. People's Rep.", 'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']




def top_10_population_2021(df):
    """
    a function that filters for the top 10 largest countries by population and returns a list of those countries

    Args:
        df (dataframe): the processed dataframe pulled from APIs

    Returns:
        dataframe: the finalized dataframe, filtered for countries that are top 10 in total population
    """
    df=df[df['country'].isin(country_list)]
    largest_10_population = df[df['date']==2021].nlargest(n=11,columns='population')

    largest_10_list = [country for country in largest_10_population['country']]

    world_bank_df = df[df['country'].isin(largest_10_list)]

    return world_bank_df


def top_10_rural_population_2021(df):
    """
    a function that filters for the top 10 largest countries by rural population and returns a list of those countries

    Args:
        df (dataframe): the processed dataframe pulled from APIs

    Returns:
        dataframe: the finalized dataframe, filtered for countries that are top 10 in rural population
    """
    df=df[df['country'].isin(country_list)]
    largest_10_rural = df[df['date']==2021].nlargest(n=10,columns='Rural')

    top_10_rural_pop_list = [country for country in largest_10_rural['country']]

    world_bank_df = df[df['country'].isin(top_10_rural_pop_list)]


    return world_bank_df


def top_10_urban_population_2021(df):
    """
    a function that filters for the top 10 largest countries by urban population and returns a list of those countries

    Args:
        df (dataframe): the processed dataframe pulled from APIs

    Returns:
        dataframe: the finalized dataframe, filtered for countries that are top 10 in urban population
    """
    df=df[df['country'].isin(country_list)]
    largest_10_urban = df[df['date']==2021].nlargest(n=10,columns='Urban')

    top_10_urban_pop_list = [country for country in largest_10_urban['country']]

    world_bank_df = df[df['country'].isin(top_10_urban_pop_list)]

    return world_bank_df


def top_10_ag_land_2018(df):
    """
    a function that filters for the top 10 largest countries by total agricultural land in sq. km and returns a list of those countries

    Args:
        df (dataframe): the processed dataframe pulled from APIs

    Returns:
        dataframe: the finalized dataframe, filtered for countries that are top 10 in total agricultural land in sq km
    """
    df=df[df['country'].isin(country_list)]
    largest_10_land = df[df['date']==2018].nlargest(n=10,columns='agriculture_sqkm')

    top_10_agland_list = [country for country in largest_10_land['country']]

    world_bank_df = df[df['country'].isin(top_10_agland_list)]

    return world_bank_df


def top_10_pop_vs_other(df):
    """
    this function splits the dataframe into a "world" and "countries" dataframes. Then groups the information in the top 10 by year, subtracts the top 10 information from world information to get the "other" information. This is all other countries in the world. Finally it concats the two group dataframes "Top 10" and "Other" into one. 

    Args:
        df (dataframe): the processed dataframe pulled from APIs

    Returns:
        dataframe: the finalized dataframe, transformed to have two groups: a Top 10 populations and an Other.
    """

    top_10_df = top_10_population_2021(df)

    world_df = df[df['country']=='World']

    top_10_df=top_10_df.groupby(by=['date']).sum().reset_index()

    world_df.set_index('date',inplace=True)
    top_10_df.set_index('date',inplace=True)

    world_df.drop(columns={'country'},inplace=True)

    #Create a new dataframe for top 10 populations vs. all other countries
    top_10_vs_other = pd.DataFrame(columns=top_10_df.columns)

    for i in range(1960,2022):
            top_10_vs_other.loc[i]=world_df.loc[i] - top_10_df.loc[i]

    top_10_df.insert(0,'country','Top_10')
    top_10_vs_other.insert(0,'country','Other')

    top_10_vs_other = pd.concat((top_10_vs_other,top_10_df))

    top_10_vs_other = top_10_vs_other.reset_index().rename(columns={'index': 'date'})

    return top_10_vs_other