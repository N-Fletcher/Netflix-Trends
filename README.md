# Netflix-Trends
Herein lies a brief analysis of a Netflix dataset. [This data](https://www.kaggle.com/datasets/ashishgup/netflix-rotten-tomatoes-metacritic-imdb?resource=download) was collected by Ashish Gupta and last updated in April of 2021. Ashish essentially rounded up ratings data for nearly every movie/show that was on Netlfix at the time, as well as other relevent data such as director, cast, genre, etc. The majority of my analysis focuses on the success and revenue of titles based on different genres, directors, and more. Perhaps we can speculate what makes Netlix successful, and why it's slowly getting beaten out by its competitors.

The dataset, although extensive, had a lot of holes and missing data throughout. While this may have been due to numerous factors outside of our control, I still didn't want to use incomplete data. With the help of Python and csv, I filtered the original data into a new file that contained only titles with complete, unique data with the exception of a few decidedly useless columns that I didn't include. This filter turned out to be quite harsh, reducing the row count from 15,000 to 3,000. On one hand, we may be missing a vast amount of relevant titles that could help our analysis. On the other hand, we're left with a more complete dataset that won't skew the statistics with null values.
