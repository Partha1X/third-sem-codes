#Write a program to compute standard deviation(SD)of 1,3,5,7,11 and 12(PyQ2019)
'''
Standard Deviation (SD) = sqrt((1/N) * sum((x_i - mean)^2))

where:
- N is the number of data points,
- sum denotes the sum over all data points,
- x_i represents each individual data point,
- mean is the mean of the data set.
'''
import math

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / len(numbers)
    standard_deviation = math.sqrt(variance)
    return standard_deviation

# Given set of numbers
data = [1, 3, 5, 7, 11, 12]

# Calculate and print the standard deviation
sd = calculate_standard_deviation(data)
print(f"The standard deviation of the given data is: {sd:.2f}")
