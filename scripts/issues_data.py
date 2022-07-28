import pandas as pd
import numpy as np
import plotly.graph_objs as go

world_default = ['World']


def top_filter(filter):
    pass


def data_wrangle(question):

    indicators = ['SP.POP.TOTL', 'AG.LND.TOTL.K2', 'AG.LND.FRST.ZS',
    'AG.LND.CROP.ZS','AG.LND.AGRI.ZS','AG.LND.ARBL.ZS','AG.LND.CREL.HA', 
    'SP.RUR.TOTL.ZS','SP.URB.TOTL.IN.ZS', 'SL.AGR.EMPL.MA.ZS', 
    'SL.AGR.EMPL.FE.ZS', 'AG.CON.FERT.ZS','AG.YLD.CREL.KG', 'NV.AGR.TOTL.ZS',
    'SH.DYN.MORT', 'EN.ATM.GHGT.KT.CE', 'EN.ATM.CO2E.KT', 'SI.POV.DDAY']



    pass 





def return_issues_figures():
    """
    creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations
    """
    # first chart plots the total population of the world from 1960 to current  available data
    
    graph_one = []

    graph_one.append(
        go.Scatter(
        x =[0,1,2,3,4,5],
        y = [0, 2, 4, 6, 8, 10],
        mode = 'lines'
        )
    )

    layout_one = dict(title = 'Chart One', 
                    xaxis = dict(title = 'x-axis label'),
                    yaxis = dict(title = 'y-axis label'),
                    )
    
    # second cahrt plots the total urban population of the world from 1960  to current available data
    
    graph_two = []

    graph_two.append(
                go.Scatter(
        x =[0,1,2,3,4,5],
        y = [0, 2, 4, 6, 8, 10],
        mode = 'lines'
        )
    )

    layout_two = dict(title='Chart Two',
                    xaxis = dict(title = 'x-axis label',),
                    yaxis = dict(title = 'y-axis label',),
                    )
    
    # third cahrt plots the total rural population of the world from 1960  to current available data

    graph_three = []

    graph_three.append(
                go.Scatter(
        x =[0,1,2,3,4,5],
        y = [0, 2, 4, 6, 8, 10],
        mode = 'lines'
        )
    )

    layout_three = dict(title='Chart three',
                    xaxis = dict(title = 'x-axis label',),
                    yaxis = dict(title = 'y-axis label',),
                    )

    # fourth cahrt plots a global heat map with countries population over time from 1960  to current available data

    graph_four = []

    graph_four.append(
                go.Scatter(
        x =[0,1,2,3,4,5],
        y = [0, 2, 4, 6, 8, 10],
        mode = 'lines'
        )
    )

    layout_four = dict(title='Chart four',
                    xaxis = dict(title = 'x-axis label',),
                    yaxis = dict(title = 'y-axis label',),
                    )
    

    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures