import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation, combine_dataframe,format_dataframe
     
indicators = ['SP.POP.TOTL','SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS']

world_bank_columns = ['population', 'rural_pop_%','urban_pop_%']


def return_pop_figures(data_filter_choice):
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """


    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df = format_dataframe (world_bank_df, data_filter_choice)




    # first chart plots the total population of the world from 1960 to current  available data
        
    if data_filter_choice == 'World':
        graph_one = px.line(world_bank_df,
        x ='date',
        y = 'population',
        title = 'Total Population Growth',
        color = 'country'
            )
        graph_one.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))
        # second cahrt plots the total urban vs rural population of the world from 1960  to current available data
        
        #reshape for combined plot
        df_rural_urban = world_bank_df.melt(id_vars = ['date'], value_vars=['Urban','Rural'],var_name = 'urban_rural', value_name = 'population_new')

        graph_two= px.line(df_rural_urban,
            x ='date',
            y = 'population_new',
            color = 'urban_rural',
            title = 'Rural vs. Urban Population Growth',
            labels = {
                "population_new": "population",
                "urban_rural": "Location"
            }
            )
        graph_two.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))
        

        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        
    elif data_filter_choice == "Top 10 Largest Population vs. Other":
        graph_one = px.line(world_bank_df,
        x ='date',
        y = 'population',
        title = 'Total Population Growth',
        color = 'country'
            )
        graph_one.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

                #reshape for combined plot
        df_rural_urban = world_bank_df.melt(id_vars = ['country','date'], value_vars=['Urban','Rural'],var_name = 'urban_rural', value_name = 'population_new')

        df_rural_urban = df_rural_urban[df_rural_urban['date']==2021]

        graph_two= px.bar(df_rural_urban,
            x ='country',
            y = 'population_new',
            color = 'urban_rural',
            title = '2021 Total Rural & Urban Population',
            labels = {
                "population_new": "population",
                "urban_rural": "Location"
            }
            )


        graph_three = px.line(world_bank_df,
        x ='date',
        y = 'Rural',
        title = 'Total Rural Population Growth',
        color = 'country',
        labels = {
                "Rural": "population"
            }
            )
        graph_three.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

        graph_four = px.line(world_bank_df,
        x ='date',
        y = 'Urban',
        title = 'Total Urban Population GRowth',
        color = 'country',
        labels = {
                "Urban": "population"
            }
            )
        graph_four.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        figures.append(graph_three)
        figures.append(graph_four)        
        
    else:
        graph_one = px.line(world_bank_df,
        x ='date',
        y = 'population',
        title = 'Total Population',
        color = 'country'
            )
        graph_one.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))

            #reshape for combined plot
        df_rural_urban = world_bank_df.melt(id_vars = ['country','date'], value_vars=['Urban','Rural'],var_name = 'urban_rural', value_name = 'population_new')

        df_rural_urban = df_rural_urban[df_rural_urban['date']==2021]

        graph_two= px.bar(df_rural_urban,
            x ='country',
            y = 'population_new',
            color = 'urban_rural',
            title = '2021 Totol Rural & Urban Population Growth',
            labels = {
                "population_new": "population",
                "urban_rural": "Location"
            }
            )


        graph_three = px.line(world_bank_df,
        x ='date',
        y = 'Rural',
        title = 'Total Rural Population',
        color = 'country',
        labels = {
                "Rural": "population"
            }
            )
        graph_three.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))
        

        graph_four = px.line(world_bank_df,
        x ='date',
        y = 'Urban',
        title = 'Total Urban Population',
        color = 'country',
        labels = {
                "Urban": "population"
            }
            )
        graph_four.update_layout(legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01
        ))



        figures = []
        figures.append(graph_one)
        figures.append(graph_two)
        figures.append(graph_three)
        figures.append(graph_four)

    return figures