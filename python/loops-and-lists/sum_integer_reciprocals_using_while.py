import numpy as np

# original code
# summation = 0
# starting_index = 1
# index = starting_index
# maximum_index = 100
#
# while index < maximum_index:
#     summation += 1 / index
#
# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index <= maximum_index:
    summation += 1/index
    index += 1

#for loop
#summation = sum(1 / k for k in range(1, 101))
#print(f'sum(k = 1, 100) 1/k = {summation}')

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.6f}')#:.6f for 6 digits after decimal point
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.3f}') #:.nf number of folate digits
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.2f}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 3

while index <= maximum_index:
    summation += 1/index
    index += 1

#for loop
#summation = sum(1 / k for k in range(1, 4))
#print(f'sum(k = 1, 3) 1/k = {summation}')

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.6f}')#:.6f for 6 digits after decimal point
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.3f}') #:.nf number of folate digits
#print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.2f}')

#the while condition should be <= to include maximum index
#the index needs to be indicated to the while loop

#hand solved 1/k summation
#1/1 +1/2 + 1/3 = 1 5/6 =1.8333

#chatgpt code
#summation = 0
#starting_index = 1
#index = starting_index
#maximum_index = 100

#while index <= maximum_index:  # Use <= to include the maximum index in the sum
#     summation += 1 / index
#     index += 1  # Increment index to avoid infinite loop
#
# print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation}')
