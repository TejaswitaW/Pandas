import pandas as pd
#reading csv file which is in current working directory
df=pd.read_csv('weather_data.csv')
#print(df)
print("Maximum temerature is:",df['maximum temperature'].max())
print("Minimum temerature in maximum temerature range is:",df['maximum temperature'].min())
print("maximum temperature in minimum temperature range is: ",df['minimum temperature'].max())
print("Minimum temperature is: ",df['minimum temperature'].min())
print("Minimum temperature in minimum temperature range is: ",df['minimum temperature'].min())
print("Maximum temperature average is : ",df['maximum temperature'].mean())
print("Minimum temperature average is : ",df['minimum temperature'].mean())
