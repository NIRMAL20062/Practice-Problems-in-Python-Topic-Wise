           # Concept-1👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


#1Q.Enter a number find it even or odd
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


#2Q. Given two number return larger one

""" def larger():
    x=int(input("Enter a number: "))
    y=int(input("Enter a number: "))
    list=[x,y]
    return max(list)
print(larger()) """



#3Q. temp. is given in ferenhiet F=(C*1.8)+32
#   If temp>90 degree return other wise return false

""" def temp_check(c):
    f=(c*1.8)+32
    return f
print(temp_check(66)) """


#4Q. Given a year, return True if it is a leap year, else return False. A leap year is divisible by 4, except for years that are divisible by 100. However, years that are divisible by 400 are also leap years.
# year should be divisible by 4 , but not by 100, unless it is also divisible by 400.

""" def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
print(leap_year(2000)) """



""" def leap_year(year):
     if year%4==0:
          if year%100==0:
               if year%400==0:
                  return('Its a leap year')
               else:
                  return("not a leap year")
          else:
              return('Its a leap year')
(leap_year(300)) """


# Q.Given two numbers, a and b, return the value of a/b (return None if b is zero).

""" def div(a,b):
    if b!=0:
        return(a/b)
    else:
      return None
print(div(4,2))
print(div(4,0)) """


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

""" # Q9. Given three points, return True if they lie on the same straight line, else return False. Input should be in this format : (x1, y1, x2, y2, x3, y3).
def are_points_collinear(x1, y1, x2, y2, x3, y3):
    # Calculate the area of the triangle formed by the three points
    # Area formula: 0.5 * |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)|
    # If the area is zero, the points are collinear
    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return area == 0

# Example usage
print(are_points_collinear(1, 1, 2, 2, 3, 3))  # True
print(are_points_collinear(1, 1, 2, 2, 3, 4))  # False
 """





           # Concept-2  👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


# 1. Given a positive integer, return its factorial.
""" def factorial(num):
    fact=1
    while num>0:
        fact=fact*num
        num=num-1
    return(fact)  
print(factorial(5)) """   

# 2. Given a positive integer, return True if it’s prime, else return False.
""" def get_prime(x):
    if  x<2:
            return False
    elif x==2:
            return True
    else:        
        for i in  range(2, x):
            if x % i == 0:
                return False
        else:
            return True
print(get_prime(5)) """


# 3. Given a positive integer, return the sum of all integers from 1 up to this number.
""" def sum(num):
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    return sum
print(sum(5)) #5+4+3+2+1 =15 """

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
                                  #5=101
""" def get_binary(n):
    s=''
    while n>0:
        r=n%2   #storing remainder
        n=int(n/2)
        s+=str(r)
    # reversed_s = ''.join(reversed(s))
    # print(reversed_s)
    str1=''
    for ele in range(1,len(s)+1):  #ele=1,2,3
            str1=str1+s[len(s)-ele]
    print(str1)
(get_binary(8)) """

""" def get_binary(n):
    s = ''
    binary = 0
    place = 1  # Represents the place value in binary (units, tens, hundreds, etc.)
    
    while n > 0:
        r = n % 2  # Get the binary digit (remainder)
        binary += r * place  # Add it to the result at the correct place value
        n = n // 2  # Integer division to reduce the number
        place *= 10  # Move to the next binary place value
    
    return binary  # Return the result as an integer

# Example usage
print(get_binary(8))  # Output: 1000 """

""" def get_binary(n):
    if n == 0:
        return 0  # Special case for zero
    s = ''
    while n > 0:
        r = n % 2  # Get remainder (binary digit)
        n = n // 2  # Reduce the number using integer division
        s += str(r)  # Append remainder as a string
    # Reverse the constructed string to get the correct binary representation
    reversed_s = ''.join(reversed(s))
    return int(reversed_s)  # Convert the reversed string to an integer
# Example usage
print(get_binary(1))  # Outputs: 0
print(get_binary(8))  # Outputs: 1000
print(get_binary(5))  # Outputs: """ 

#Q7. Given a binary representation of an integer (input using integer datatype), return the corresponding integer value in decimal representation.
# 101 then  5 ,1*(2**0)+0*(2**1)+1*(2**2)=1+0+4=5
""" s = '1000'  # Binary string
sum = 0  # Initializing sum
x = len(s)  # Taking the length of the string
for i in range(x, 0, -1):  # Iterating over the loop
    p = int(s[i-1]) * (2 ** (x - i))  # Convert s[i-1] to an integer before multiplication
    sum = sum + p
print(sum)    #5 """

