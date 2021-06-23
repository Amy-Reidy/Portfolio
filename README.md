## Hi, I'm Amy. 

I'm an educator, humanitarian, global nomad, lifelong learner, goal-digger, Sudoku enthusiast and now a data scientist. 

I have an MA in Education and International Development, I'm trained in monitoring and evaluation, and I have worked in the non-profit and private sectors in 4 continents over the past 10 years. I am currently based in Germany where I'm studying an online masters in Data Science. 

I'm interested in the intersection of social impact and data science, and I want to use data to help non-profits and governments to analyze, visualize and solve social issues around the world. I'm particularly interested in working on challenges related to migration and displacement, gender equality, children's rights, and equity in public health and education.

This is just the beginning of my data science journey, and as I progress I am excited to add more projects to my portfolio which are more related to my interests and which utilize more machine learning techniques. Watch this space!

### Project 1: 
["Exploring Factors Related to Global Rates of COVID-19"](https://github.com/Amy-Reidy/Portfolio/blob/main/IntroProgProject%20-%20%20s00216954%20Amy%20REIDY/IntroProgProject%20-%20s00216954%20Amy%20REIDY.ipynb)
I created this project as my final assignment for the 'Introductory Python for Data Science' module of my master's program in May 2021.

There were two goals of the project:
1. Test the claim that female-led countries have lower rates of COVID-19.

2. Create a linear regression model to predict rates of COVID-19 in countries around the world.

The data for COVID-19 rates around the world was retrieved by sending an API request to 'https://api.covid19api.com/summary'. Data for population and global rates of smoking, obesity, and life expectancy was sourced from csv files on https://ourworldindata.org/. Information about which countries are part of the OECD was retrieved from [https://www.oecd.org/](https://www.oecd.org/newsroom/global-oecd-welcomes-colombia-as-its-37th-member.htm#:~:text=The%20OECD's%2037%20members%20are,Poland%2C%20Portugal%2C%20Slovak%20Republic%2C) to get a list of countries that have had a female leader for the COVID-19 outbreak, I used BeautifulSoup to web-scrape a table with female heads of state and government from [Wikipedia](https://en.wikipedia.org/wiki/List_of_elected_and_appointed_female_heads_of_state_and_government).

Libraries used: *pandas, numpy, sklearn, matplotlib, seaborn, requests, geopy, folium, wikipedia, yellowbrick*

### Project 2: 
![Beyond-Catastrophe](https://user-images.githubusercontent.com/73396449/123085318-6269a780-d422-11eb-85a9-babc7d78552b.jpg)





[“Exploring Toronto Neighborhoods to Identify a Suitable Location for a New Indian Restaurant”](https://github.com/Amy-Reidy/Portfolio/blob/main/IBM%20Capstone%20Project%20-%20Exploring%20Indian%20Restaurants%20in%20Toronto.ipynb)

This was my first ever data science project, which I did as a capstone project for [IBM's Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science?utm_source=gg&utm_medium=sem&campaignid=2087860785&utm_campaign=10-IBM-Data-Science-ROW&utm_content=10-IBM-Data-Science-ROW&adgroupid=116274867101&device=c&keyword=&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=506892807488&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9H3qhF5Sg8y6oWRoxM86ZqMkHP_gaTK_Y1x9O8FKXRNscBTeqVRav8aAttWEALw_wcB) in November 2020.

The aim of the project was to investigate where would be a suitable location for a new Indian restaurant in Toronto, based on the density of existing Indian restaurants and the number of Indian residents in each neighborhood.

Data was sourced by web-scraping Wikipedia, extracting information about various venues in Toronto and their geospatial information using Foursquare’s API, and obtaining geospatial for Toronto from “https://cocl.us/Geospatial_data”.

The K-means machine learning model was used to group the neighborhoods into clusters based on the density of Indian restaurants in each neighborhood.

Libraries used: *pandas, numpy, sklearn, matplotlib, seaborn, requests, geopy, folium, wikipedia, yellowbrick*


