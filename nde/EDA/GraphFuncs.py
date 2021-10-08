import plotly.graph_objects as px
#import plotly.express as px
import pandas as pd
import numpy as np

class GraphFuncs:
    def __init__(self,df):
        self.df = df
    
    def graph(self):
        plot = px.Figure()
        plot.add_trace(px.Box(y=self.df, boxpoints="all"))
        graph_img = plot.to_image(format='png')
        return graph_img