""" s = '1000'  # Binary string
sum = 0  # Initializing sum
x = len(s)  # Taking the length of the string
for i in range(x):  # Iterating over the loop
    p=int(s[i])*2**(x-1-i)  # Convert s[i-1] to an integer before 
    sum = sum + p
print(sum)    #8 """

# 8. Given a positive integer, return True if its a palindrome, else return False.

""" def pel(n):
    str1 = str(n)  # Convert the number to a string
    x = len(str1)  # Get the length of the string
    for i in range(x // 2):  # Loop only through half the string
        if str1[i] != str1[x - 1 - i]:  # Compare characters from both ends
            return False  # Return False if any mismatch is found
    return True  # If the loop completes, it is a palindrome
print(pel(1231))  # Outputs: False
print(pel(121))   # Outputs: True
print(pel(0))     # Outputs: True """


""" def x():
    str1="rdar"
    str1.lower()
    left=0
    right=len(str1)-1
    while left<right:
        if str1[left]!=str1[right]:
            return ('not pelindrome')
        left+=1
        right-=1
    return('a pelin')
print(x()) """


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

# 9. Given a positive integer, return the number of digits in it.

""" def return_no_of_digits(num):
    if num == 0:
        return 1  # Special case for 0
    no_of_digits = 0
    while num > 0:   #num=86687
        num = num // 10   #each time reducing digit by 1
        no_of_digits += 1  #adding the reduced digits
    return no_of_digits   #retrunig the result
print(return_no_of_digits(103767)) """


# 10. Given a positive integer, return the number of even digits in it.
# NOTE: Cool problem!
# x=09948

""" num=9856420
x=str(num)
sum=0
for i in x:
    if int(i)%2==0:
        sum+=1
print(sum) """


           # Concept-3   👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                        #     👍🤔💙🩵💚🫀❤️❤️🩷🧡
                        # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛

#1. Given a list of numbers, return its length and the sum of all these numbers.

""" def get_len_sum(list):
        sum=0
        length=0
        for i in list:
                sum+=i
                length+=1
        return f"sum is {sum},length is { length}"
print(get_len_sum([12,45,75,34])) """

# 2. Given a list of numbers, return a list of the squares of all the numbers.

""" def get_squares(list1):
    squares=[]
    for i in list1:
        squares.append(i**2)
    return squares
print(get_squares([12,45,75,34])) """


# 3. Given a list of numbers, return their mean and standard deviation.

# mean = total_sum/total no.
# standard_deviation = root[(summission_of(x-xbar)**2)/(total_num-1)] , x=mean

""" list1 = [2, 44, 63, 22, 3]
def get_mean_std_dev():
    def get_mean():
        return sum(list1) / len(list1)
    mean = get_mean()  # Calculate mean once and store it
    def get_std_dev(mean):
        variance = sum((x - mean) ** 2 for x in list1) / (len(list1) - 1)
        return variance ** 0.5
    std_dev = get_std_dev(mean)  # Pass mean to std_dev calculation
    return f'Mean is: {mean}, Standard Deviation is: {std_dev}'
print(get_mean_std_dev()) """


""" list1 = [2, 44, 63, 22, 3]
def get_mean_std_dev():
    mean = sum(list1) / len(list1)
    # variance = sum((x - mean) ** 2 for x in list1) / (len(list1) - 1)
    sum1=0
    for x in list1:
        sum1=((x - mean) ** 2)+sum1
    x=sum1/(len(list1) - 1)
    std_dev = x ** 0.5
    return f'Mean is: {mean}, Standard Deviation is: {std_dev}'
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

""" def get_max(list):
    max=list[0]
    for i in list:
        if i>max:
            max=i
    return max
print(get_max([1,2,3,4,5,6.6,9])) """




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

""" def get_index(list1,target=6):
    for i in range(len(list1)):
        if list1[i]==target:
            return i
print(get_index([23,67,2,6,9,6])) """

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
    lcm = 1
    for num in numbers:
        max_val = max(lcm, num)
        while True:
            if max_val % lcm == 0 and max_val % num == 0:
                break
            max_val += max(lcm, num)  # Increment by larger value for efficiency
        lcm = max_val
    return lcm

# Example usage
list1 = [2, 3,7]
result = get_least_common_multiple(list1)
print("Least common multiple:", result) """

