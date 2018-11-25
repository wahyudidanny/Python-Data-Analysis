import pandas as pd


insurance = pd.read_csv('E:\Github Repository\Python-Data-Analysis\Data Munging\FL_insurance_sample.csv',index_col=0)

insurance.to_html('insurance.html')
