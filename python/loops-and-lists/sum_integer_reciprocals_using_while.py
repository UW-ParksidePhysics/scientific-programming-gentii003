import numpy as np

summation = 0
starting_index = 1
index = starting_index
maximum_index = 100

while index < maximum_index:
    summation += 1/index
    index += 1 #without will run infinte loop

#for loop
#summation = sum(1 / k for k in range(1, 101))
#print(f'sum(k = 1, 100) 1/k = {summation}')

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.6f}')#:.6f for 6 digits after decimal point
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.3f}') #:.nf number of folate digits
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.2f}')

summation = 0
starting_index = 1
index = starting_index
maximum_index = 3

while index < maximum_index:
    summation += 1/index
    index += 1 #without will run infinte loop

#for loop
#summation = sum(1 / k for k in range(1, 4))
#print(f'sum(k = 1, 3) 1/k = {summation}')

print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.6f}')#:.6f for 6 digits after decimal point
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.3f}') #:.nf number of folate digits
print(f'sum(k = {starting_index}, {maximum_index}) 1/k = {summation:.2f}')