""" def lcm1(a,b):
    if a >b:
        greater=a
    else:
        greater=b
    while True:
        if ((greater % a == 0) and (greater % b == 0)):
            lcm=greater
            break
        else:
            greater+=1
    return lcm
print(lcm1(12,14))
 """

# MEthod-2
# x=12
# y=30

# 9. Given a list of integers, return their Greatest Common Divisor (Divisor).
""" def gcd(a, b):
    # Compute GCD of two numbers using the Euclidean Algorithm.
    while b != 0:
        a, b = b, a % b
    return a
def find_gcd_of_list(numbers):
    #Compute GCD of a list of integers without slicing.
    if not numbers:
        return 0  # Handle empty list case
    current_gcd = numbers[0]  # Start with the first number
    for i in range(1, len(numbers)):  # Explicitly iterate from the second element
        current_gcd = gcd(current_gcd, numbers[i])
        if current_gcd == 1:  # Early exit, as GCD of 1 is the smallest possible
            break
    return current_gcd
# Example usage
list1 = [3, 7, 2]
result = find_gcd_of_list(list1)
print("Greatest common divisor:", result)  # Outputs: 3 """

# 10. Given a positive integer (n), return a list containing the first n integers in the Fibonacci series.

# FS-0,1,1,2,3,5,8
""" n=10
sum=0
list=[0,1]
for i in range(n+1):
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

""" def pair_sums(list1):
    list2 = []  # Initialize the result list
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):  # Ensure j > i to avoid duplicate pairs
            list2.append(list1[i] + list1[j])  # Compute and add the sum of the pair
    return list2
# Example usage
print(pair_sums([1, 2, 3, 4, 5])) """

""" def sum(list1):
    list2=[]
    for i in list1:
        for j in list1:
            if i!=j:  # after this also code is not correct it will take 2,1 and 1,2
                list2.append(i+j)
    return list2
print(sum([1,2,3,4,5])) """
# Output: [3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13, 14, 15] """

#Q2. Given a list of distinct numbers (may contain zero), return another list which contains the ratio of all pairs of numbers in the given list (the same pair should not be taken twice).

# wrong code on pytutor
""" def get_ratio(list1):
    list2 = []
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):  # ensure each pair is taken only once
            if list1[j] != 0:  # avoid division by zero
                list2.append(list1[i] / list1[j])  # calculate ratio for the pair (i, j)
    return list2
print(get_ratio(list1 = [1, 4, 6, 7, 9, 4]))
# Output: [0.25, 0.6666666666666666, 0 .5, 0.42857142857142855, 0.444444444444 4444, 1.0] """

# 3. Given a list of positive integers, return a list of the factorial of all these numbers.
""" def get_fact(list1):
    list2=[]
    for i in range(len(list1)):
        fact=1
        for j in range(1,list1[i]+1):
            fact=fact*j
        list2.append(fact)
    return list2
print(get_fact([3,6,7,5])) """


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

""" def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True


# 5. Given a positive integer, return the sum of all prime numbers from 1 up to this number.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:  # If n is divisible by any number, it's not prime
            return False
    return True
def find_primes(n):
    sum=0
    for num in range(2, n + 1):  # Check numbers from 2 to n
        if is_prime(num):  # If the number is prime, add it to the list
            sum+=num
    return sum
# Example usage
n = 30
print(find_primes(n))

n=6
sum=0
for i in range(2,n+1):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag:
        sum+=i
print(sum) """

# 6. Given a list of numbers, return another list of co-primes and count how many co-primes are there in this given list.

""" def gcd(a, b):
    # Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime_with_all(num, lst):
    # Check if `num` is co-prime with all numbers in the list
    for x in lst:
        if gcd(num, x) != 1:
            return False
    return True

def find_coprimes(lst):
    coprime_list = []
    for i in lst:
        # Exclude the current number from the rest of the list
        others = []
        for x in lst:
            if x != i:
                others.append(x)
        
        # Check if the current number is co-prime with all other numbers
        if is_coprime_with_all(i, others):
            coprime_list.append(i)
    
    # Return the list of co-prime numbers and their count
    return coprime_list, len(coprime_list)

# Example usage
numbers = [6, 35, 13, 20, 8]
coprimes, count = find_coprimes(numbers)
print("Coprime numbers:", coprimes)
print("Number of co-primes:", count) """

