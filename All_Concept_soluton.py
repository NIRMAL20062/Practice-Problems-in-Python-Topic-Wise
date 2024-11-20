           # Concept-1👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


# Q.Enter a number find it even or odd
""" def check_no():
    num=int(input('Enter a number:'))
    if num%2==0:
        return 'Even'
        # print('even')
    else:
        return "Odd"
        # print("odd")
# check_no()
print(check_no()) """


# # Q. Given two number return larger one

""" def larger():
    x=int(input("Enter a number: "))
    y=int(input("Enter a number: "))
    list=[x,y]
    return max(list)
print(larger()) """



#  Q. temp. is given in ferenhiet F=(C*1.8)+32
#   If temp>90 degree return other wise return false

""" def temp_check(c):
    f=(c*1.8)+32
    return f
print(temp_check(66)) """


# Q. Given a year, return True if it is a leap year, else return False. A leap year is divisible by 4, except for years that are divisible by 100. However, years that are divisible by 400 are also leap years.


""" def leap_year(year):
     if year%4==0:
          if year%400==0:
               if year%100==0:
                  print('Its a leap year')
               else:
                  print("not a leap year")
          else:
              print('Its a leap year')
     
(leap_year(300)) """


# Q.Given two numbers, a and b, return the value of a/b (return None if b is zero).


""" def div(a,b):
    if b!=0:
        print(a/b)
    else:
      print("NONE")
div(4,2)
div(4,0) """


# Q. Given a point (x1, y1), return the quadrant (integer values given below) in which this point lies.
# [0: origin, 1: first quadrant, 2: second quadrant, 3: third quadrant, 4: fourth quadrant, 12: positive y-axis, 23: negative x-axis, 34: negative y-axis, 41: positive x-axis]


""" def quadrant(x,y):
    if x>0 and y>0:
        print("First Quadrant")
    elif x>0 and y<0:
        print("Fourth Quadrant")
    elif x<0 and y<0:
        print("third Quadrant")
    elif x<0 and y>0:
        print("second  Quadrant")
    else:
        print("7th Dimention")

quadrant(2,4)
quadrant(-3,4)
quadrant(2,-4)
quadrant(-2,-4) """


# Q. Given two points (x1, y1) and (x2, y2), return the slope and intercept of the line joining these two points (the line may be perfectly horizontal or vertical). Input should be in this format : (x1, y1, x2, y2).


""" def slope():
 x1=int(input("Enter a number :"))
 y1=int(input("Enter a number :"))
 x2=int(input("Enter a number :"))
 y2=int(input("Enter a number :"))
#  equation: y=slope(x)+c
 slope=(y2-y1)/(x2-x1)
 intercept1=-slope*(-x1)+y1
 print(slope)
 print(intercept1)
slope() """


# Q. Given a quadratic equation with coefficients a, b and c, return the two solutions (may be real or complex). You should not take the square root of a negative number in your code. Output should be a list of two tuples. So if the roots are 1+2j and 1–2j, the output of the function should be [(1,2), (1,-2)]. If the roots are real, then the second part of both the tuples becomes zero.

# a=2
# b=2
# c=7
""" def quad(a,b,c):
# eq=a*x**2+b*x+c
    # x1=b-((b**2-4*a*c)**(.5))/(2*a)
    # x1=b+((b**2-4*a*c)**(.5))/(2*a)
    d=((b**2-4*a*c))
    if d<0:
      print([(b,((b**2-4*a*c)**(.5))/(2*a)),(b,-((b**2-4*a*c)**(.5))/(2*a))] )
    else:
       x1=b-((b**2-4*a*c)**(.5))/(2*a)
       x1=b+((b**2-4*a*c)**(.5))/(2*a)
       print('X1= {x1}','x2={x2}')
(quad(2,4,5))
(quad(2,3,1))  """

# Q. Given three points, return True if they lie on the same straight line, else return False. Input should be in this format : (x1, y1, x2, y2, x3, y3).
""" a=3
b=1
c=4
d=((b**2-4*a*c))
if d < 0:          # checking for real roots
   print([((-b)/(2*a),d/(2*a('j'))) ,((-b)/(2*a),(-d)/(2*a('j')))])
elif d >= 0:
   print([((-b+((b**2-4*a*c)**(.5))/(2*a)),'0') ,(-b-((b**2-4*a*c)**(.5))/(2*a),'0')]) """

