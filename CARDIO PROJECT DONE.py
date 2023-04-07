#!/usr/bin/env python
# coding: utf-8

# In[1]:


# We import the various libraries we are going to use for our visualization

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


# we read the csv file using read_csv method in pandas and we store it in the variable df 

df = pd.read_csv("CardioGoodFitness-1.csv")


# In[3]:


df


# In[4]:


# to have a quick overview of what my data looks like I"ll be perform 3 operations
# sample, head and tail

df.sample(10)


# In[21]:


df.head(10)


# In[22]:


df.tail(10)


# In[5]:


df.shape


# - There are 180 rows and 9 columns in this dataset

# In[6]:


df.columns


# - These are the 9 column names specifying the features of the data we are about to analyse

# In[8]:


df.info()


# 
# - There are only two data types: integers and object
# - Also, there are no missing entries in our data set

# In[9]:


df.isna().sum()


# - There are no missing values in this dataset
# - Since there are no missing values, hence our data is cleaned and we can move to the analysis

# In[37]:


df.describe(include = "all")


# ### A STATISTICAL OVERVIEW OF THE DATA PROVIDES THE FOLLOWING OBSERVATIONS:
# 
# - The TM195 product type has the highest usage with 80 customers.
# 
# 
# - Males make up the highest number of treadmill product customers, with 104 recorded male customers.
# 
# 
# - The age range of our customers is between 18 and 50 years old, with an even split between those 26 years old or older and those 26 years old or younger. 75% of customers fall between 18 to 33 years old, while 25% are between 33 to 50 years old. Additionally, 25% of the customers are 24 years old or younger, while 75% are older than 24 years old.
# 
# 
# - Married people make up the majority of treadmill customers, with 107 recorded partnered customers.
# 
# 
# - The average income of our customers is 53,719, with the highest income recorded at 104,581 and the lowest at 29,562. 25% of customers earn between 58,668 to 104,561, while 75% earn between 29,562 to 58,688.
# 
# 
# - The highest number of miles ran by a customer is 360 miles, while the lowest is 21 miles. The average number of miles ran is 103 miles per week. 25% of customers run between 114 to 360 miles per week, while 75% run between 21 to 114 miles per week.
# 
# 
# - The average usage of our treadmills is three times a week, with the highest usage at seven times a week and the lowest at two times a week. 75% of customers use the treadmills between one to four times per week, while only 25% use them four to seven times per week.
# 
# 
# - 25% of customers ranked their fitness level as above 4, indicating they consider themselves strongly fit, while 75% ranked their fitness levels as 4 or below. This suggests that a large portion of our customer base does not consider themselves to be strongly fit.
# 
# 
# - The maximum number of years of education in our data is 21 years, while the lowest is 12 years. The average number of years of education is 16 years, with 75% of the customer base having between 12 and 16 years of education, and 25% having between 16 and 21 years of education. Additionally, 25% of customers reported having 14 years of education or less, while the remaining 75% reported having 14 years or more

# ### PRODUCT TYPE ANALYSIS

# In[10]:


df["Product"].value_counts()


# - There are only 3 product types: TM195, TM498 and TM798
# - The most used product is TM195 with 80 users
# - The least used is TM798 with 40 users
# - While TM498 which is in between the most and least used has 60 users

# In[84]:


sns.countplot(x = "Product", data = df)
plt.title("Number of Customers Vs Product Types")
plt.ylabel("Number of Customers")
plt.xlabel("Product Types");


# - The histogram above gives us a visual representation of the 3 product types; TM195, TM498 and TM798. 
# - TM195 has the highest number of customers of 80 as shown above and TM498 has 60 and TM798 has 40

# ##  CUSTOMER PROFILE FOR PRODUCT TM195 
# 
# 

# In[69]:


df[(df["Product"] == "TM195")].describe(include = "all")


# - There are 80 customers using M195 with 40 males and 40 females.
# 
# 
# - There is a higher number of married people using TM195. 48 customers are married while 32 are single
# 
# 
# - 75% of users are within the ages of 18 to 33 years and 25% are within the ages of 33 to 50 years
# 
# 
# - The average miles ran is 82.78 miles
# 
# 
# - The highest miles ran for TM195 is 188 miles and the highest usage is 5 times a week
# 
# 
# - The average income is 46,418 with the highest income of 68,220
# 
# 
# - The average fitness ranking is approximately 3. 
# 
# 
# - The average number of years of education is 15 years.

# ##  CUSTOMER PROFILE FOR PRODUCT TM498

# In[67]:


df[(df["Product"] == "TM498")].describe(include = "all")


# - There are 60 customers using TM498 with a higher number of male than females; 31 males and 29 females.
# 
# 
# - There is a higher number of married people using TM498. 36 customers are married while 24 are single
# 
# 
# - 75% of users are within the ages of 19 to 33.25 years and 25% are within the ages of 33.25 to 48 years
# 
# 
# - The average miles ran is 88 miles
# 
# 
# - The highest miles ran for TM498 is 212 miles and the highest usage is 5 times a week
# 
# 
# - The average income is 48,973 with the highest income of 67,083
# 
# 
# - The average fitness ranking is approximately 3. 
# 
# 
# - The average number of years of education is 15 years.

