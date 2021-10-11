import plotly.express as px
import pandas as pd
import base64

class MissingValuesPlottingFuncs:
    def __init__(self,df):
        self.df = df
    
    def missingvaluesPlotting(self):
        fig = px.imshow(self.df)
        missing_vals_plotting_img = fig.to_image(format='png')
        return base64.encodebytes(missing_vals_plotting_img)

