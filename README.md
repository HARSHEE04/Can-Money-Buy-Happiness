The Price of Joy: Does Money Buy Happiness?

An end-to-end data analysis project investigating the link between wealth and happiness 

Created by Harsheta Sharma



##Project Description

This data analysis project was created to help answer a question I have often wondered about, does money buy happiness? Yet instead of looking at this question from an individual perspective, I decided to view it from a country’s perspective to see if a country’s GDP directly affects the happiness scores of its inhabitants.

This project was also created to experiment with different data extraction, manipulation and visualization techniques to put my knowledge of those concepts into useful practice.

The data set was obtained from Kaggle under the name World Happiness Report- 2024
World Happiness Report for 2024 & World Happiness Report from 2005-2024.  

The Logic.py file was used for the data extraction, manipulation and cleaning. The following technologies were present and used in that file.

The kaggle api was used to get direct access to this dataset into my VS code environment and kagglehub was used to obtain the kaggle data programmatically.and provide vital in being able handle frequent dataset updates if they occurred on the file in addition to providing a more scalable and streamlined workflow.

Pandas library was also used for data manipulation, cleaning as well as analysis. The pandas library was used to read the csv file which was created into the project file using the kaggle technologies. Data frames were used to represent and explore the data set. Dictionaries were also created to hold the relevant columns and the rename method present in pandas was used to rename the columns of the data to match the dictionary. Data was also manipulated such as the life_ladder column which was converted to a percent for a more presentable format. After the data extraction, cleaning and manipulation, the to_excel method was used to create an updated csv file which would be used for the visualization.

It is quite significant to understand the relevant columns to understand what the data and visualisations represent. The GDP column will represent the Log GDP per capita which is the natural logarithm of the country's GDP per capita, adjusted for purchasing power parity (PPP) to account for differences in the cost of living between countries. The Life_Ladder score which was altered to be represented as percentage represents the happiness score for each country, based on responses to the Cantril Ladder question that asks respondents to think of a ladder, with the best possible life for them being a 10, and the worst possible life being a 0.

Other columns have also been created and are present in the dataset but they were not included into the visualisations since I did not see them contributing to gaining an insight into the asked question. In the future, I plan on building onto this question and project to see how those other factors such as generosity or freedom contribute to the happiness score which is why they are still included in the revised dataset.


The app.py file holds the layout, interactivity and code for the figures present in the visualization. The visualisation was created using dash and plotly using the bootstrap framework for the layout

Plotly/plotly express was used to be able to add interactive charts to my pages such as the scatter plot, line graph and bubble chart. Dash was used as the main technology as it allows us to build a web app with interactive charting and graphing capabilities where the frontend and backend is handled using the tools dash provinces. Dash is built on  flask which is web framework for python. Dash helps create quite a comprehensive web application visualization with easy to use methods and tools. Dash is used as a way to create an interface to display the plotly visualizations 

From dash, dash_core_ components, html, callback, output and input was used. The dcc are the dash core components which are needed for any dash application has provides features like markdown, graph and location. The html was used to further help with the layout using html.Div. The callback, output and input were used as part of the interactivity and allows for easy navigation between different pages holding the different graphs.

Dash_bootstraph_components was used for the navigation bar as well as for creating the main layout using a container..

Three different visualizations were created as a part of this project, a scatter plot, a line graph and a bubble chart. The methods scatter, line and update_layout were used to create the respective visualisations.

A scatter plot was determined to be the best choice from the three of help answer this question since scatter plots are used to compare two variables and view the trend between them using a trend or regression line. The scatter plot created displayed a positive correlation between the life_ladder score and gdp indicating that the higher the GDP, the higher the happiness of the people in that country.

The line graph shows us the happiness score over time for each country but does not significantly contribute to answer the question unless we have additional external data about events which took place during certain time periods which may have effects on the happiness score.

The bubble chart was a good choice since it also plotted the life_ladder score against the GDP but I found it to be just another variation of the scatter plot thus not adding much value in this case to find a conclusion to the asked question.


To further build on this project in the future, I aim to look at the other factors present in this dataset such as freedom, generosity and social support to see how those facts are affected by the GDP and how that affects the overall happiness score. I strongly believe these factors play a crucial role in one’s sense of community and overall satisfaction/content thus I plan on incorporating these into different visualizations to further deepen this analysis.



##How to Install and Run the Project

To run this project, simply run the app.py and click on the URL provided in the output to access the dash app.




##Credits
Dataset used: https://www.kaggle.com/datasets/jainaru/world-happiness-report-2024-yearly-updated/data


Documentation Used: 
https://plotly.com/python/
https://dash-bootstrap-components.opensource.faculty.ai/
https://dash.plotly.com/


Tutorials Used for Help:
https://www.youtube.com/watch?v=hSPmj7mK6ng