# ##  CUSTOMER PROFILE FOR PRODUCT TM798

# In[68]:


df[(df["Product"] == "TM798")].describe(include = "all")


# - There are 40 customers using M195 with a higher number of male than females; 33 males and 7 females.
# 
# 
# - There is a higher number of married people using TM195. 23 customers are married while 17 are single
# 
# 
# - 75% of users are within the ages of 22 to 30.25 years and 25% are within the ages of 30.25 to 48 years
# 
# 
# - The average miles ran is 82.78 miles
# 
# 
# - The highest miles ran for TM195 is 360 miles and the highest usage is 7 times a week
# 
# 
# - The average income is 75, 441 with the highest income of 104,581
# 
# 
# - The average fitness ranking is approximately 4. 
# 
# 
# - The average number of years of education is 17 years.

# ## UNIVARIATE ANALYSIS OF THE FEATURES OF THE VARIOUS PRODUCT TYPES

# ### A) GENDER

# In[117]:


# We are drawing a bar chart to visually represent the gender number for each product

sns.countplot(x = "Product", data = df, hue = "Gender")
plt.title("Gender Usage For Each Product Type")
plt.xlabel("Product Types")
plt.ylabel("Number of Customers");


# #### The Histogram above gives us the number of males and females using each product type
# 
# - For TM195 there is an equal number of males and females using it. 40 each resepectively.
# - There are 31 males and 29 females using TM498
# - There are 33 males and 8 females using the TM798
# 
# - So the highest number of males are using TM195 and TM798 has the lowest number of females
# - TM195 has the highest number of female usage
# - Generally TM195 has the highest number of customers for both male and female

# ### B) MARITAL STATUS

# In[118]:


# We are drawing a bar chart to visually represent the marital status for each product

sns.countplot(x = "MaritalStatus", data = df, hue = "Product")
plt.title("Histogram of MaritalStatus")
plt.xlabel("Marital Status")
plt.ylabel("Number of Customers");


# - We can see that married people are the highest users of the 3 product categories. With married people totally 107 and single people totally 71
# - Across the 3 product categories there is a higher number of married people than single
# - TM195 has both the highest number of married customers and single customers. It 48  married customers while single customers 32
# 
# 

# ### C) AGE

# In[123]:


# We are drawing a bar chart to visually represent the age distribution for each product

sns.histplot(x = "Age", data = df, kde = True, hue = "Product")
plt.title("Age Distribution ")
plt.xlabel("Age in Years")
plt.ylabel("Number of Customers");


# - The age distribution for TM798 is rightly skewed with a larger customer base within the ages of 23 to 32 years. It also has the oldest customer of 50 years.
# - TM195 and TM498 are both slightly rightly skewed.
# - TM498 has majority of its customer base within the ages of 30 - 35 years
# 

# ### D)  FITNESS

# In[126]:


# We are drawing a bar chart to visually represent the fitness distribution for each product

sns.countplot(x = "Fitness", data = df, hue = "Product")
plt.title("Fitness Ranking For Each Product Type")
plt.xlabel("Fitness(1 - 5)")
plt.ylabel("Number of Customers");


#  - TM798 customers ranked the highest with 27 customers ranking 5 for strongly fit. It's ranking did not go below 3
#  - A higher number of T195 AND TM498 customers reported a ranking of 3. Meaning the were just fit.
#  

# ### E) INCOME

# In[127]:


# We are drawing a histogram plot to visually represent the fitness distribution for each product

sns.histplot(x = "Income", data = df, hue = "Product")
plt.title("Income of Customers For Each Product Type")
plt.xlabel("Income")
plt.ylabel("Number of Customers");


# - From the histogram TM798 customers are high earners. A large number of customers earn between 70,000 and 100,000.
# - TM195 and TM498 customers are average earners, earning between 35,000 to 69,000

# ### F) USAGE

# In[129]:


# We are drawing a bar chart to visually represent the usage distribution for each product

sns.countplot(x = "Usage", data = df, hue = "Product")
plt.title("Usage For Each Product Type")
plt.xlabel("Usage(Average Number of Times Used Per Week)")
plt.ylabel("Number of Customers");


# - We can see from the bar chart above that TM798 customers are the highest users with highest usage being 7 and lowest being 3
# - TM498 and TM195 both have most customers using it mostly 3 times a week. They both have an average of about 3 for usage and they 

# ### G) MILES

# In[134]:


# We are drawing a histogram to visually represent the miles distribution for each product

sns.histplot(x = "Miles", data = df, hue = "Product")
plt.title("Miles Ran For Each Product Type")
plt.xticks(rotation = 69)
plt.xlabel("Miles")
plt.ylabel("Number of Customers");