""" x1, y1, x2, y2, x3, y3 = map(float, input().split())

if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
    print("A straight line")
elif (x2 - x1) == 0 or (x3 - x2) == 0:
    print("A vertical line")
else:
    print("Not a straight line") """





           # Concept-2  👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


# 1. Given a positive integer, return its factorial.
""" def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    print(fact)  
factorial(5)    """

# 2. Given a positive integer, return True if it’s prime, else return False.
""" def get_prime(x):
    if  x==2:
            return True
    else:        
        for i in  range(2, x):
            if x % i == 0:
                return False
            else:
                return True
print(get_prime(4)) """

""" def check_num(num):
    # prime number divisible by 1 and number itself
    
        if num%2!=0 and num%3!=0:
            if num%1==0 and num%num==0:
                print(num,'Its a Prime Number')
            elif num==2 or num==3:
                 print(num,'Its a Prime Number')
        else:
             print(num,': Not a Prime Number')
        return True
check_num(1) """


# 3. Given a positive integer, return the sum of all integers from 1 up to this number.
""" def sum(num):
    sum=0
    for i in range(0,num+1):
        sum=sum+i
    print(sum)
    return True
sum(5) #5+4+3+2+1 """

# 4. Given a positive integer, return the sum of all odd numbers from 1 up to this number.
""" def sum_odd(num):
    sum=0
    for i in range(1,num+1):
        if i%2!=0:
            sum=sum+i
    return (sum)
print(sum_odd(10)) """  #1+3+5=9  #1+3+5+6=15 #15+7+9+11=35+9

# 5. Given a positive integer greater than 1, return the sum of all even numbers from 2 up to this number.
""" def sum_even(num):
    sum=0
    for i in range(1,num+1):
        if i%2==0:
            sum=sum+i
    print(sum)
sum_even(10) """


# 6. Given a positive integer, return its binary representation (output using integer datatype)
# if int=5 then binary number will be |5| 1
                                  #   |2| 0
                                  #   |1|
                                 #   5=101                                
""" def get_binary(n):
    s=''
    while n>0:
        r=n%2    #storing remainder
        s+=str(r)
        n=int(n/2)
    print(s) 
(get_binary(5)) """

# (output using integer datatype)
""" n=5
s=''
while n>0:
        r=n%2
        s=str(r)+s
        n=(n//2)
print(s)  """

# Given a binary representation of an integer (input using integer datatype), return the corresponding integer value in decimal representation.
# 101 then  5 ,1*(2**0)+0*(2**1)+1*(2**2)=1+0+4=5
""" s = '101'  # Binary string
sum = 0  # Initializing sum
x = len(s)  # Taking the length of the string
for i in range(x, 0, -1):  # Iterating over the loop
    p = int(s[i-1]) * (2 ** (x - i))  # Convert s[i-1] to an integer before multiplication
    sum = sum + p
print(sum)    #5 """

# 8. Given a positive integer, return True if its a palindrome, else return False.
""" def is_palindrome(s):
    # Convert the string to lowercase and remove spaces for accurate comparison
    s = s.replace(" ", "").lower()
    # Compare the string with its reverse
    return s == s[::-1]

# Example usage
word = "radar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome")
else:
    print(f"'{word}' is not a palindrome") """
# (output) 'radar' is a palindrome

# 9. Given a positive integer, return the number of digits in it.
""" import keyword
keyword.help """
""" def return_no_of_digits(num):
            no_of_digits=1 #num=86687
            while num>10:
                x=num//10          #each time reducing digit by 1
                num=x
                no_of_digits+=1    #adding the reduced digits
            return no_of_digits    #retrunig the result
print(return_no_of_digits(763767)) """

""" def check_integer(y):
    y=input('Enter a integer: ')
    if y>=0:
        def return_no_of_digits(num):
            no_of_digits=1 #num=86687
            while num>=10:
                x=num//10          #each time reducing digit by 1
                num=x
                no_of_digits+=1    #adding the reduced digits
            return no_of_digits    #retrunig the result
        # print(return_no_of_digits(76376))
print(check_integer(6567))"""

