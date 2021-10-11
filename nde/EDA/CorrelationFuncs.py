import plotly.express as px
import pandas as pd
import base64

class CorrelationFuncs:
    def __init__(self,df):
        self.df = df
    
    def correlation(self):
        fig = px.imshow(self.df.corr())
        corr_img = fig.to_image(format='png')
        return base64.encodebytes(corr_img)
        #return corr_img