# - TM798 customers have the highest miles ran of 360 miles. This is understandable, given that they have the highest usage.
# - TM195 customers have the lowest miles ran among the 3 product categories with highest mile ran of about 180

# ### H) EDUCATION

# In[136]:


# We are drawing a bar chart to visually represent the miles distribution for each product

sns.countplot(x = "Education", data = df, hue = "Product")
plt.title("Education in Years For Each Product Type")
plt.xlabel("Education in Years")
plt.ylabel("Number of Customers");


# - TM798 customers have the highest number of years spent acquiring an education. The lowest number of education in years for this product category is 14 years and the highest is 21 years 
# - A majority of TM195 customers have spent between 14 to 16 years in education
# - TM498 have a large number of her customers between 14 years and 16 years in eduation

# ## MULTIVARIATE ANALYSIS FOR PRODUCT TYPES

# In[85]:


# We will analyse the relationship between the various features

df.corr()


# #### From the table above:
# - There is slightly positive relationship bewteen Age and Income
# - There is slightly positive relationship between Education and Income
# - There is a highly positive reationship between Usage and Fitness
# - There is a highly positive relationship between Usage and Miles
# 

# ### 1) A PLOT OF AGE VS INCOME

# In[141]:


# we draw a scatterplot to show the relationship between age and income

sns.scatterplot(x= "Age", y = "Income", data = df, hue = "Product")
plt.title("Age Vs Income ")
plt.xticks(rotation = 90)
plt.xlabel("Age in Years")
plt.ylabel("Income");


# - There is a slightly positive positive between age and income 
# - For the various product categories, majority of the highest earners are TM798 customers
# - There's a substantial number of customers within ages of 30 to 50 years earning above 70,000 for TM798 customers
# 

# ### 2) A PLOT OF EDUCATION VS INCOME

# In[149]:


# we draw a scatterplot to show the relationship between education and income

sns.scatterplot(x= "Education", y = "Income", data = df, hue = "Product")
plt.title("Plot of Education vs Income ")
plt.xlabel("Education in Years")
plt.ylabel("Income");


# - There is a slightly positive relationship between education and income. Customers with education of 16 years and above have a larger income. 
# - Most TM798 customers have between 16 to 21 years of education and earn from 50,000 to over 100,000
# - Most TM498 customers have 14 years in education and are earning from 32,000 to about 58,000
# - A few TM195 customers have 18 years in education and earn between 60,000 to 70,000

# ### 3) A PLOT OF FITNESS VS USAGE

# In[155]:


# we draw a scatterplot to show the relationship between fitness and usage

sns.scatterplot(x = "Fitness", y = "Usage", data = df, hue = "Product")
plt.title("Plot of Fitness Vs Usage")
plt.xlabel("Fitness(1-5)")
plt.ylabel("Usage(Average Number of Times Used Per Week)");


# - There is a positive relationship between Fitness and Usage
# - The higher the usage the higher the fitness
# - Majority of TM798 customers have a high usage resulting to a high fitness rank
# - Most TM195 customers reported  a low rank because low usage
# - Most TM498 customers lie between 2 to 5 for usage and 2 to 3 for rank

# In[160]:


sns.scatterplot(x= "Fitness", y = "Miles", data = df, hue = "Product")
plt.title("Plot of Fitness Vs Miles")
plt.xlabel("Fitness(1-5)")
plt.ylabel("Miles");


# - There is a positive relationship between Fitness and Miles ran
# - The more miles ran the higher the fitness ranking
# - TM798 customers ranked higher than TM498 and TM195 customers and had more miles ran

# ## INSIGHTS FROM THE DATA ANALYSIS
# 
# - The largest customer base across all three product categories was comprised of married individuals, particularly men, indicating that fitness is particularly appealing to this demographic. As a result, targeting married individuals in advertising may be a fruitful strategy.
# 
# 
# - The age range of 24-33 years old constitutes the majority of fitness customers, suggesting that younger individuals are more interested in fitness compared to older individuals.
# 
# 
# - Based on the positive correlation between fitness and treadmill usage, it can be inferred that customers who spend more time per week on the treadmill tend to have higher fitness rankings.
# 
# 
# - The majority of treadmill users are male, indicating that more men use the treadmill for fitness compared to women.
# 
# 
# - Despite having the highest ranking, usage, income, and education, TM798 has the lowest number of customers, suggesting that the product may require a rebrand or redesign to increase awareness and appeal to a larger audience. Its high usage indicates its effectiveness.
# 
# 
# - TM798 has a relatively low number of female customers, which may be attributed to aesthetics. As previously mentioned, a redesign may be necessary to enhance its visual appeal and attract more female customers.
# 
# 
# - TM195 has 80 customers, but has the lowest usage and ranking. If a large number of customers are purchasing the product but not using it, the product should be examined for possible technical issues
# 
# 
# - Despite having over 60 customers, the TM498 category did not exhibit any noteworthy results across its various features.

# In[ ]:




