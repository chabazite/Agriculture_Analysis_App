def create_land_features(world_bank_df):
    """
    _summary_

    Args:
        world_bank_df (_type_): _description_
    
    Return:
        (_type_): _description_
    """


        #transform land features into sqkm
    world_bank_df['forest_sqkm'] = world_bank_df['forest_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['crop_sqkm'] = world_bank_df['crop_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['agriculture_sqkm'] = world_bank_df['agricultural_%']*world_bank_df['total_land_sqkm'] / 100
    world_bank_df['arable_sqkm'] = world_bank_df['arable_%']*world_bank_df['total_land_sqkm'] / 100 
    world_bank_df['cereal_grain_sqkm'] = world_bank_df['cereal_grain_hectare']/100
    #drop converted columns
    world_bank_df.drop(labels=['forest_%','crop_%','agricultural_%','arable_%','cereal_grain_hectare'],axis=1,inplace=True)

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
    world_bank_df['cereal_yield_per_person'] = world_bank_df['cereal_yield_kgPerHectare'] / world_bank_df['population']

    world_bank_df['Total_fertilizer_per_person'] = (world_bank_df['fertilizer_consump'] *world_bank_df['arable_sqkm']*100)/ world_bank_df['population']
    world_bank_df['Total_fertilizer'] = (world_bank_df['fertilizer_consump'] *world_bank_df['arable_sqkm']*100)

    return world_bank_df