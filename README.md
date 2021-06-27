## Hi, I'm Amy. 

![IMG_20210427_103513 (1)](https://user-images.githubusercontent.com/73396449/123549631-227c2a80-d76a-11eb-8cb7-7395ca88872e.jpg)


I'm an educator, humanitarian, global nomad, lifelong learner, goal-digger, Sudoku enthusiast and now an aspiring data scientist. 

I have an MA in Education and International Development, I'm trained in monitoring and evaluation, and I have worked in the non-profit and private sectors in 4 continents over the past 10 years. I am currently based in Germany where I'm studying an online master’s in data science. 

I'm interested in the intersection of social impact and data science, and I want to use data to help non-profits and governments to analyze, visualize and solve social issues around the world. I'm particularly interested in working on challenges related to migration and displacement, gender equality, children's rights, and equity in public health and education.

This is just the beginning of my data science journey, and as I progress, I am excited to add projects to my portfolio which are more related to my interests and which utilize more machine learning techniques. Watch this space!


### Project 1: ["Exploring Factors Related to Global Rates of COVID-19"](https://github.com/Amy-Reidy/Portfolio/blob/main/Exploring%20Factors%20Related%20to%20Global%20Rates%20of%20COVID-19/Exploring%20Factors%20Related%20to%20Global%20Rates%20of%20COVID-19..ipynb)

![Alarming gap in global response to COVID-19](https://user-images.githubusercontent.com/73396449/123540825-3bbcb100-d741-11eb-84f9-0d0b61a7fda3.jpg)

I created this project as my final assignment for the 'Introductory Programming for Data Science' module of my master's program in May 2021.

There were two goals of the project:
**1. Test the claim that female-led countries have lower rates of COVID-19.**
   I used the non-parametric Mann-Whitney U test to test the null hypothesis that the distributions of two samples are equal; first, I compared all countries in the sample and then just the OECD countries, as some critics say that this claim focuses too much on OECD countries.

**2. Create a linear regression model to predict rates of COVID-19 in countries around the world.**
   I created multiple linear regression models using TensorFlow and Scikit-learn and compared the results. Note: these are quite simple models, as the course’s main objective was to introduce Python programming and there was only a very brief introduction to machine learning.
   
The data for COVID-19 rates around the world was retrieved by sending an API request to 'https://api.covid19api.com/summary'. Data for population and global rates of smoking, obesity, and life expectancy was sourced from csv files on https://ourworldindata.org/. Information about which countries are part of the OECD was retrieved from [https://www.oecd.org/](https://www.oecd.org/newsroom/global-oecd-welcomes-colombia-as-its-37th-member.htm#:~:text=The%20OECD's%2037%20members%20are,Poland%2C%20Portugal%2C%20Slovak%20Republic%2C). And to get a list of countries that have had a female leader for the COVID-19 outbreak, I used BeautifulSoup to web-scrape a table with female heads of state and government from [Wikipedia](https://en.wikipedia.org/wiki/List_of_elected_and_appointed_female_heads_of_state_and_government).  

After the data was pre-processed, it was merged into a SQL database which was queried to extract information into dataframes 

Libraries used: *pandas, numpy, sklearn, tensorflow, sqlite3, scipy.stats,  matplotlib, seaborn, requests, BeautifulSoup, geopy, folium*



### Project 2: ["Has COVID-19 affected the world's happiness and wellbeing?"](https://github.com/Amy-Reidy/Portfolio-by-Amy-Reidy/blob/main/World%20Happiness%20and%20Wellbeing%20-%20Stats%20Project/World%20Happiness%20and%20Wellbeing%20Project.ipynb)
![Beyond-Catastrophe](https://user-images.githubusercontent.com/73396449/123085318-6269a780-d422-11eb-85a9-babc7d78552b.jpg)

This is another project that I completed for my master's program, this time for the 'Statistics and Applied Probability' module. I used data from the World Happiness Report 2021 to test the following hypotheses:
 1.	Global happiness scores decreased from 2019 to 2020. 
 2.	Positive emotions decreased globally from 2019 to 2020. 
 3.	Negative emotions increased globally from 2019 to 2020.

As the differences between the samples were not normally distributed and had significant outliers, I decided to use a non-parametric test (Wilcoxon signed-rank test), rather than the paired T-test which is usually used for comparing paired samples. 

Libraries used: *pandas, numpy, scipy, matplotlib, seaborn* 



### Project 3: [“Exploring Toronto Neighborhoods to Identify a Suitable Location for a New Indian Restaurant”](https://github.com/Amy-Reidy/Portfolio/blob/main/IBM%20Capstone%20Project%20-%20Exploring%20Indian%20Restaurants%20in%20Toronto.ipynb)

![shutterstock_573575497___Super_Portrait](https://user-images.githubusercontent.com/73396449/123547450-22c3f800-d761-11eb-9bd9-61e6df04b868.jpg)

This was my first ever data science project, which I did as a capstone project for [IBM's Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science?utm_source=gg&utm_medium=sem&campaignid=2087860785&utm_campaign=10-IBM-Data-Science-ROW&utm_content=10-IBM-Data-Science-ROW&adgroupid=116274867101&device=c&keyword=&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=506892807488&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9H3qhF5Sg8y6oWRoxM86ZqMkHP_gaTK_Y1x9O8FKXRNscBTeqVRav8aAttWEALw_wcB) in November 2020.

The aim of the project was to investigate where would be a suitable location for a new Indian restaurant in Toronto, based on the density of existing Indian restaurants and the number of Indian residents in each neighborhood.

Data was sourced by web-scraping Wikipedia, extracting information about various venues in Toronto and their geospatial information using Foursquare’s API, and obtaining geospatial for Toronto from “https://cocl.us/Geospatial_data”.

The K-means machine learning model was used to group the neighborhoods into clusters based on the density of Indian restaurants in each neighborhood.

Libraries used: *pandas, numpy, sklearn, matplotlib, seaborn, requests, geopy, folium, wikipedia, yellowbrick*

