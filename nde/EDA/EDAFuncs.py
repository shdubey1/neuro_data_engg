from plotly import graph_objects
from nde.EDA.CorrelationFuncs import CorrelationFuncs
from nde.EDA.GraphFuncs import GraphFuncs
from nde.EDA.MissingValuesFuncs import MissingValuesFuncs
from nde.EDA.MissingValuesPlottingFuncs import MissingValuesPlottingFuncs
from nde.EDA.SampleOfFstnLstRowFuncs import SampleOfFstnLstRowFuncs
from nde.models import MissingValues, SampleOfFirstNLastRows
import pandas as pd
from django.shortcuts import render


class EDAFuncs:
    def __init__(self, df,request):
        self.df = df
        self.request = request
        # self.missingValues(df)
    
    def missingValuesHtml(self):
        print('called')
        missing_values_object = MissingValuesFuncs(self.df)  
        columns = missing_values_object.columnList()
        missing_value_percentage = missing_values_object.missingValuesPercentage()
        missing_values = missing_values_object.missingValuesList()
        mean = missing_values_object.meanList()
        median = missing_values_object.medianList()
        mode = missing_values_object.modeList()
        memory_size = missing_values_object.memoryUsageList()
        params = {
                'columns': columns, 
                'missing_value_percentage' : missing_value_percentage, 
                'missing_values': missing_values, 
                'mean':mean, 
                'median' : median, 
                'mode': mode, 
                'memory_size' : memory_size
                }
        #print(self.df)
        return render(self.request,'nde/EDATabularView.html', params)
    

    def correlationHtml(self):
        correlation_object = CorrelationFuncs(self.df)
        corr_html = correlation_object.correlation()
        return corr_html

    def missingValuesPlottingHtml(self):
        missing_vals_plotting_obj = MissingValuesPlottingFuncs(self.df)
        missing_vals_plotting_html = missing_vals_plotting_obj.missingValuesPlotting()
        return missing_vals_plotting_html  

    def sampleOfFstnLstRowHtml(self):
        sample_of_fst_n_lst_row_obj = SampleOfFstnLstRowFuncs(self.df)
        sample_of_fst_n_lst_row_html = sample_of_fst_n_lst_row_obj.sampleOfFstnLstRow()
        return sample_of_fst_n_lst_row_html
    
    def graphHtml(self):
        graph_object = GraphFuncs(self.df)
        graph_html = graph_object.graph()
        return graph_html


       

  