import time
import requests
import pandas as pd
import aiohttp
import asyncio


indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'SL.AGR.EMPL.MA.ZS', 
    'SL.AGR.EMPL.FE.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS', 'SH.DYN.MORT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.CO2E.KT', 'SI.POV.DDAY']

start_time = time.time()

async def main():
    async with aiohttp.ClientSession as session:
        tasks = []
        for indicator in indicators:
            task = asyncio.ensure_future(get_indicator_data(session, indicator))
            tasks.append(task) 

        dataframe_list = await asyncio.gather(*tasks)

async def get_indicator_data(session, indicator):
    url = 'http://api.worldbank.org/v2/countries/indicators/' + indicator 

    data = []
    for page in range(1,18):
        payload = {'format': 'json', 'per_page': '1000', 'date':'1960:2022', 'page':page} 

        async with session.get(url, params=payload) as response:    
            results_data = await response.json()
            data+=results_data.json()[1]

    return pd.DataFrame(data)



asyncio.run(main())

print("--- %s seconds ---" % (time.time() - start_time))