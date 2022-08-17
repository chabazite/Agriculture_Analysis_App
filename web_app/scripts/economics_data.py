import plotly.express as px
from scripts.dataframe_compile import indicator_url_creation,  combine_dataframe, format_dataframe
from scripts.additional_features import create_econ_features

indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2','AG.LND.ARBL.ZS',
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS']

world_bank_columns = ['population', 'total_land_sqkm', 'arable_%', 'rural_pop_%','urban_pop_%', 'fertilizer_consump','cereal_yield_kgPerHectare', 'total_gdp_ag_forestry_fishing']



def return_econ_figures(data_filter_choice):
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """

    dataframe_list = indicator_url_creation(indicators)
    world_bank_df = combine_dataframe(dataframe_list, world_bank_columns)
    world_bank_df['arable_sqkm'] = world_bank_df['arable_%']*world_bank_df['total_land_sqkm'] / 100 
    world_bank_df.drop(labels=['arable_%'],axis=1,inplace=True)
    world_bank_df = format_dataframe(world_bank_df, data_filter_choice)
    world_bank_df = create_econ_features(world_bank_df)

    # first chart plots 
    graph_one = px.line(world_bank_df,
        x ='date',
        y = 'cereal_yield_kgPerHectare',
        title = 'Total Yield in Cereal Grain (kg per Hectare)',
        color = 'country',
         labels = {
                "cereal_yield_kgPerHectare": "Cereal Grain (kg per Hectare)"
            }
        )
    
    # second chart plots 
    graph_two= px.line(world_bank_df,
        x ='date',
        y = 'Total_fertilizer',
        title = 'Total Fertilizer Consumption (kg)',
        color = 'country',
         labels = {
                "Total_fertilizer": "Fertilizer (kg)"
            }
        )


    # third chart plots 
    graph_three = px.scatter(world_bank_df,
        x ='Total_fertilizer',
        y = "cereal_yield_kgPerHectare",
        title = 'Cereal Production vs Fertilizer Consumption',
        color = 'country',
         labels = {
                "cereal_yield_kgPerHectare": "Cereal Grain (kg per Hectare)",
                "Total_fertilizer": "Fertilizer (kg)"
            }
        )


    # fourth chart plots 
    graph_four= px.scatter_3d(world_bank_df,
        x ='Total_fertilizer',
        y = "cereal_yield_kgPerHectare",
        z='total_gdp_ag_forestry_fishing',
        title = 'Ag GDP vs. Fertilizer Consumption vs Cereal Yield',
        color = 'country',
         labels = {
                "Total_fertilizer": "Fertilizer (kg)",
                "cereal_yield_kgPerHectare": "Cereal (kg per Hectare)",
                "total_gdp_ag_forestry_fishing": "GDP"
            }
        )



    figures = []
    figures.append(graph_one)
    figures.append(graph_two)
    figures.append(graph_three)
    figures.append(graph_four)

    return figures