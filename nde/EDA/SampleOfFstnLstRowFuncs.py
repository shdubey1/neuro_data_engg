import plotly.express as px
import pandas as pd

class SampleOfFstnLstRowFuncs:
    def __init__(self,df):
        self.df = df
    
    def sampleOfFstnLstRow(self):
        fst_n_lst_rows = self.df.head(50) + self.df.tail(50)
        return fst_n_lst_rows.to_html()