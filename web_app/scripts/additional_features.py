def create_land_features(world_bank_df):
    """
    _summary_

    Args:
        world_bank_df (_type_): _description_
    
    Return:
        (_type_): _description_
    """


        #transform land features into sqkm
    world_bank_df['crop_sqkm'] = world_bank_df['crop_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['agriculture_sqkm'] = world_bank_df['agricultural_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['arable_sqkm'] = world_bank_df['arable_%']*world_bank_df['total_land_sqkm'] / 100 
    world_bank_df['cereal_grain_sqkm'] = world_bank_df['cereal_grain_hectare']/100
    #drop converted columns
    world_bank_df.drop(labels=['crop_%','agricultural_%','arable_%','cereal_grain_hectare'],axis=1,inplace=True)

    return world_bank_df

def create_econ_features(world_bank_df):
    """
    _summary_

    Args:
        world_bank_df (_type_): _description_
    
    Return:
        (_type_): _description_
    """

    #transform features
    world_bank_df['Total_fertilizer'] = (world_bank_df['fertilizer_consump'] *world_bank_df['arable_sqkm']*100)

    return world_bank_df



def create_issue_features(world_bank_df):
    """
    _summary_
    Args:
        world_bank_df (_type_): _description_
    Return:
        (_type_): _description_
    """
    #transform features
    world_bank_df['Population_under_5_50_per_day'] = world_bank_df    ['%Poverty_under5_50_per_day'] * world_bank_df['population']
 
    world_bank_df['Total_mortality_under_5'] = world_bank_df    ['mortality_under5']/1000 * world_bank_df['population']
  

    return world_bank_df


def mortality_rate(world_bank_df):
    """
    _summary_
    Args:
        world_bank_df (_type_): _description_
    Return:
        (_type_): _description_
    """
    #transform features 
    world_bank_df['Total_mortality_under_5'] = world_bank_df['Total_mortality_under_5'] / world_bank_df['population'] * 1000

    world_bank_df['Poverty_Rate'] = world_bank_df['Population_under_5_50_per_day'] / world_bank_df['population']
  

    return world_bank_df