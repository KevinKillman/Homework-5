import pandas as pd
def outlier(describe_series, dataframe):
    q1 = describe_series['25%']
    q3 = describe_series['75%']
    iqr = q3-q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    outliers = []
    for (value) in dataframe:
        value = int(value)
        if value>upper_bound or value<lower_bound:
            outliers.append(value)
    return {'Lower Bound': lower_bound,
            'Upper Bound': upper_bound,
            'Median': describe_series['50%'],
            'IQR': iqr,
            'Potential Outliers': outliers}
