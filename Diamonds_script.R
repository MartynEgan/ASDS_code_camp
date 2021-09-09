##################
# Diamonds dataset
##################

#Setting our working directory

getwd()
?setwd()
setwd("") #Put your working directory here inside the quotes (""), with forward slashes (/) for the file path.

#We can also set our working directory using R Studio's 
#"New Project" function - check it out, it's in the top
#right corner...

library(tidyverse)

#Next, we list the different packages we will require in 
#order to execute the script. For this script, we will
#only need the tidyverse package.

summary(diamonds) # a function which gives a summary of the diamonds dataset
head(diamonds) #a function which gives the first 6 values of the diamonds dataset

#In our analysis, we are going to be working with the 
#*diamonds* dataset, which is a built-in dataset provided
#with the ggplot package. If you managed to successfully
#load the tidyverse package, diamonds should now be
#available to you.

ideal_cut <- diamonds[diamonds$cut == "Ideal",]
premium_cut <- diamonds[diamonds$cut == "Premium",]
very_good_cut <- diamonds[diamonds$cut == "Very Good", ]

#Most data science projects begin by organising our data.
#Here, we are taking three subsets of the diamonds data -
#The square brackets []are used to *subset* or filter our 
#dataset. Inside the brackets we call the dataset name, 
#diamonds, followed by the $ operator and the *variable* 
#we want to filter on. We then use two equals signs == 
#followed by the *category* of that variable which we want 
#to filter on. Do not worry for now about the comma ",".
#We assign each new subset to an object with a name using 
#the <- operator.

ideal_cut_mean <- mean(ideal_cut$price)
premium_cut_mean <- mean(premium_cut$price)
very_good_cut_mean <- mean(very_good_cut$price)

#We want to find out the average price for our diamonds
#according to the three types of cut we used to subset
#the data. We use the mean() function and assign the 
#output.

cut_boxplot <- diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(cut, price)) +
    geom_boxplot()

cut_boxplot #calling the object will plot it in the plots window

#As we might expect, there seems there to be quite a 
#difference between the average price of the 3 cuts of 
#diamond. But is everything as you might expect? Run the
#code above. What is strange about the box plot? This 
#could be an important finding. We give the plot object 
#an appropriate name and assign it.

class(diamonds$cut)
levels(diamonds$cut)

#The cut variable is what is known in R as an *ordered 
#factor*. A factor is a categorical variable (a variable
#with distinct categories). An ordered factor is a factor
#where the different possible categories have an explicit
#order. The levels() function shows us that order for the
#cut variable. Again, looking at the box plot, what is 
#strange?

mean(diamonds$carat)
mean(ideal_cut$carat) #mean carat, Ideal diamonds object 
mean(premium_cut$carat) #mean carat, Premium diamonds object 
mean(very_good_cut$carat) #mean carat, Very Good diamonds object 

#The carat of a diamond is the diamond's weight. Let's 
#see if there is any *interaction* with the cut variable. 
#Use the mean() function on the carat variable for your 
#3 diamonds subsets.

carat_boxplot <- diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(cut, carat)) + #here, we substituted "carat" for "price"
  geom_boxplot()

carat_boxplot #again, calling the object will draw the plot

#Recycling code is an important skill. You may not quite
#understand yet everything that's going on in the code
#above (which we used to generate the previous box plot),
#but we can edit it to produce a new box plot which 
#substitutes the carat variable for price. What do you 
#notice about the plot?

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(carat, price, color = cut)) +
  geom_point(alpha = 0.2) +
  geom_smooth() 

#Our final plot gives us a good idea of the interaction: 
#"ideal" diamonds tend to be smaller, but among diamonds
#of the same weight, "ideal" diamonds are more expensive,
#as we would expect. This only changes at the extremes of
#our data, where the "error bars" grow wider, showing that
#our estimated line of best fit is less reliable.

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(carat, price, color = cut)) +
  geom_smooth() +
  theme_classic() +
  labs(title = "Diamond price by weight and cut")

ggsave("diamond_price.pdf")

write_csv(diamonds, "diamonds.csv")

#We decide that the scatter plot is a bit busy, and the
#line plot with error bars does a good job of showing 
#the interaction effect on its own. We add a clean theme
#and a title to the plot, and decide to save a pdf of
#the plot as a record of our analysis. We also decide it
#would be a good idea to have a record of the data in the
#same location, so we use the write_csv() function to
#store a *comma-separated values* copy of the dataset. 
#We also decide to rename our script file and save it in 
#the same place. Now, when closing R, all the files should
#be in the working directory!