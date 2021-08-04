def map_ex(a,b):
    return a+b
lst1 = [1,2,3]
lst2 = [2,3,4]
lst_final = list(map(map_ex,lst1,lst2))
print(lst_final)
#for i in lst_final:
#    print(i)

# lambda() -- Predefined function
lst1 = [1,2,3]
lst2 = [2,3,4]
lst22 = list(map(lambda first,second:first*second,lst1,lst2))
print(lst22)

str1= ['Manoj', "vamshi", 'nosh', 'mahesh', 'ram']
final_str = set(map(lambda x:x*2,str1))
print(final_str)
a11 = list(map(list,str1))
print(a11)
