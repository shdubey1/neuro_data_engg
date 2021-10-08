class MissingValuesFuncs:

    def __init__(self, df):
        self.df = df

    def columnList(self):
        column_list = ['column']
        for i in self.df.columns:
            column_list.append(i)
        return column_list    
    
    def missingValuesList(self):
        missing_values = self.df.isnull().sum()
        missing_values_list=['missing values']
        for i in missing_values:
            missing_values_list.append(i)
        return missing_values_list
    
    def missingValuesPercentage(self):
        total_missing_cells = self.df.isna().mean().round(4) * 100
        missing_values_percentage = total_missing_cells/len(self.df)*100
        percentage_row_list = ['missing values percentage']
        for i in missing_values_percentage:
            percentage_row_list.append(i)
        return percentage_row_list

    def meanList(self):
        mean_list = ['mean']
        for i in self.df.mean():
            mean_list.append(i)
        return mean_list

    def medianList(self):
        median_list = ['median']
        for i in self.df.median():
            median_list.append(i)
        return median_list

    def modeList(self):
        mode_list = ['mode']
        return mode_list
    
    def memoryUsageList(self):
        memory_usage_list = ['memory usage']
        for i in self.df.memory_usage():
            memory_usage_list.append(i)
        return memory_usage_list