# 10. Given a positive integer, return the number of even digits in it.
""" def return_no_of_digits(num):
            no_of_digits=1                 #num=86686
            while num>=10:
                for i in num:              #iterating over num
                    if i%2==0:
                        x=num//10          #each time reducing total no. in digit by 1
                        num=x
                        no_of_digits+=1    #adding digits each time 1
            return no_of_digits            #retrunig the result
print(return_no_of_digits(76376))  """

""" def return_no_of_digits(num):
            no_of_digits=1 
            while num>=10:
              num_str=str(num)               # converting into string to iterate
              for i in num_str:              #iterating over num_str
                    digit=int(i)            
                    if i%2==0:
                        x=num//10          #each time reducing total no. in digit by 1
                        num=x
                        no_of_digits+=1    #adding digits each time 1
            return no_of_digits            #retrunig the result
print(return_no_of_digits(76376)) """



           # Concept-3   👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                        #     👍🤔💙🩵💚🫀❤️❤️🩷🧡
                        # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


#1. Given a list of numbers, return its length and the sum of all these numbers.

""" def get_len_sum():
        list=[12,45,75,34]
        sum=0
        print(len(list))
        for i in list:
                # print(i,end=' ')
                sum+=i
        return (sum)
print(get_len_sum()) """



# 2. Given a list of numbers, return a list of the squares of all the numbers.

""" def get_square():
    list=[11,5,2,4,]
    new_list=[]
    for i in list:                    #iterating on list
        square=i*i
        new_list.append(square)     #appending in new list
    return new_list
print(get_square()) """


# 3. Given a list of numbers, return their mean and standard deviation.

# mean = total_sum/total no.
# standard_deviation = root[(summission_of(x-xbar)**2)/(total_num-1)] , x=mean
""" list1=[2,44,63,22,3]
def get_mean_std_dev():
    def get_mean():
        return ((sum(list1))/(len(list1)))
    def get_std_dev():
        variance=sum((x-get_mean())**2 for x in list1)/(len(list1)-1)
        return (variance)**(.5)
    return ('Mean is: ' ,get_mean()),('Standard Deviation is: ', get_std_dev())
print(get_mean_std_dev()) """


# 4. Given a list of integers, return the count of even numbers in it.

""" def count_even_no():
    list=[12,44,3,7,42,43,10]
    count_even_no=0
    for i in list:
        if i%2==0:
            count_even_no+=1
    return count_even_no
print(count_even_no()) """


# 5. Given a list of numbers, return the list in reverse order (without using list splicing).

""" def reverse_order_list():
    list1=[12,556,7,32,33]
    x=len(list1)                       #x=5
    new_list=[]
    for i in range(x):
        new_list.append(list1[x-1-i])    # to get last index and substract -1 each time 33,32,7,556,12
    return (new_list)
print(reverse_order_list()) """

# 6. Given a list of numbers, return the maximum number in it.

""" def max_in_list():
    list=[12,5,9,55,7,3]
    max=0
    for i in list:
        if max<=i:
            max=i
    return max
print(max_in_list()) """

# 7. Given a list of integers and another integer, return the index of this given integer.

# METHOD-1

""" def get_index():
    list1=[23,67,2,6,9,6]
    target=6
    for i in range(len(list1)):
        if list1[i]==target:
            return i
        
print(get_index()) """

# METHOD-2

""" def get_index():
    list1=[23,67,2,6,9]
    target=6
    for index,ele in enumerate(list1):
        if ele==target:
        #    print(index)
             return index
    return -1
print(get_index()) """

# 8. Given a list of integers, return their Least Common Multiple (LCM).

""" def get_least_common_multiple(numbers):
    Calculates the least common multiple of a list of numbers.

    Args:
        numbers: A list of integers.

    Returns:
        The least common multiple of the numbers in the list.

    lcm = 1
    for num in numbers:
        max_val = max(lcm, num)
        while True:
            if max_val % lcm == 0 and max_val % num == 0:
                break
            max_val += 1
        lcm = max_val
    return lcm
# Example usage
list1 = [2, 4, 7]
result = get_least_common_multiple(list1)
print("Least common multiple:", result) """


