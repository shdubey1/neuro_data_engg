import plotly.express as px
import pandas as pd
import json

class CorrelationFuncs:
    def __init__(self,df):
        self.df = df
    
    def correlation(self):
        fig = px.imshow(self.df.corr())
        corr_json = json.loads(fig.to_json())
        return corr_json
        #return corr_img

