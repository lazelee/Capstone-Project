# Capstone-Project
In the MGTC28 Capstone Project, students will work on real datasets to get an experience of what data scientists go through in real life. The group assignment's objectives are to define a business problem, look for data on the web, and use Foursquare location data to compare different neighbourhoods in Toronto to figure out which neighbourhood is suitable for starting a new local business. The UTSC Venture Capital Fund is investing up to $1 million CAD in your group to launch a new local business, anywhere within the city.  Your group is open to pitch any business ideas that is profitable in the next couple of years.

# Pest Control

# Part 3: Exploring Competitors and Commercial Demographics
The Foursquare API allow you to search places, and discover businesses within certain distance to an address.  You can also get reviews and other information related to the places. Use Foursquare API to search places, discover businesses within certain distance to an address, see their reviews and other information related to the places.

However, due to limited competitor data availability from the Foursquare API, we adopted an alternative approach focusing on commercial demographics. Specifically, we analyzed the density of Fast Food Restaurants in Toronto neighborhoods as a proxy for commercial activity and potential consumer demand.

# Steps Taken:
Data Collection:
  - Extracted Fast Food Restaurant data from the Foursquare API and visualized their geographical distribution.
Clustering Analysis:
  - Applied K-Means clustering to group neighborhoods based on the density of fast-food venues.
  - Identified the ideal cluster as one with the highest neighborhood count and average number of fast-food restaurants.
Comparison with Residential Demographics:
  - Compared the selected commercial neighborhoods to the top residential neighborhoods from Part 2 to finalize our recommendation.

This approach allowed us to integrate residential and commercial considerations in our business decision-making, ensuring a broader consumer base for our pest control business.

