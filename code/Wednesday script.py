########################
# ASDS Code Camp Day 3 #
########################
# Python basics #
#################

# The hash sign "#" is used to comment out text
# Text preceded by "#" will not be read by Python

This will be read by Python, and will produce an error message

####################
# First things first
####################

# There is no equivalent in Python to R's ls() function. 

# Calling dir() in Python is similar to calling ls() and search() 
# simultaneously in R: it provides a list of names of objects in the 
# current *scope*, which is similar to R's concept of environment.

dir()

dir?

# Unlike R, there isn't a clear distinction between objects *you* 
# create and Python's internal objects. In fact, each time you ask
# Python to interpret a line of code in the console, it saves that
# line as an object. 

_1
dir(_1)

# Fortunately, spyder has a variable explorer, which helps keep
# things tidy. You can see variables in the window, and import or
# remove variables.

a = "Hello World"
print(a)

# The core distribution of Python has very limited data science 
# capabilities. For this reason, doing data analysis in Python 
# requires additional libraries to be attached.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# The three most important of these libraries are numpy (short for
# Numerical Python), which provides some additional data structures
# for arrays; pandas (short for Panel Data), which does the same for 
# tabular data; and matplotlib, which provides graphical capabilities.
# Anaconda comes with all three installed, and to use them in a 
# Python session we *import* them *as* an abbreviated version. 

conda update package_name

# To update a package in Anaconda we use the above command.

conda install package_name

# To install a new package in Anaconda we use the above command.

#######
# Help!
#######

# Accessing help in Python is similar to R. Calling the help() 
# function, and passing the name of a function within the brackets,
# will call the help file for that function. It is also generally 
# possible to use a question mark (?) as a shortcut, though be 
# careful as this is not a "built-in" capability.

help()
help?
?help

# Next we call help on a built-in function, len(), which works
# like length() in R - or does it? When we pass our recently created
# object "a" to the length() function, what value does it return?

len(a)
len?
help(len)

help(pd)

#############
# Making data
#############

# Mostly in Python you will be dealing with data which you have
# imported from external sources, or data types associated with 
# numpy or pandas. However, it is good to know about Python's basic 
# data structures, because everything else is built on them, and they
# can be less intuitive to work with than R.

# In R, the assignment operator is <-. In Python, we use the equals
# sign (=). (We can also use = in R, but it is discouraged to do so
# as it behaves slightly differently to <- in some circumstances).

b = 5
print(b)

# Python has numerous types of data structures: "a" is a string (str); 
# "b" is an integer (int), which are both types of *scalar*, or 
# single values; "c" and "d", below, are both *lists*, which contain multiple 
# values. Note the use of square brackets [] and comma separation of 
# values. Note also that a list can contain both integers and strings.

c = [1, 2, 3]
print(c)

d = [1, "two", 3]
print(d)

# A *tuple* is similar to a list, but its contents cannot be modified.
# Note that round brackets () are not needed, but can be used.

e = 1, 2, 3
print(e)

f = (1, 2, 3)
print(f)

# The last two basic structures are sets and dictionionaries (dicts). 
# A set is like a list, but can only contain unique elements: here, 
# "g" and "h" are identical. Sets are created using curly braces {}. 
# A dict is an important data structure in python. Similar to a set, it is 
# created using curly braces, but it contains pairs of *keys* and *values*, 
# separated by colons. 

g = {1, 2, 3, 4}
print(g)

h = {1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4}
print(h)

i = {1: 'This', 2: 'is', 3: 'a', 4: 'dict'}
print(i)

# The example below gives an idea of how data science libraries such
# as pandas build on basic Python data structures. Here, we create a 
# dict comprising three lists, each defined by a different key. If 
# we then pass this dict to the DataFrame() function in pandas 
# (remembering to use the pd. alias when calling the function) we 
# can tranform the dict into a dataframe: a much more useful data
# structure for data analysis.

data = {'year': [1992, 1997, 2002, 2007, 2011, 2016, 2020],
        'party': ['Fianna Fail', 'Fianna Fail', 'Fianna Fail', 'Fianna Fail', 'Fine Gael', 'Fine Gael', 'Fianna Fail'],
        'seats': [68, 77, 81, 78, 76, 50, 38]}

print(data)
type(data)

data_frame = pd.DataFrame(data)
print(data_frame)

###########
# Functions
###########

# We were introduced to functions in the section on help. An 
# important difference between Python and R is the concept of 
# *methods*. 

# In R, every function is called the same way: the name of the 
# function is followed by round brackets, and the *arguments*
# of the function are placed inside the brackets. 

# Many Python functions operate the same way. However, *methods* 
# operate slightly differently. A method is a function which 
# belongs to a specific *class* of object, and it is called by 
# placing a dot (.) after the name of the object, followed by the method, 
# followed by round brackets. 

