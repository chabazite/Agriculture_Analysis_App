def create_land_features(world_bank_df):
    """
    function to create addition features specific to land_use. Will drop columns that are now useless based on the updated features (% columns)

    Args:
        world_bank_df (dataframe): input dataframe from APIs
    
    Return:
        (dataframe): a dataframe with new land-use features
    """


        #transform land features into sqkm
    world_bank_df['crop_sqkm'] = world_bank_df['crop_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['agriculture_sqkm'] = world_bank_df['agricultural_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['arable_sqkm'] = world_bank_df['arable_%']*world_bank_df['total_land_sqkm'] / 100 
    world_bank_df['cereal_grain_sqkm'] = world_bank_df['cereal_grain_hectare']/100
    #drop converted columns
    world_bank_df.drop(labels=['crop_%','agricultural_%','arable_%','cereal_grain_hectare'],axis=1,inplace=True)

    return world_bank_df


def seperate_econ_features(world_bank_df):
    """
    function that creates one new feature for the economic page

    Args:
        world_bank_df (dataframe): input dataframe from APIs
    
    Return:
        (dataframe): a dataframe with new economic features
    """
    world_bank_df['total_gdp_ag_forestry_fishing'] = (world_bank_df['total_gdp_ag_forestry_fishing'] *world_bank_df['GDP'])

    world_bank_df['fertilizer_consump'] = (world_bank_df['fertilizer_consump'] *world_bank_df['arable_sqkm'])

    world_bank_df['cereal_yield_kgPerHectare'] = (world_bank_df['cereal_yield_kgPerHectare'] * world_bank_df['cereal_grain_hectare'])

    return world_bank_df

    

def create_econ_features(world_bank_df):
    """
    function that creates one new feature for the economic page

    Args:
        world_bank_df (dataframe): input dataframe from APIs
    
    Return:
        (dataframe): a dataframe with new economic features
    """
    world_bank_df['total_gdp_ag_forestry_fishing'] = (world_bank_df['total_gdp_ag_forestry_fishing'] / world_bank_df['GDP'])

    world_bank_df['fertilizer_consump'] = (world_bank_df['fertilizer_consump'] /world_bank_df['arable_sqkm'])

    world_bank_df['cereal_yield_kgPerHectare'] = (world_bank_df['cereal_yield_kgPerHectare'] / world_bank_df['cereal_grain_hectare'])


    #transform features
    world_bank_df['Total_fertilizer'] = (world_bank_df['fertilizer_consump'] *world_bank_df['arable_sqkm']*100)

    return world_bank_df



def create_issue_features(world_bank_df):
    """
    function that prepares the poverty and mortality rates for the combination of data in the top10vsother dataframe. by turning them into pure counts based on population
    Args:
        world_bank_df (dataframe): input dataframe from APIs
    Return:
        (dataframe): a dataframe with new features for global issues
    """
    #transform features
    world_bank_df['Population_under_5_50_per_day'] = world_bank_df    ['%Poverty_under5_50_per_day'] * world_bank_df['population']
 
    world_bank_df['Total_mortality_under_5'] = world_bank_df    ['mortality_under5']/1000 * world_bank_df['population']
  

    return world_bank_df


def mortality_rate(world_bank_df):
    """
    function that recreates the mortality rate and poverty rate after the creation of the Top10vsother dataframe.
    Args:
        world_bank_df (dataframe): input dataframe from APIs
    Return:
        (dataframe): a dataframe that returns new features for poverty and mortality
    """
    #transform features 
    world_bank_df['Total_mortality_under_5'] = world_bank_df['Total_mortality_under_5'] / world_bank_df['population'] * 1000

    world_bank_df['Poverty_Rate'] = world_bank_df['Population_under_5_50_per_day'] / world_bank_df['population']
  

    return world_bank_df