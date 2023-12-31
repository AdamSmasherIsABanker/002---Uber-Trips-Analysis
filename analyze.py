import pandas as dataTool

data = dataTool.read_csv('American.csv')

# the busiest time to order an uber 
busiestTime = data['TIME'].describe()['top']

# the busiest date to order an uber
busiestDay = data['DATE'].describe()['top']

# the amount of ubers ordered on the busiest day
ubersOrderedOnBusiestDay = data['DATE'].describe()['count']

# getting the least congested day to order an uber.
pickupdataValueCounts = data['TIME'].value_counts()
leastCongested = pickupdataValueCounts.index[pickupdataValueCounts.argmin()]

print('The most ubers were ordered at ' + busiestTime + " on " + busiestDay + " with " + str(ubersOrderedOnBusiestDay) + " ubers ordered. ")
print("")
print('The best time to order an uber is ' + leastCongested + )
