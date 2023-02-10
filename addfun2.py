# def add_numbers(number1,number2):
#     a=number1+number2
#     print(a)
# add_numbers(56,12)

# If we give [50, 60, 10] and [10, 20, 13] to this function it will print this

def add_numbers_list(list1,list2):
    i=0
    while i<len(list1):
        c=list1[i]+list2[i]
        print(c)
        i=i+1
add_numbers_list([50,60,10],[10,20,13])