""" def gcd(a, b):
    # Euclidean algorithm to find the GCD
    while b != 0:
        a, b = b, a % b
    return a

def find_coprimes(lst):
    coprime_list = []  # List to store co-prime numbers
    for i in range(len(lst)):
        is_coprime = True  # Flag to check if the current number is co-prime with all others
        for j in range(len(lst)):
            if i != j:  # Do not compare the number with itself
                if gcd(lst[i], lst[j]) != 1:  # If GCD is not 1, they are not co-prime
                    is_coprime = False
                    break  # No need to check further if a non-co-prime pair is found
        if is_coprime:
            coprime_list.append(lst[i])  # Add to the list if it's co-prime with all others

    return coprime_list, len(coprime_list)

# Example usage
numbers = [6, 35, 13, 10]
coprimes, count = find_coprimes(numbers)
print("Coprime numbers:", coprimes)
print("Number of co-primes:", count) """



""" def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def find_coprime_pairs(lst):
    coprime_pairs = []  # List to store pairs of co-prime numbers

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  # Compare each pair only once
            if gcd(lst[i], lst[j]) == 1:  # If GCD is 1, they are co-prime
                coprime_pairs.append((lst[i], lst[j]))  # Add the pair to the list

    return coprime_pairs, len(coprime_pairs)

# Example usage
numbers = [6, 35, 13, 10]
coprime_pairs, count = find_coprime_pairs(numbers)
print("Coprime pairs:", coprime_pairs)
print("Number of co-prime pairs:", count) """

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
result=[]
for i in range(len(matrix1)):  # i = 0,1   #Row per
    row=[]
    for j in range(len(matrix1[0])):
        sum1=matrix1[i][j]+matrix2[i][j]
        row.append(sum1)
    result.append(row)
print(result) """

#Q8. Given a list of integers, sort it on your own and return the median.
""" def bubble_sort(numbers):
    n = len(numbers) #5
    for i in range(n - 1):  # Number of passes # i=0
        for j in range(n - i - 1):  # Compare adjacent elements 
            if numbers[j] > numbers[j + 1]:  # Swap if out of order 64>34
                # Swap if the element found is greater than the next element
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]  # 64 34 = 34 64
    return numbers
