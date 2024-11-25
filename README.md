# Objective
In the MGTC28 Capstone Project, students will work on real datasets to get an experience of what data scientists go through in real life. The group assignment's objectives are to define a business problem, look for data on the web, and use Foursquare location data to compare different neighbourhoods in Toronto to figure out which neighbourhood is suitable for starting a new local business. The UTSC Venture Capital Fund is investing up to $1 million CAD in your group to launch a new local business, anywhere within the city.  Your group is open to pitch any business ideas that is profitable in the next couple of years.

# Data Description
For this project, we need the following data:
1. ***Toronto City data that contains Borough, Neighbourhoods along with there latitudes and longitudes***
* **Data Source:** https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
* **Description:** This Wikipedia page contain all the information we need to explore and cluster the neighbourhoods in Toronto
2. ***Geographical Location data using Geocoder Package***
* **Data Source:** https://cocl.us/Geospatial_data
* **Description:** The second source of data provided us with the Geographical coordinates of the neighbourhoods with the respective Postal Codes.
3. ***Canada Census***
* **Data Source:** https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E
* **Description:** By scraping the 2021 census population, we can specify the postal code to obtain data about a particular neighbourhood.
4. ***Venue Data using Foursquare API***
* **Data Source:** https://foursquare.com/developers/apps
* **Description:** From Foursquare API we can get the name, category, latitude, and longitude for each venue.


# Pest Control
## Part 1
To decide what business we wanted to enter, we looked through IBIS World and looked at different industries in Canada.  At first we were looking at more traditional bigger industries like airlines and sporting goods but landed on a very different and unique page: Pest Control.  At first we thought of it more as a joke but as we looked through the report we saw some good signs of entering this market, such as increasing revenues every year (even throughout COVID), low volatility and and above GDP growth.  The life cycle of pest control is at an early stage of quantity growth, and the barriers to enter is moderate meaning that it might be hard for us to enter at first but also there is less competitors later if we enter.  Another main factor is that there is no big market leader so that the market is very competitive and we are able to gain market share easily.  One disadvantage to this business is that there is little differentiation between other businesses, making it harder to charge a more premium price. 

## Part 2
Objective:
- To analyze demographic data from the 2021 Canadian Census to identify neighborhoods in Toronto with high potential for a new pest control business. Key metrics include population, income, housing characteristics, and professional demographics.

#### Steps Taken:
1) Data Collection:
  - Scraped demographic data for Toronto postal codes using BeautifulSoup and urllib.
  - Collected key data points:
  - Population size
  - Median Income
  - Number of older housing units
  - Number of apartment units
  - Number of health professionals
2) Analysis:
  - Normalized data using min-max scaling for comparability.
  - Applied a weighted Composite Scoring system to rank neighborhoods:
  - 30%: Older housing units
  - 25%: Population size
  - 20%: Apartment units
  - 15%: Median income
  - 10%: Health professionals

Ranked neighborhoods based on composite scores to identify the top 5 most suitable areas.



## Part 3: Exploring Competitors and Commercial Demographics
Our first approach used Foursquare to get all the locations of our competitors, including their ratings, pricing, and foot traffic. However, Foursquare did not have the data available in their database. Therefore, we adopted an alternative approach focusing on our commercial demographics to further support our choice of neighbourhood. Specifically, we analyzed the density of Fast Food Restaurants in Toronto neighbourhoods as a proxy for commercial activity and potential consumer demand.

#### Steps Taken:
1) Data Collection:
  - Extracted Fast Food Restaurant data from the Foursquare API and visualized their geographical distribution.
2) Analysis:
  - Applied Elbow Method of K-Means clustering to group neighbourhoods based on the density of fast-food venues.
  - Identified the ideal cluster as one with the highest restaurant count and highest average number of fast-food restaurants.
  - Applied Elbow Method of K-Means clustering to group neighbourhoods based on the density of pest control venues.
  - Identified the ideal cluster as one with the highest neighbourhood count and lowest average number of pest control venues.
3) Comparison with Residential Demographics:
  - Compared the ideal cluster to the top residential neighbourhoods from Part 2 to finalize our recommendation.

This approach allowed us to integrate residential, commercial, and competitive considerations in our business decision-making, ensuring a broader consumer base for our pest control business.

