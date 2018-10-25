# This script is used to run multiple linear regression on data extracted from a excel file
# The script also exports plotted fitted data vs. actual data after regression
import pandas as pd
import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
import matplotlib.pyplot as plt
df = pd.read_excel('/Users/Chris/Desktop/CHK_Stock_Valuation/CHK_master.xlsx')

def main():
	# Assign date to a series
	date = df['date_quarter']
	# Create dataframe for y
	df_depend = df['revenue_log']
	# Create dataframe for all x
	df_independ = df[['us_10year_treasury','us_industrial','opec_log','gdp_log','p_gas_log','p_oil_log']]
	# Execute regression
	reg = LinearRegression().fit(df_independ,df_depend)
	# Output coefficients, intercepts, R squared and predicted values
	print(reg.score(df_independ,df_depend))
	print(reg.coef_)
	print(reg.intercept_)
	prediction = reg.predict(df_independ)
	# Plot predicted values vs. actual values



if __name__ == '__main__':
	main()