# Here, we make a list of numbers, "a", which we then 
# convert into a dataframe, an object belonging to the pandas module,
# using the function DataFrame() and the pd alias. We then call the 
# mean() *method*, a type of function belonging to the dataframe 
# class, on this object. 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = pd.DataFrame(a)
a.mean()

# To call the help file on a method, we need to supply an object of 
# the proper class. Here, for example, the first four calls to help 
# on the .mean() method do not work. Calling help on methods can be 
# extremely unintuitive, and is a good example of Python's steep 
# learning curve. 

?mean
?mean()
?.mean()
help(mean)

?a.mean

# Next, we call the .mean() method on the 'seats' column of the 
# data_frame object we just created. Notice that to select the seats 
# column we can use either a dot (.) after the name of our object, 
# or square brackets [] with the column name inside, surrounded by 
# quotes ''. Note how this differs to R's $ operator. We then call 
# the mean() method by adding another dot(.), followed by round 
# brackets. 

data_frame.seats.mean()
data_frame['seats'].mean()

# It is possible to *chain* methods together to perform fairly 
# complex operations in a very concise manner. 

# Say we wanted to calculate the average number of seats won by the 
# largest party in the Dail following a general election, and to see 
# whether there is any difference between the average number of seats 
# won by Fianna Fail and Fine Gail. To achieve this, we first select our 
# object and column of interest, data_frame['seats']. 

# We then use the groupby method, a function which *groups* the 'seats' 
# column *by* the values in the 'party' column. 

# If we then call the mean method on this newly grouped data, Python will 
# return the average seats for each party. 

data_frame['seats'].groupby(data_frame['party']).mean()

# The same syntax works equally well with the std method, which returns 
# the standard deviation of the mean we just calculated. What does this 
# tell us about the respective parties?

data_frame['seats'].groupby(data_frame['party']).std()

# Below is a simple function, which demonstrates one of the most 
# important aspects of Python as a programming language: indentation.

def a_function(x):
    if x > 1:
        print("x is greater than 1")
    else:
        print("x is less than or equal to 1")

a_function(5)
a_function(-5)

# Whereas in R indentation is of little importance (it is mainly used
# as a convention to help with readability of code), in Python it is
# extremely important. Indentation tells Python which sections of 
# code belong together. Here, the "if" and "else" statements are both
# at the same level of indentation, as are the two calls to "print".
# This is a bit like telling Python "if the argument I give you, x,
# is bigger than 1, print the first statement. Otherwise, print the
# second one." In R, we would use curly braces {} and commas "," to
# separate these statements.

##########
# Plotting
##########

# We use the matplotlib library in Python to provide graphical 
# capabilities, aliased as "plt". 

# Below, we create a simple line plot of the number of seats won by 
# the leading party at each GE since 1992. Note how we build up our 
# plot in stepwise fashion: we begin with a call to the plot() function, 
# in which we specify our x and y axes, taking advantage of *positional* 
# arguments (i.e. the *first* argument in the function is the x axis, the 
# *second* is the y axis). We then call the xlabel(), ylabel() and title() 
# functions. This approach to plotting graphics is very similar to R's base
# graphics, which we briefly used yesterday. In spyder the resulting
# plot is displayed automatically. In other editors you may need to
# explicitly render the plot using the plt.show() function.

plt.plot(data_frame.year, data_frame.seats)
plt.xlabel("Year")
plt.ylabel("Seats")
plt.title("No. of seat won by leading party, General Elections 1992-2020")

##########
# Activity
##########

# By recycling the code below (i.e. changing the values), try to 
# create a dataframe and a line plot for the number of seats of the 
# second largest party over the same period. You can find the figures 
# at wikipedia: https://en.wikipedia.org/wiki/D%C3%A1il_election_results

data = {'year': [1992, 1997, 2002, 2007, 2011, 2016, 2020],
        'party': ['Fianna Fail', 'Fianna Fail', 'Fianna Fail', 'Fianna Fail', 'Fine Gael', 'Fine Gael', 'Fianna Fail'],
        'seats': [68, 77, 81, 78, 76, 50, 38]}

data_frame = pd.DataFrame(data)
print(data_frame)

data_frame.seats.mean()
data_frame['seats'].mean()

data_frame['seats'].groupby(data_frame['party']).mean()
data_frame['seats'].groupby(data_frame['party']).std()

plt.plot(data_frame.year, data_frame.seats)
plt.xlabel("Year")
plt.ylabel("Seats")
plt.title("No. of seat won by leading party, General Elections 1992-2020")

################
# And finally...
################

# There is much more to Python as a language, but the learning curve
# can be quite steep, and it is easy to become overwhelmed. For this
# reason we will leave it here for today - Congratulations, you 
# survived Python basics!