# MEthod-2
# x=12
# y=30
""" def get_hcf(x,y):
    
        smaller = y
    else:
        smaller=x
        for i in range(1,smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf
get_hcf(12,30) """


# 9. Given a list of integers, return their Greatest Common Divisor (Divisor).
# hcf=gcd
# x=12
# y=30
""" def get_hcf(x,y):
    if x>y:
        smaller = y
    else:
        smaller=x
        for i in range(1,smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf
get_hcf(12,30) """





# 10. Given a positive integer (n), return a list containing the first n integers in the Fibonacci series.

# FS-0,1,1,2,3,5,8
""" sum=0
list=[0,1]
for i in range(10):
    sum=list[i]+list[i+1]
    list.append(sum)
print(list) """

""" list2=[2,4,6,3,6]
list1=[]
for i in range(len(list2)-1):   #i=0,1,2,3,4
    for j in range(len(list1)-1):    #i=0,1,2,3,4
        sum=list2[i]+list2[j]         #when i=0 j=0 to 4
        list1.append(sum)
print(list1) """

""" list2=[2,4,6,3,6]
list1=[]
for i in list2:
    for j in list2:
        sum=i+j
        list1.append(sum)
print(list1) """



         # Concept-4 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                    #  👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                    # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


# 1. Given a list of distinct numbers, return another list which contains the sum of all pairs of numbers in the given list (the same pair should not be taken twice).
""" def give_list():
    list1 = [1, 4, 6, 7, 9, 4]
    new_list1 = []
    for i in list1:
        for j in list1:
            if i != j:  # avoid duplicate pairs
                sum = (i + j)
                new_list1.append(sum)
    return new_list1
print(give_list()) """


# 2. Given a list of distinct numbers (may contain zero), return another list which contains the ratio of all pairs of numbers in the given list (the same pair should not be taken twice).
def give_list():
    list1 = [1, 4, 6, 7, 9, 4]
    new_list1 = []
    for i in list1:
        for j in list1:
            if i != j:  # avoid duplicate pairs
                ratio = i / j if j != 0 else float('inf')  # avoid division by zero
                new_list1.append(ratio)
    return new_list1
print(give_list())

# 3. Given a list of positive integers, return a list of the factorial of all these numbers.
""" def get_factorial():
    list1=[2,3,4,5,6]
    f=1
    list2=[]
    for i in (list1):
        fact=1
        while i>0:
             fact=fact*i
             i=i-1
        list2.append(fact)
    return list2
print(get_factorial())   # 2,6,24,120,720 """

# 4. Given a positive integer, return a list of all prime numbers from 1 up to this number.
""" def get_pn():
    start=11
    end=10+10
    for i in range(start,end+1):
            flag=1       #indicating prime no.
            for j in range(2,i):
                  if i % j == 0:
                     flag=0     #indicating not a prime no.
                     break
            if flag==1:
                 print(i,end=' ')
get_pn() """

""" def get_prime(x):
    if x==2:
            return True
    else:        
        for i in  range(2, x):
            if x % i == 0:
                return False
            else:
                return True
print(get_prime(4)) """

# 5. Given a positive integer, return the sum of all prime numbers from 1 up to this number.
""" def get_pn():
    start=11
    end=10+10
    sum=0
    for i in range(start,end+1):
            flag=0       #indicating prime no.
            for j in range(2,i):
                  if i % j == 0:
                     flag=1     #indicating not a prime no.
                     break
            if flag==0:
                 print(i,end=' ')
                 sum=sum+i
    print()            
    c='sum is:',sum
    print(c)
get_pn()     #11+13+17+19 """

