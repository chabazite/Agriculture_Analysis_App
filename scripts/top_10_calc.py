country_list = [ 'Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'British Virgin Islands', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Rep.', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt, Arab Rep.', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong SAR, China', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Rep.', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Dem. People's Rep.", 'Korea, Rep.', 'Kosovo', 'Kuwait', 'Kyrgyz Republic', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao SAR, China', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Fed. Sts.', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russian Federation', 'Rwanda', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovak Republic', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Sudan', 'Spain', 'Sri Lanka', 'St. Kitts and Nevis', 'St. Lucia', 'St. Martin (French part)', 'St. Vincent and the Grenadines', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkiye', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, RB', 'Vietnam', 'Virgin Islands (U.S.)', 'West Bank and Gaza', 'Yemen, Rep.', 'Zambia', 'Zimbabwe']




def top_10_population_2021(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df=df[df['country'].isin(country_list)]
    largest_10_population = df[df['date']==2021].nlargest(n=11,columns='population')

    largest_10_list = [country for country in largest_10_population['country']]

    return largest_10_list


def top_10_rural_population_2021(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df=df[df['country'].isin(country_list)]
    largest_10_rural = df[df['date']==2021].nlargest(n=10,columns='Rural')

    top_10_rural_pop_list = [country for country in largest_10_rural['country']]

    return top_10_rural_pop_list


def top_10_urban_population_2021(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df=df[df['country'].isin(country_list)]
    largest_10_urban = df[df['date']==2021].nlargest(n=10,columns='Urban')

    top_10_urban_pop_list = [country for country in largest_10_urban['country']]

    return top_10_urban_pop_list


def top_10_ag_land_2018(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    df=df[df['country'].isin(country_list)]
    largest_10_land = df[df['date']==2018].nlargest(n=10,columns='agriculture_sqkm')

    top_10_agland_list = [country for country in largest_10_land['country']]

    return top_10_agland_list


def top_10_pop_vs_other(df, world_bank_columns):
    top_10_df=df[df['country'].isin(country_list)]
    world_df = df[df['country'].isin(['World'])]

    top_10_df=top_10_df.groupby(by=['date']).sum().reset_index()
    top_10_df['Group'] = 'Top 10 Population'

    world_df['date']=world_df['date'].dt.year
    top_10_df['date'] = top_10_df['date'].dt.year

    world_df.set_index('date',inplace=True)
    top_10_df.set_index('date',inplace=True)
    top_10_df.insert(0,'country','Top_10')

    world_df.drop(columns={'country'},inplace=True)
    top_10_df.drop(columns={'country'},inplace=True)

    top_10_vs_other = pd.DataFrame()
    top_10_vs_other.columns = world_bank_columns
    
    for i in range(1960,2022):
        top_10_vs_other.loc[i]=world_df.loc[i] - top_10_df.loc[i]