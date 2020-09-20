
def outlier(series):
    import pandas as pd
    index_counter = 0
    describe_series = series.describe()
    q1 = describe_series['25%']
    q3 = describe_series['75%']
    iqr = q3-q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = []
    for (value) in series:        
        value = int(value)
        if value>upper_bound or value<lower_bound:
            outliers.append(index_counter)
        index_counter+=1
    return {'Mean': series.mean(),
            'Mode':series.mode(),
            'Lower Bound': lower_bound,
            'Upper Bound': upper_bound,
            'Median': describe_series['50%'],
            'IQR': iqr,
            'Potential Outliers': outliers}