# 6. Given a list of numbers, return another list of co-primes and count how many co-primes are there in this given list.
# hcf should be 1
""" def get_co_prime():
    list = [2, 3, 4, 5, 6, 7, 8]
    list1 = []
    # co-prime=(2,3),(2,5),(2,7) || (3,4),(3,5),(3,7),(3,8) || (4,5),(4,7)
    for i in range(len(list)):  # i=0,1,2,3,4,5,6
        for j in range(i + 1, len(list)):  # j starts from i+1 to avoid duplicate pairs
            # finding GCD
            smaller = min(list[i], list[j])  # Get the smaller of the two numbers
            hcf = 1  # Initialize hcf to 1
            for k in range(1, smaller + 1):
                if (list[i] % k == 0) and (list[j] % k == 0):
                    hcf = k  # Update hcf if k is a common divisor
            if hcf == 1:  # If hcf is 1, they are co-prime
                l = (list[i], list[j])
                list1.append(l)  # Store the co-prime pair in list1
    return list1  # Print all co-prime pairs
get_co_prime() """

# Method-2

""" def get_co_prime():
    list = [2, 3, 4, 5, 6, 7, 8]
    co_primes = []  # List to store co-prime pairs
    count = 0       # Counter for co-prime pairs

    # Iterate through each unique pair in the list
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            # Finding GCD
            a, b = list[i], list[j]
            smaller = min(a, b)
            hcf = 1  # Initialize hcf to 1
            for k in range(1, smaller + 1):
                if (a % k == 0) and (b % k == 0):
                    hcf = k  # Update hcf if k is a common divisor
            if hcf == 1:  # If hcf is 1, they are co-prime
                co_primes.append((a, b))  # Store the co-prime pair
                count += 1  # Increment the count
    return co_primes, count  # Return the list of co-prime pairs and their count

# Example usage
co_prime_pairs, co_prime_count = get_co_prime()
print("Co-prime pairs:", co_prime_pairs)
print("Count of co-prime pairs:", co_prime_count) """

#Q7. Given two 2D matrices of the same dimensions, return their sum.
""" matrix1=[[2,3,4],
         [5,6,7]]
matrix2=[[8,9,10],
         [11,12,13]]
# print((matrix1[0]))  #[2,3,4]
# print(len(matrix1[0])) #3
# print(matrix1[1][1])
result=[]
for i in range(len(matrix1)):  # i = 0,1   #Row per iterate kiya
    row=[]
    for j in range(len(matrix1[0])): # J = 0,1,2    #column per kiya
        x=(matrix1[i][j]+matrix2[i][j])
        row.append(x)
    result.append(row)
print(result) """

""" matrix1 = [[2, 3, 4],
            [5, 6, 7]]
matrix2 = [[8, 9, 10],
            [11, 12, 13]]
# print(len(matrix1)) # 2 
# Create a new matrix to store the result
result = []
# Iterate through the rows
print("Sum of matrices:")
for i in range(len(matrix1)): #i=0,1
    # Create a new row for the result
    row = []
    # Iterate through the columns
    for j in range(len(matrix1[0])): #matrix1[0]=[2,3,4] so j=0,1,2
        # Add the corresponding elements
        row.append(matrix1[i][j] + matrix2[i][j])
    # Append the new row to the result matrix
    result.append(row)
    print(row) """

# 8. Given a list of integers, sort it on your own and return the median.
# get median
""" list1=[1,4,6,8,3,9,3,10]
list1.sort()
print(list1)  #[1, 3, 3, 4, 6, 8, 9,10]
x=int(len(list1))  #x=7
if x/2==0:
    median=int((list1[x-1]+list1[x]))/2  # 
else:
    median=list1[int((x)/2)]   #3
print(median) """

""" def selection_sort(arr):
    n = len(arr)
    # Implementing selection sort
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def find_median(arr):
    # Sort the array
    sorted_arr = selection_sort(arr)
    n = len(sorted_arr)
    
    # Calculate the median
    if n % 2 == 0:
        # If even, return the average of the two middle numbers
        median = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
    else:
        # If odd, return the middle number
        median = sorted_arr[n//2]
    
    return median

# Example usage
numbers = [1, 4, 6, 8, 3, 9, 3]
median_value = find_median(numbers)
print("Median:", median_value) """

# 9. Given a list of integers, return its mode (list of numbers with highest frequency of occurrence). Do not use a dictionary.

""" lists=[1,4,6,3,4,7,3,3,3,3]
lists.sort()
list1=[]
# print(lists)   # [1, 3, 3, 3, 4, 4, 6, 7]
for i in lists:
    x=lists.count(i)
    lists.remove(i)
    list1.append([x,i])
print(max(list1)) """

