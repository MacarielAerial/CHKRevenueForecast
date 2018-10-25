# This script aims at converting monthly excel data into quarterly dataframe data
import pandas as pd
input_excel = '/Users/Chris/Desktop/CHK_Stock_Valuation/cpi/CPIAUCSL (1).xls'
header_number = 10
mean_or_sum = 'mean'
datetime_index = 'observation_date'
df = pd.read_excel(input_excel,sheet_name=0,header=header_number)
writer = pd.ExcelWriter('/Users/Chris/Desktop/CHK_Stock_Valuation/cpi/cpi.xls')

def main():
	# Set index of dataframe to a datetime object
	df.set_index(datetime_index,inplace=True)
	# Group by and sum up/average monthly data into quarterly data
	if mean_or_sum == 'mean':
		df_quarter = df.resample('Q').mean()
	elif mean_or_sum == 'sum':
		df_quarter = df.resample('q').sum()
	# Write quarterly data to the original excel workbook as another worksheet
	df_quarter.to_excel(writer,'quarter_result')
	writer.save()





if __name__ == "__main__":
	main()
