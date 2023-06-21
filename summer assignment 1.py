#question 1
# def is_multiple(n,m):
#     if n % m==0:
#         return True
#     else:
#         return False
# print(is_multiple(8,4))

#question 2 def is_even(k):
    last_dig=str(k)[-1]
    if last_dig in["0","2","4","6","8"]:
        return True
    else:
        return False
print(is_even(233))
question 3
# def minmax(data):

def minmax(data):
    largest = data[0]
    smallest = data[0]
    for i in data:
        if i > largest:
            largest = i
        elif i< smallest:
            smallest = i
    return smallest, largest
data=[2,5,7,1,8,6,4,10]
print(minmax(data))

# question 4 using the accumulator pattern
# def sum_of_posi_num(n):
#     summ=0
#     for i in range (0,n):
#         summ=summ+i**2
#     return summ
# print(sum_of_posi_num(4))

#question 5
# def computeArea(b,d,w,h):
#     area_trapz=(1/2)(w+(b+w+b)*d)
#     area_square=(w*h)
#     total_area=area_trapez +area_square
#     return total_area
# print(computeArea(3,4,9,7))

# question 6
# def letter_grade(grade):
#     if grade<100 and grade>=85:
#          return "A+"
#     elif grade<84 and grade>=80:
#          return"A"
#     elif grade<79 and grade>=75:
#          return"B+"
#     elif grade<74 and grade>=70:
#          return"B"
#     elif grade<69 and grade>=65:
#          return"C+"
#     elif grade<64 and grade>=60:
#          return"C"
#     elif grade<59 and grade>=55:
#          return"D+"
#     elif grade<54 and grade>=50:
#          return"D"
#     else:
#          return"E"
# print(letter_grade(90))
    
#question 7
# def abb_name(name):
#     names = name.split
#     first_name=names[0]
#     second_name=names[1]
#     last_name=names[-1]
#     
#     initial_1= first_name[0] +"."
#     initial_2=second_name[0] +"."
#     abbrv_name=initial_1 + initial_1 + last_name
#     
#     return abbrv_name
# 
# name=input("please enter full name: ")
# 
# print(abb_name(name))

#question 8
#temp_celsius= int(input("Please enter degree temperature in celsius: "))
#fahrenheit= temp_celsius +32
#print(fahrenheit)


    
     
    