# 10 . Given a list of lists of integers, return a list that is sorted based on the sum of each inner list. Do not use any inbuilt function for sorting.
""" def selection_sort_by_sum(list_of_lists):
    n = len(list_of_lists)    # n=3
    # Implementing selection sort based on the sum of inner lists
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            # Compare the sums of the inner lists
            if sum(list_of_lists[j]) < sum(list_of_lists[min_index]):
                min_index = j
        # Swap the found minimum element with the first element
        list_of_lists[i], list_of_lists[min_index] = list_of_lists[min_index], list_of_lists[i]

    return list_of_lists

# Example usage
lists = [[3, 5, 1], [2, 2], [4, 0, 1], [1, 2, 3]]
sorted_lists = selection_sort_by_sum(lists)
print("Sorted list based on the sum of inner lists:")
for inner_list in sorted_lists:
    print(inner_list) """


              # Concept-5 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                            # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                            # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
   
#Q 1. Given two lists of the same length as input, return a dictionary with keys taken from the first list and values from the second list. If the list sizes are different, consider the length of the shorter one for creating the dictionary.
""" 
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict1={}
def lists_to_dict(keys, values):
    length = min(len(keys), len(values))  # Determine the length of the shorter list
    # return {keys[i]: values[i] for i in range(length)}  # Create the dictionary
    for i in range(length):
        dict1[keys[i]]=values[i]
    return dict1
print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}


keys = ['a', 'b', 'c']
values = [1, 2, 3]
def lists_to_dict(keys, values):
    length = min(len(keys), len(values))  # Determine the length of the shorter list
    return {keys[i]: values[i] for i in range(length)}  # Create the dictionary

print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3}
 """

# Q2. Given two dictionaries, merge them and return a single dictionary.

""" 
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    merged_dict.update(dict2)    # Update with the second dictionary
    return merged_dic
print(merge_dicts(dict1, dict2))  # Output: {'a': 1, 'b': 3, 'c': 4}which
 """

#Q3 . Given a dictionary and a key, return True if the key is present in the dictionary, else return False.
""" my_dict = {'a': 1, 'b': 2, 'c': 3}
key='bg'
def dict2():
    if key in my_dict:
        return True
    else:
        return False
print(dict2()) """
# Q4 . Given a dictionary and a list of keys, return another dictionary only has the keys given in the input list, and values taken from the input dictionary.

""" keys = ['a', 'e', 'c', 'd']
dict1 = {'e': 1, 'f': 2, 'g': 3, 'h': 4}
dict2 = {}

def lists_to_dict(keys, dict1):
    
    for i in range(len(keys)):  # include all keys i=0,1,2,3
      if keys[i] in dict1:
        dict2[keys[i]]=dict1[keys[i]] #direct assign
        # dict2[keys[i]] = dict1.get(keys[i], None)  # safely access dict1
    return dict2

result = lists_to_dict(keys, dict1)
print(result) """

""" keys=['a','b','c','d']
dict1={'e':1,'f':2,'g':3,'h':4}
dict2={}
def lists_to_dict(keys, dict1):
    for i in range(len(keys)):
        dict2[keys[i]]=dict1.get(keys[i])
    return dict2
print(lists_to_dict(keys,dict1)) """

""" dict1={'e':1,'f':2,'g':3,'h':4}
for i in dict1:
    print(dict1[i])
    # print(i)
 """


# Q5. Given a dictionary, return the inverted dictionary, i.e. keys of the output dictionary are the values of the input dictionary, and values of the output dictionary are the keys of the input dictionary.

""" dict1={'a':1,"b":2,"c":3}
inv_dict1={}
# print(dict1.keys())
# print(dict1.values())
# for i in dict1:
#     print(i)   #a,b,c
#     print(dict1[i])  #1,2,3
for i in dict1:
    inv_dict1[dict1[i]]=i
    # inv_dict1[dict1[i]]
print(inv_dict1)
    # print(dict1.values())
    # dict1.values() """

