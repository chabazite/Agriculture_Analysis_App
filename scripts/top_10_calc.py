def top_10_population_2021(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    largest_10_population = df[df['date']=='2021'].nlargest(n=11,columns='population')

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
    largest_10_rural = df[df['date']=='2021'].nlargest(n=10,columns='total_rural_pop')

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

    largest_10_urban = df[df['date']=='2021'].nlargest(n=10,columns='total_urban_pop')

    top_10_urban_pop_list = [country for country in largest_10_urban['country']]

    return top_10_urban_pop_list


def top_10_ag_land_2021(df):
    """
    _summary_

    Args:
        df (_type_): _description_

    Returns:
        _type_: _description_
    """
    largest_10_land = df[df['date']=='2021'].nlargest(n=10,columns='total_ag_land')

    top_10_agland_list = [country for country in largest_10_land['country']]

    return top_10_agland_list


def top_10_pop_vs_other(top_10_df, world_df, world_bank_columns):
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