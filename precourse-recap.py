#

# In the file, create a simple Python program:

#     create variables of different types
#     call some methods/functions on these variables
#     use some operators (e.g. +, -)



# var_a = str(input("enter words to be capitalized\n"))
# upper=var_a.upper() 
# print(upper)





print("Enter numbers for summation\nType END to exit\n")
list_n=[]
result=0
while True:
    user_in=input()    

    if user_in==str("END"):
        print("Ending input")
        break

    else:
         list_n.append(user_in)
        
        #  print (len(list_n))

 

for i in range (len(list_n)):
    result=result+(int(list_n[i]))
    # print (result)

print('the sum of the numbers you entered')
print(list_n)
print("is\n" +str(result))