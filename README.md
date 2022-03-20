## Hi, I'm Amy. 

![IMG_20210427_103513 (1)](https://user-images.githubusercontent.com/73396449/123549631-227c2a80-d76a-11eb-8cb7-7395ca88872e.jpg)


I'm an educator, humanitarian, global nomad, lifelong learner, goal-digger, Sudoku enthusiast and now an aspiring data scientist. 

I have an MA in Education and International Development, I'm trained in monitoring and evaluation, and I have worked in the non-profit and private sectors in 4 continents over the past 10 years. I am currently based in Germany where I'm studying an online master’s in data science. 

I'm interested in the intersection of social impact and data science, and I want to use data to help non-profits and governments to analyze, visualize and solve social issues around the world. I'm particularly interested in working on challenges related to migration and displacement, gender equality, children's rights, and equity in public health and education.

This is just the beginning of my data science journey, and as I progress, I am excited to add projects to my portfolio which are more related to my interests. Watch this space!

### Project 1: [Transfer Learning with VGG16 Convolutional Neural Network to Classify Traffic Signs](https://github.com/Amy-Reidy/Portfolio/blob/main/Traffic%20Sign%20Classifier%20with%20Transfer%20Learning%20Project/Poster%20for%20Transfer%20Learning%20Project.pdf)

![image](https://user-images.githubusercontent.com/73396449/157452389-8f33cf8d-4cfe-48ec-9b7b-8495d570ddb4.png)

As vehicles become more autonomous, there is an increasing demand in the automobile industry for driver assistance systems that can identify and classify road signs quickly and accurately. The aim of this project was to create a classifier, using a pre-trained convolutional neural network, that can effectively classify images from the German Traffic Sign Recognition Benchmark dataset. 

The convolutional base of the popular VGG16 model was used for feature extraction while the top fully connected layers were retrained with the GTSRB dataset and the hyperparameters were fine-tuned to further improve the model. The results show that the best-performing model in this experiment achieved an accuracy of 82.98%. As the dataset is quite imbalanced, future work could improve on this result by augmenting the images in the smaller classes to create a more balanced dataset.

The architecture of the best-performing model is shown below.

<p align="center">
<img src="https://user-images.githubusercontent.com/73396449/157449841-3084082f-89e6-44d5-b87b-a9fa85a32a8a.png" height="400"">
</p>
                                                                                                                              
Skills demonstrated: *Google Colab, TensorFlow, Keras, Transfer Learning, Convolutional Neural Network, Machine Learning*

### Project 2: [Dashboard of Global Disparities in Cervical Cancer Rates](https://github.com/Amy-Reidy/Portfolio/blob/main/Global%20Disparities%20in%20Cervical%20Cancer%20Rates/Notebook%20-%20'Global%20Disparities%20in%20Cervical%20Cancer'%20Project.ipynb)

### Project 3: [Latent Semantic Analysis: Applied Linear Algebra in Natural Language Understanding](https://github.com/Amy-Reidy/Portfolio/blob/main/Latent%20Semantic%20Analysis%20Project/Linear%20Algebra%20Project%20Code%20-%20LSA.ipynb)                                                                                                                          

![image](https://user-images.githubusercontent.com/73396449/159176567-92ee61b6-9233-4385-b957-ad8e0cfe9a87.png)

                 
The aim of this project was to describe how linear algebra can be applied to topic modelling in Natural Language Understanding (NLU). NLU is a subfield of Natural Language Processing (NLP), and the goal of NLU is to use computer algorithms to not just process text data, but to make sense of natural language data as it is spoken and written like a human would. NLU has many diverse real-world applications, including voice-controlled assistants like Apple’s Siri, customer service chatbots, and machine translators. NLU is an important subset of machine learning as it allows us to analyse and gain understanding from large bodies of unstructured data.

Topic modelling is a NLU text-mining technique for extracting topics from text, and it can be used for information retrieval, categorizing documents and exploratory analysis of text datasets. It assumes that documents contain different topics, and these topics are made up of a collection of words. A foundational method of topic modelling is Latent Semantic Analysis (LSA) which is an unsupervised machine learning technique that was introduced by Deerwester et al. (1990) as a way of analysing a text corpus (a large collection of texts) to discover the hidden or latent topics in it. This method differs from traditional NLP as it uses statistical techniques and linear algebra to analyse text, rather than relying on any specification of rules or dictionaries, and it is based on the principle of distributional hypothesis - words that have similar meanings occur in analogous segments of text.

There are two main steps in conducting LSA:

- Construction of a term-document matrix.
- Dimensionality reduction of this matrix using Singular Value Decomposition (SVD). This process produces a topic-document matrix and a topic-term matrix.

To illustrate each of the steps involved in using LSA to uncover themes across documents, titles and abstracts from ten recent research papers were analyzed in this project. The papers are all related to ‘anticipatory action’ (an emerging approach to disaster risk reduction), and they were chosen by selecting the first ten results from searching for the keywords “anticipatory action” on Google Scholar and filtering the results for only papers published in 2021.

Skills demonstrated: *Natural Language Processing (NLP), Natural Language Toolkit (NLTK), Text-Mining, Latent Semantic Analysis*

### Project 4: [Exploring Factors Related to Global Rates of COVID-19](https://github.com/Amy-Reidy/Portfolio/blob/main/Exploring%20Factors%20Related%20to%20Global%20Rates%20of%20COVID-19/Exploring%20Factors%20Related%20to%20Global%20Rates%20of%20COVID-19..ipynb)

![Alarming gap in global response to COVID-19](https://user-images.githubusercontent.com/73396449/123540825-3bbcb100-d741-11eb-84f9-0d0b61a7fda3.jpg)

I created this project as my final assignment for the 'Introductory Programming for Data Science' module of my master's program in May 2021.

There were two goals of the project:\
**1. Test the claim that female-led countries have lower rates of COVID-19.**\
   I used the non-parametric Mann-Whitney U test to test the null hypothesis that the distributions of two samples are equal; first, I compared all countries in the sample and then just the OECD countries, as some critics say that this claim focuses too much on OECD countries.

**2. Create a linear regression model to predict rates of COVID-19 in countries around the world.**\
   I created multiple linear regression models using TensorFlow and Scikit-learn and compared the results. Note: these are quite simple models, as the course’s main objective was to introduce Python programming and there was only a very brief introduction to machine learning.
   
The data for COVID-19 rates around the world was retrieved by sending an API request to 'https://api.covid19api.com/summary'. Data for population and global rates of smoking, obesity, and life expectancy was sourced from csv files on https://ourworldindata.org/. Information about which countries are part of the OECD was retrieved from [https://www.oecd.org/](https://www.oecd.org/newsroom/global-oecd-welcomes-colombia-as-its-37th-member.htm#:~:text=The%20OECD's%2037%20members%20are,Poland%2C%20Portugal%2C%20Slovak%20Republic%2C). And to get a list of countries that have had a female leader for the COVID-19 outbreak, I used BeautifulSoup to web-scrape a table with female heads of state and government from [Wikipedia](https://en.wikipedia.org/wiki/List_of_elected_and_appointed_female_heads_of_state_and_government).  

After the data was pre-processed, it was merged into a SQL database which was queried to extract information into dataframes 

Skills demonstrated: *pandas, numpy, sklearn, tensorflow, sqlite3, scipy.stats,  matplotlib, seaborn, requests, BeautifulSoup, geopy, folium*



### Project 2: ["Has COVID-19 affected the world's happiness and wellbeing?"](https://github.com/Amy-Reidy/Portfolio-by-Amy-Reidy/blob/main/World%20Happiness%20and%20Wellbeing%20-%20Stats%20Project/World%20Happiness%20and%20Wellbeing%20Project.ipynb)
![Beyond-Catastrophe](https://user-images.githubusercontent.com/73396449/123085318-6269a780-d422-11eb-85a9-babc7d78552b.jpg)

This is another project that I completed for my master's program, this time for the 'Statistics and Applied Probability' module. I used data from the World Happiness Report 2021 to test the following hypotheses:
 1.	Global happiness scores decreased from 2019 to 2020. 
 2.	Positive emotions decreased globally from 2019 to 2020. 
 3.	Negative emotions increased globally from 2019 to 2020.

As the differences between the samples were not normally distributed and had significant outliers, I decided to use a non-parametric test (Wilcoxon signed-rank test), rather than the paired T-test which is usually used for comparing paired samples. 

Skills demonstrated: *pandas, numpy, scipy, matplotlib, seaborn* 



### Project 3: [“Exploring Toronto Neighborhoods to Identify a Suitable Location for a New Indian Restaurant”](https://github.com/Amy-Reidy/Portfolio/blob/main/IBM%20Capstone%20Project%20-%20Exploring%20Indian%20Restaurants%20in%20Toronto.ipynb)

![shutterstock_573575497___Super_Portrait](https://user-images.githubusercontent.com/73396449/123547450-22c3f800-d761-11eb-9bd9-61e6df04b868.jpg)

This was my first ever data science project, which I did as a capstone project for [IBM's Data Science Professional Certificate](https://www.coursera.org/professional-certificates/ibm-data-science?utm_source=gg&utm_medium=sem&campaignid=2087860785&utm_campaign=10-IBM-Data-Science-ROW&utm_content=10-IBM-Data-Science-ROW&adgroupid=116274867101&device=c&keyword=&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=506892807488&hide_mobile_promo&gclid=Cj0KCQjw5auGBhDEARIsAFyNm9H3qhF5Sg8y6oWRoxM86ZqMkHP_gaTK_Y1x9O8FKXRNscBTeqVRav8aAttWEALw_wcB) in November 2020.

The aim of the project was to investigate where would be a suitable location for a new Indian restaurant in Toronto, based on the density of existing Indian restaurants and the number of Indian residents in each neighborhood.

Data was sourced by web-scraping Wikipedia, extracting information about various venues in Toronto and their geospatial information using Foursquare’s API, and obtaining geospatial for Toronto from “https://cocl.us/Geospatial_data”.

The K-means machine learning model was used to group the neighborhoods into clusters based on the density of Indian restaurants in each neighborhood.

Skills demonstrated: *pandas, numpy, sklearn, matplotlib, seaborn, requests, geopy, folium, wikipedia, yellowbrick*

