###################
# Call me something
###################

#Setting our working directory

getwd()
?setwd()
setwd("C:/Some/File/You/Chose")

#We can also set our working directory using R Studio's 
#"New Project" function - check it out, it's in the top
#right corner...

library(some_package)

#Next, we list the different packages we will require in 
#order to execute the script. For this script, we will
#only need the tidyverse package, so go ahead and edit
#the call to library().

summary(diamonds)
head(diamonds)

#In our analysis, we are going to be working with the 
#*diamonds* dataset, which is a built-in dataset provided
#with the ggplot package. If you managed to successfully
#load the tidyverse package, diamonds should now be
#available to you.

an_object <- diamonds[diamonds$cut == "Ideal",]
anotherObject <- diamonds[diamonds$cut == "Premium",]
Object3 <- diamonds[diamonds$cut == "Very Good", ]

#Most data science projects begin by organising our data.
#Here, we are taking three subsets of the diamonds data -
#can you work out what the code is doing? Each new subset
#becomes an object with a name. The names provided are
#not very good. Choose your own name in keeping with good
#data science principles, and edit the code accordingly.

mean(an_object$price)
mean(anotherObject)
mean()

#We want to find out the average price for our diamonds
#according to the three types of cut we used to subset
#the data. Edit and complete the code above to find out.
#What would you need to add to the code if you wanted to
#create 3 new objects containing the different means?
#What names might you give these objects? Go ahead and
#try it out.

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(cut, price)) +
    geom_boxplot()

#As we might expect, there seems there to be quite a 
#difference between the average price of the 3 cuts of 
#diamond. But is everything as you might expect? Run the
#code above. What is strange about the box plot? This 
#could be an important finding. Give the plot object an
#appropriate name and assign it.

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
#mean carat, Ideal diamonds object 
#mean carat, Premium diamonds object 
#mean carat, Very Good diamonds object 

#The carat of a diamond is the diamond's weight. Let's 
#see if there is any *interaction* with the cut variable. 
#Use the mean() function on the carat variable for your 
#3 diamonds subsets.

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(cut, price)) +
  geom_boxplot()

#Recycling code is an important skill. You may not quite
#understand yet everything that's going on in the code
#above (which we used to generate the previous box plot),
#but you should be able to work out how to edit it to 
#produce a new box plot which substitutes the carat
#variable for price. Give it a go, and don't forget to 
#also make an appropriately named object. What do you 
#notice about the plot?

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(carat, price, color = cut)) +
  geom_point(alpha = 0.2) +
  geom_smooth() 

#Our final plot gives us a good idea of the interaction:
#can you describe what is happening here?

diamonds %>%
  filter(cut %in% c("Ideal", "Premium", "Very Good")) %>%
  group_by(cut) %>%
  ggplot(aes(carat, price, color = cut)) +
  geom_smooth() +
  theme_classic() +
  labs(title = "Pick a good title for this plot")

ggsave("Name this plot.pdf")

write_csv(diamonds, "Name this data.csv")

#We decide that the scatter plot is a bit busy, and the
#line plot with error bars does a good job of showing 
#the interaction effect on its own. We add a clean theme
#and a title to the plot, and decide to save a pdf of
#the plot as a record of our analysis. Choose a name for
#the file, and then call the function. We also decide it
#would be a good idea to have a record of the data in the
#same location, so we use the write_csv() function to
#store a *comma-separated values* copy of the dataset. 
#We also decide to rename our script file and save it in 
#the same place. Now try closing R. Can you find the 
#files in the working directory?