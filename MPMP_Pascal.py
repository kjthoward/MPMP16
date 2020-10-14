import math
from matplotlib import pyplot
#function to check if number is odd
def is_odd(number):
    if number%2==0:
        return False
    else:
        return True

odd_count=0
total=0

def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)

def pascals_triangle(rows):
    result = [] # need something to collect our results in

    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result

# stores row number and percentage that's odd
odd_percentage={}

#change number of rows as needed
for row in pascals_triangle(128):
    odds_in_row=0
    for n in row:
        if is_odd(n)==True:
            odd_count+=1
            odds_in_row+=1
        total+=1
    print(f"Row: {len(row)} - {odds_in_row/len(row)*100}")
    odd_percentage[len(row)]=odds_in_row/len(row)*100
    # print(row)
pyplot.figure(figsize=(20,10))
pyplot.title("Percentage of each row in Pascal's Triangle that's odd",fontsize=18)
pyplot.xlabel("Row Number")
pyplot.ylabel("Percentage Odd")
pyplot.plot([x for x in odd_percentage.keys()], [x for x in odd_percentage.values()])
pyplot.show()