""" # 6. Given a dictionary containing the student names as keys and list of marks in 3 subjects as the dictionary values, return a list containing the average marks for each subject.

dict1={"a":[15,20,25],"b":[30,35,40],"c":[45,50,55]}
list1=[]
for value in dict1:
    x=(dict1[value])
    sum=0
    for i in x:
         sum=sum+i
    avg=sum/3
    list1.append(avg)
print(list1)   #20,35,40 """

# Q7. Given a dictionary containing the student names as keys and list of marks in 3 subjects as the dictionary values, return a dictionary where the keys are the student names and values are the student CGPA. Above 80 marks is A grade with 10 grade points, 60–80 marks is B grade with 8 grade points, 40–60 marks is C grade with 6 grade points, and below 40 is F with 0 grade points. Course1 is of 4 credits, Course2 of 10 credits, and Course3 of 6 credits.



# Q8 . Given a fruit name and a dictionary whose keys are people names and the values are the list of fruits they like, return the list of names of people who like this fruit.

""" fruits='banana'
dict1={'ram':["apple",'banana','pineapple'],"shayam":['banana','pineapple','litchi'],"veer":['pineapple','Mango',"guava"]}
list1=[]
for people in dict1:
    if fruits in dict1[people]:
        list1.append(people)
print(list1) """


# Q 9. Given a list of integers, return its mode (list of numbers with highest frequency of occurrence) by using a dictionary in your code

""" list1=[1,3,5,7,6,3,8,3,5,2,3,5,2,3]
# mode =3
dict1={}
for i in list1:
 """


# Q 10 . Given a text file with one word in each line, return a dictionary where the key is the word and the value is the number of times it occurs in the text file.

# text_file=8


              # Concept-6     👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                           # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                           #👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                           #👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


# Given a string as input, return its length without using the inbuilt length function.
""" len1=0
string='To take new keys'
# print(len(string))
for ele in string:
    len1+=1
print(len1) """


# Given a string as input, return the string in reverse order (without using string splicing).
""" string='To take new keys'
new_str=[' ']
for ele in range(1,len(string)+1):
    str1=string[len(string)-ele]
    # new_str.append(str1)
    print(str1,end='')
 """

# Given a string as input, return the number of vowels in it.
""" string='To take new keys aa'
list1=['a','e','i','o','u']
list2=[]
# string.isupper()
# print(string)
for ele in range(len(string)):
    for j in range(len(list1)):
        if string[ele]==list1[j]:
            list2.append(string[ele])
            x=len(list2)
print(x) """

# Given a string as input, return the number of words in it. Use space as a separator for words.

# string='To take new keys'


# Given a string as input, return the string with the first letter of each word capitalised.
""" string='To take new keys'
x=string.capitalize()
y=string.title()
print(x)
print(y) """


# Given a string as input, return the length of the longest word in it. Use space as a separator for words.
""" import re
string='To takee new keys'
x=re.split('\s',string)
print(x)          #['To', 'tak', 'new', 'key']
max=len(x[0])
for ele in (x):
        if max<=len(ele):
            max=len(ele)
print(max) """


# Given a string as input, return True if its a valid email address, else return False.
""" import re
string='hello my mail is  kumar.nirmal2608@gmail.com and nirk383@outlook.com '
x=re.search('^([a-z]|[0-9]+@(gmail.com))',string)
x=re.search(r"\@......com",string)
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
print(x)
print(pattern,string) """

# Given a string as input, return True if its a valid mobile number in India, else return False.
""" import re
string='hello boy\'s my number is 123123213 and `1231232442'
x=re.search('[0-9]{9}',string)
print(x) """


# Given a string as input, return True if its a palindrome, else return False (case sensitive and ignore spaces). Do not use string splicing.
# import re
# string='iitii'
# k=(len(string))
# x= re.findall(r'[a-zA-Z]', string)
# print(x)      
# for word in range(len(string)):
#     if x[word]==x[k-word]:

#        print('its a pelindrome')








# Split the string between each character using a regular expression
""" result = re.split(r'()', string)

# Manually filter out the empty strings (instead of shorthand)
filtered_result = []
for char in result:
    if char != '':
        filtered_result.append(char)

print(filtered_result) """