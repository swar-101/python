# Lambda functions doesn't allow multiple statements,
# however we can create 2 lambda functions and then
# as a parameter to the first function and then call
# other lambda functions and then call the other
# lambda functions as a parameter to the first function.
# Let's try to find the second maximum element using
# lambda!

List = [[2, 3, 4], [3, 5, 7], [3, 2, 4]]

# Sort each sublist
sort_list = lambda x: (sorted(i) for i in x)

# Get the second-largest element
second_largest = lambda x, f: [y[len(y)-2] for y in f(x)]

result = second_largest(List, sort_list)

print(result)

# In PyCharm press Shift+F10 to run the code :)
