# Objective
In the MGTC28 Capstone Project, students will work on real datasets to get an experience of what data scientists go through in real life. The group assignment's objectives are to define a business problem, look for data on the web, and use Foursquare location data to compare different neighbourhoods in Toronto to figure out which neighbourhood is suitable for starting a new local business. The UTSC Venture Capital Fund is investing up to $1 million CAD in your group to launch a new local business, anywhere within the city.  Your group is open to pitch any business ideas that is profitable in the next couple of years.

# Data Description
For this project, we need the following data:
1. ***Toronto City data that contains Borough, Neighbourhoods along with there latitudes and longitudes***
* **Data Source:** https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
* **Description:** This Wikipedia page contain all the information we need to explore and cluster the neighborhoods in Toronto
2. ***Geographical Location data using Geocoder Package***
* **Data Source:** https://cocl.us/Geospatial_data
* **Description:** The second source of data provided us with the Geographical coordinates of the neighbourhoods with the respective Postal Codes.
3. ***Canada Census***
* **Data Source:** https://www12.statcan.gc.ca/census-recensement/2021/dp-pd/prof/index.cfm?Lang=E
* **Description:** By scraping the 2021 census population, we can specify the postal code to obtain data about a particular neighbourhood.
4. ***Venue Data using Foursquare API***
* **Data Source:** https://foursquare.com/developers/apps
* **Description:** From Foursquare API we can get the name,category,latitude,longitude for each venue.


# Pest Control
### Part 1

### Part 3: Exploring Competitors and Commercial Demographics
The Foursquare API allow you to search places, and discover businesses within certain distance to an address.  You can also get reviews and other information related to the places. Use Foursquare API to search places, discover businesses within certain distance to an address, see their reviews and other information related to the places.

However, due to limited competitor data availability from the Foursquare API, we adopted an alternative approach focusing on commercial demographics. Specifically, we analyzed the density of Fast Food Restaurants in Toronto neighborhoods as a proxy for commercial activity and potential consumer demand.

#### Steps Taken:
1) Data Collection:
  - Extracted Fast Food Restaurant data from the Foursquare API and visualized their geographical distribution.
2) Analysis:
  - Applied K-Means clustering to group neighborhoods based on the density of fast-food venues.
  - Identified the ideal cluster as one with the highest neighborhood count and average number of fast-food restaurants.
3) Comparison with Residential Demographics:
  - Compared the selected commercial neighborhoods to the top residential neighborhoods from Part 2 to finalize our recommendation.

This approach allowed us to integrate residential and commercial considerations in our business decision-making, ensuring a broader consumer base for our pest control business.

