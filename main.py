# Talking Data Starter Code

### -- Part 2 Setting up the program -- ###
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "The Vow"
print("My favorite movie is " + favMovie)


### -- Part 3 Investigate the data -- ###
#print(movieData.head())
#print(movieData["movie_title"])


### -- Part 4 Filter data -- ###
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList = movieData["movie_title"] == favMovie
#print(favMovieBooleanList)

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre (step 2)
dramaMovieBooleanList = movieData["genres"].str.contains("Drama")
dramaMovieData = movieData.loc[dramaMovieBooleanList]

numOfMovies = dramaMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Drama in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Drama.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

### -- Part 5 Describe data -- ###
#find min
min = dramaMovieData["audience_rating"].min()
minDifference = favMovieData.iloc[0, 3] - min
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated " + str(minDifference) + " points higher than the lowest rated movie.")
print()

#find max
max = dramaMovieData["audience_rating"].max()
maxDifference = max - favMovieData.iloc[0, 3]
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated " + str(maxDifference) + " points lower than the highest rated movie.")
print()

#find mean
mean = dramaMovieData["audience_rating"].mean()
meanDifference = mean - favMovieData.iloc[0, 3]
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " lower than the mean movie rating by " + str(meanDifference) + ".")

#find median
median = dramaMovieData["audience_rating"].median()
medianDifference = median - favMovieData.iloc[0, 3]
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " lower than the median movie rating by " + str(medianDifference) + ".")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

### -- Part 6 Create graphs -- ###
#Create histogram
plt.hist(dramaMovieData["audience_rating"], range = (0, 100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Drama Movies Histogram")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Drama Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most values are between the ratings of 75 to 79 reaching over 800 drama movies. The histogram also shows a distribution slightly skewed to the left."
)
print()

#Show histogram
plt.show()
input("Press enter to see the next data visualization.\n")

#Clears plot
plt.cla()

#Create scatterplot
plt.scatter(data = dramaMovieData, x = "audience_rating", y = "critic_rating", label = "Drama Movies")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Rating Versus Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Plots favorite movie
plt.scatter(data = favMovieData, x = "audience_rating", y = "critic_rating", label = favMovie)
plt.legend()

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, there is a very slight positive correlation. Due to the vast area that the dots hold, however, no significant correlation can be concluded. There are quite a few outliers, vastly different from where the majority of values are (like the 0 critic rating with almost 100 audience rating, while the majority are both almost 100 in both categories)."
)
print()
print("According to the scatter plot, " + favMovie + " follows the scatter plot's overall pattern, being part of the majority rather than an outlier. The critic rating is overall lower than the audience rating.")
print()


#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