# Example usage
list1 = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(list1)
print("Sorted list:", sorted_list)
x = len(list1)  # Length of the list
# Check if the list length is even
if x % 2 == 0:
    # Median is the average of the two middle numbers
    median = (list1[x // 2 - 1] + list1[x // 2]) / 2
else:
    # Median is the middle element
    median = list1[x // 2]
print("Median:", median) """

""" list1 = [1, 4, 6, 8, 3, 9, 3, 10]
list1.sort()
print(list1)  # Sorted list: [1, 3, 3, 4, 6, 8, 9, 10]
x = len(list1)  # Length of the list
# Check if the list length is even
if x % 2 == 0:  
    # Median is the average of the two middle numbers
    median = (list1[x // 2 - 1] + list1[x // 2]) / 2
else:
    # Median is the middle element
    median = list1[x // 2]
print("Median:", median) """

#Q9. Given a list of integers, return its mode (list of numbers with highest frequency of occurrence). Do not use a dictionary.

""" def get_mode(numbers):

    unique_numbers=[]
    for num in numbers:
        if num  not in unique_numbers:
            unique_numbers.append(num)
    
    counts=[]
    for number in unique_numbers:
        count=0
        for num in numbers:
            if num==number:
                count+=1
        counts.append(count)

    max_count=counts[0]
    for i in range(len(counts)):
        if counts[i]>max_count:
            max_count=counts[i]

    mode=[]
    for i in range(len(unique_numbers)):
        if counts[i] == max_count:
            mode.append(unique_numbers[i])  # Add the number if its count is maximum
    return mode
# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,0]
print(get_mode(numbers))  # Output: [4] """

""" def find_mode(numbers):
    # Step 1: Find unique elements in the list
    unique_numbers = []  # To store unique elements
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)  # Add only if not already present
    # Step 2: Count the occurrences of each unique element
    counts = []  # To store counts of each unique number
    for unique_num in unique_numbers:
        count = 0  # Initialize count for the current number
        for num in numbers:
            if num == unique_num:
                count += 1  # Increment count if it matches the unique number
        counts.append(count)  # Store the count for this unique number
    # Step 3: Find the maximum frequency
    max_count = counts[0]  # Assume the first count is the maximum initially
    for count in counts:
        if count > max_count:
            max_count = count  # Update max_count if a higher frequency is found
    # Step 4: Find all elements with the maximum frequency
    mode = []  # To store elements with the maximum frequency
    for i in range(len(unique_numbers)):
        if counts[i] == max_count:
            mode.append(unique_numbers[i])  # Add the number if its count is maximum
    return mode
# Example usage:
numbers = [4, 6, 2, 4, 3, 6, 1, 4, 6, 2, 2]
print("Mode:", find_mode(numbers))
# this method ensures that if more than one number repeates same time and is the most frequent, it will return all of them. """


# method-2
""" lists=[1,4,6,3,4,7,3,3,3,3]
list1=[]
max_count = 0
max_num = None
for i in set(lists):
    x=lists.count(i)
    lists.remove(i)
    list1.append((f'{i} Occured {x} Times'))
    if x > max_count:
        max_count = x
        max_num = i
print(list1)
print(f'Mode is : {max_num}') """

# 10 . Given a list of lists of integers, return a list that is sorted based on the sum of each inner list. Do not use any inbuilt function for sorting.

""" def sort_based_on_sum(lists):
    for i in range(len(lists)):
        for j in range(len(lists) - 1):
            if sum(lists[j]) > sum(lists[j + 1]):
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists
print(sort_based_on_sum([[6,6],[2,6],[5,6],[4,6]])) """

""" def sort_based_on_sum(lists):
    for i in range(len(lists)):
        for j in range(len(lists)-i - 1):
            if sum(lists[j]) > sum(lists[j + 1]):
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists
print(sort_based_on_sum([[6,6],[2,6],[5,6],[4,6]])) """


""" def sort_based(lists):
    for i in range(len(lists)-1):
        for j in range(len(lists)-i- 1):
            if (lists[j]) > (lists[j + 1]):
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists
print(sort_based([8,5,3,6,2])) """

              # Concept-5 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                            # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                            # 👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
   
#Q 1. Given two lists of the same length as input, return a dictionary with keys taken from the first list and values from the second list. If the list sizes are different, consider the length of the shorter one for creating the dictionary.

""" list1=['a','b']
list2=[1,2]
dict1={}
for i in range(min(len(list1),len(list2))):
    dict1[list1[i]]=list2[i]
print(dict1) """

""" list1=['a','b']
list2=[1,2]
dict1={}
dict1 = dict(zip(list1, list2))
print(dict1) """

""" keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict1={}
def lists_to_dict(keys, values):
    length = min(len(keys), len(values))  # Determine the length of the shorter list
    # return {keys[i]: values[i] for i in range(length)}  # Create the dictionary
    for i in range(length):
        dict1[keys[i]]=values[i]
    return dict1
print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3} """


""" keys = ['a', 'b', 'c']
values = [1, 2, 3]
def lists_to_dict(keys, values):
    length = min(len(keys), len(values))  # Determine the length of the shorter list
    return {keys[i]: values[i] for i in range(length)}  # Create the dictionary

print(lists_to_dict(keys, values))  # Output: {'a': 1, 'b': 2, 'c': 3} """


# Q2. Given two dictionaries, merge them and return a single dictionary.


""" dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy()  # Start with a copy of the first dictionary
    merged_dict.update(dict2)    # Update with the second dictionary
    return merged_dict
print(merge_dicts(dict1, dict2)) """  # Output: {'a': 1, 'b': 3, 'c': 4}which

""" dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict3={}
# dict3=dict1.copy()
dict3.update(dict1)
dict3.update(dict2)
print(dict3)
 """

#Q3. Given a dictionary and a key, return True if the key is present in the dictionary, else return False.

""" def dict2(my_dict = {'a': 1, 'b': 2, 'c': 3},
key='bg'):
    if key in my_dict:
        return True
    else:
        return False
print(dict2()) """

""" my_dict = {'a': 1, 'b': 2, 'c': 3}
key='b'
for i in my_dict:
    if i ==key:
        print(True) """


# Q4. Given a dictionary and a list of keys, return another dictionary only has the keys given in the input list, and values taken from the input dictionary.

""" def lists_to_dict(keys, dict1):
    
    dict2 = {}
    for i in range(len(keys)):  # include all keys i=0,1,2,3
       if keys[i] in dict1:
          dict2[keys[i]]=dict1[keys[i]] #direct assign
        # dict2[keys[i]] = dict1.get(keys[i], None)  # safely access dict1
    return dict2
keys = ['a', 'e', 'f', 'd']
dict1 = {'e': 1, 'f': 2, 'g': 3, 'h': 4}
result = lists_to_dict(keys, dict1)
print(result)
 """


""" keys=['a','e','c','d']
dict1={'e':1,'f':2,'g':3,'h':4}
dict2={}
def lists_to_dict(keys, dict1):
    for i in range(len(keys)):
        dict2[keys[i]]=dict1.get(keys[i])
    return dict2
print(lists_to_dict(keys,dict1))
 """
""" dict1={'e':1,'f':2,'g':3,'h':4}
for i in dict1:
    print(dict1[i])
    # print(i)
 """


# Q5. Given a dictionary, return the inverted dictionary, i.e. keys of the output dictionary are the values of the input dictionary, and values of the output dictionary are the keys of the input dictionary.

""" dict1={'a':1,"b":2,"c":3}
inv_dict1={}
for key,value in dict1.items():
    inv_dict1[value]=key
print(inv_dict1) """

""" dict1={'a':1,"b":2,"c":3}
inv_dict1={}
# print(dict1.keys())
# print(dict1.values())
# for i in dict1:
#     print(i)   #a,b,c
#     print(dict1[i])  #1,2,3
for i in dict1:
    inv_dict1[dict1[i]]=i
print(inv_dict1)
    # print(dict1.values())
    # dict1.values() """

# 6. Given a dictionary containing the student names as keys and list of marks in 3 subjects as the dictionary values, return a list containing the average marks for each subject.

""" dict1={"a":[15,20,25],"b":[30,35,40],"c":[45,50,55]}
list1=[]
for i in dict1:
    for j in dict1[i]:
        total=sum(dict1[i])
    list1.append(total/len(dict1[i]))
print(list1) """

""" dict1={"a":[15,20,25],"b":[30,35,40],"c":[45,50,55]}
list1=[]
for value in dict1:
    x=(dict1[value])
    sum=0
    for i in x:
         sum=sum+i
    avg=sum/3
    list1.append(avg)
print(list1)   #20,35,50 """

# Q7. Given a dictionary containing the student names as keys and list of marks in 3 subjects as the dictionary values, return a dictionary where the keys are the student names and values are the student CGPA. Above 80 marks is A grade with 10 grade points, 60–80 marks is B grade with 8 grade points, 40–60 marks is C grade with 6 grade points, and below 40 is F with 0 grade points. Course1 is of 4 credits, Course2 of 10 credits, and Course3 of 6 credits.



# Q8. Given a fruit name and a dictionary whose keys are people names and the values are the list of fruits they like, return the list of names of people who like this fruit.

""" fruits='banana'
dict1={'ram':["apple",'banana','pineapple'],"shayam":['banana','pineapple','litchi'],"veer":['pineapple','Mango',"guava"]}
list1=[]
for people in dict1:
    if fruits in dict1[people]:
        list1.append(people)
print(list1) """


# Q 9. Given a list of integers, return its mode (list of numbers with highest frequency of occurrence) by using a dictionary in your code

def find_mode(numbers):
    """
    Function to find the mode(s) of a list of integers using a dictionary.
    :param numbers: List of integers
    :return: List of mode(s) with the highest frequency
    """
    # Step 1: Count the occurrences of each number
    frequency = {}
    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Step 2: Find the highest frequency
    max_frequency = 0
    for count in frequency.values():
        if count > max_frequency:
            max_frequency = count

    # Step 3: Find all numbers with the highest frequency
    mode = []
    for num, count in frequency.items():
        if count == max_frequency:
            mode.append(num)

    return mode

# Example usage:
numbers = [1, 2, 2, 3, 3, 4]
print(find_mode(numbers))  # Output: [2, 3]




# Q 10. Given a text file with one word in each line, return a dictionary where the key is the word and the value is the number of times it occurs in the text file.

""" def count_words_in_file(file_path):
    word_count = {}  # Initialize an empty dictionary to store word counts
    with open(file_path, 'r') as file:  # Open the file in read mode
        for line in file:  # Read each line in the file
            word = line.strip()  # Remove leading/trailing whitespace and newline characters
            if word in word_count:
                word_count[word] += 1  # Increment the count if the word is already in the dictionary
            else:
                word_count[word] = 1  # Add the word to the dictionary with a count of 1
    return word_count  # Return the dictionary
# Example usage:
file_path = 'words.txt'  # Replace with the path to your text file
result = count_words_in_file(file_path)
print(result) """



                    # Concept-6  👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                                #👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                                #👍🤔💙🩵💚🫀❤️❤️🩷🧡💛
                                #👍🤔💙🩵💚🫀❤️❤️🩷🧡💛


#Q1. Given a string as input, return its length without using the inbuilt length function.
""" len1=0
string='To take new keys'
# print(len(string))
for ele in string:
    len1+=1
print(len1) """


#Q2. Given a string as input, return the string in reverse order (without using string splicing).
# string are immutable i.e str1[i]=str2[i+1] we can't do thsi
""" str1="improve"
str2=""
for i in range(len(str1)):
    x=str1[len(str1)-i-1]
    str2=str2+x
print(str2) """

""" string='To take new keys'
new_str=[' ']
for ele in range(1,len(string)+1):
    str1=string[len(string)-ele]
    # new_str.append(str1)
    print(str1,end='')
 """

#Q3. Given a string as input, return the number of vowels in it.

""" str1="aeiou"
str2='improve'
count=0
for i in str2:
    if i in str1:
        count+=1
print(count) """

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

#Q4. Given a string as input, return the number of words in it. Use space as a separator for words.

""" def count_words(input_string):
    words = input_string.split()  # Split the string by spaces into a list of words
    return len(words)  # Return the number of words

# Example Usage
input_string = "Count the number of words in this string"
word_count = count_words(input_string)
print(f"Number of words: {word_count}") """

""" str1="37246hjwhfh fu"
str2=str1.split(' ')
sum=0
for i in str2:
    sum=sum+1
print(sum) """


#Q5. Given a string as input, return the string with the first letter of each word capitalised.
""" string='To take new keys'
x=string.capitalize()
y=string.title()
print(x)
print(y) """

#Q6. Given a string as input, return the length of the longest word in it. Use space as a separator for words.

""" str1='Good lesson today'
str2=str1.split(' ')
list2=[] #4,6,5
print(str2)
for i in str2:
    sum=0
    for j in i:
        sum=sum+1
    list2.append(sum)
print(max(list2)) """



""" import re
string='To takee new keys'
x=re.split('\s',string)
print(x)          #['To', 'tak', 'new', 'key']
max=len(x[0])
for ele in (x):
        if max<=len(ele):
            max=len(ele)
print(max) """


#Q7. Given a string as input, return True if its a valid email address, else return False.
""" import re

def is_valid_email(email):
    # Define the regular expression for a valid email
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    # Match the pattern with the given email
    if re.match(pattern, email):
        return True
    else:
        return False
# Example usage
email = input("Enter an email address: ")
print(is_valid_email(email)) """

#Q8. Given a string as input, return True if its a valid mobile number in India, else return False.
""" import re
string='hello boy\'s my number is +911231232130 and `1231232442'
x=re.search( r'\+91[0-9]{10}',string) """
# print(x)  #note ^ isses inintilly word me hona hahiye so use mat kr 
#  r'\+91\d{10}'


#Q9. Given a string as input, return True if its a palindrome, else return False (case sensitive and ignore spaces). Do not use string splicing.
# import re
# string='iitii'
# k=(len(string))
# x= re.findall(r'[a-zA-Z]', string)
# print(x)      
# for word in range(len(string)):
#     if x[word]==x[k-word]:

#        print('its a pelindrome')

#Q10. Given a paragraph as input, return a list of sentences. Use full-stop, exclamation and question mark as the three allowed delimiters between sentences. These punctuation marks should be included in the output list of sentences.






# Split the string between each character using a regular expression
""" result = re.split(r'()', string)

# Manually filter out the empty strings (instead of shorthand)
filtered_result = []
for char in result:
    if char != '':
        filtered_result.append(char)

print(filtered_result) """