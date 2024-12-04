# This file shows how you can use the function get_data in the DataClean function
from DataClean import get_data

data = get_data()

print(data[:10]) # display the first 10 values

# the data is a list of tuples. Each tuple is formatted like: (county name, state, covid_cases_per_100k)

# when we sort, we can sort using the last value in the tuple, covid_cases_per_100k

# below is an example using python's inbuilt sort

data.sort(key = lambda x: x[2]) # sorting based on the 2nd (last) value in the tuple

print(data[-10:]) # notice that the printed values have 0 covid cases. This is because we have successfully sorted our tuples

# we now have to do the same using our own merge and heap sort