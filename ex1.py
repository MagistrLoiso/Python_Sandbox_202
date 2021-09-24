#Task 1
def is_even(x):
    if x<0:
        print("You've typed negative number!")
    return bool(not x%2)

#Task2
def generate_squares(min_num, max_num):
    l = []
    for i in range(min_num, max_num+1):
        l.append(i**2)
    return l

print (generate_squares(1, 5))

