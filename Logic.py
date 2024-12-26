
#Check to ensure the Kaggle API is succesfully imported
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

print("Kaggle API authenticated successfully!")

import pandas as pd
import kaggle 
import zipfile

#Api command to get the kaggle data programatically
import kagglehub


# Download latest version
path = kagglehub.dataset_download("jainaru/world-happiness-report-2024-yearly-updated")

print("Path to dataset files:", path) #check path to ensure it is there


#ensure that the zipfile is in the same folder as the project file
zipfile.__name__='WorldHappy.zip'
with zipfile.ZipFile(zipfile.__name__,'r') as file:
    file.extractall()


csv_file= "World-happiness-report-updated_2024.csv"

df= pd.read_csv(csv_file, encoding="ISO-8859-1") #has to use encoding because this file has non UTF- 8 chars and this is a more forgiving encoding
#encodings ensure that you are able to read the file properly

df.info() #use to explore the data

#check to see entire dataset
print(df)

#check to see column names
print(df.columns)

#check to see unique values in certain coulmns
print(df['Country name'].value_counts())
print(df['year'].value_counts())
print(df['Life Ladder'].value_counts())
print(df['Log GDP per capita'].value_counts())
print(df['Freedom to make life choices'].value_counts())
print(df['Generosity'].value_counts())
print(df['Social support'].value_counts())
print(df['Healthy life expectancy at birth'].value_counts())

#now that all columns work, we need to make a dictionary so we can change the names into what is relevent and easily used
new_cols_names={'Country name': 'country_name', 
                'year': 'year',
                'Life Ladder': 'life_ladder',
                'Log GDP per capita':'GDP',
                'Freedom to make life choices':'choice_freedom',
                'Generosity':'generosity',
                'Social support': 'social_support',
                'Healthy life expectancy at birth':'life_expectancy'}

#now rename the coulmns with these names
df.rename(new_cols_names,axis=1, inplace=True) #rename is pandas method to rename coulmns or index in data frame, acceptts dictionary
#the axis 1 specifies if we are renaming cols or rows, 1 means cols and 0 means rows, inplace means make changes directly to df w/o making new copy

#now change the relevent values so they can be properly reprenseted 
#make ladder score into percentage
df.life_ladder=(df.life_ladder/10)*100
print("After changes in life ladder in percent")
print(df.life_ladder)


df.to_excel('World Happiness_Final.xlsx', sheet_name='Data')

