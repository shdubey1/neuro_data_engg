import plotly.express as px
import pandas as pd
import json

class MissingValuesPlottingFuncs:
    def __init__(self,df):
        self.df = df
    
    def missingValuesPlotting(self):
        fig = px.imshow(self.df)
        missing_vals_plotting_json = json.loads(fig.to_json())
        return missing_vals_plotting_json

