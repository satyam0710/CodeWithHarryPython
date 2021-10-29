# print("Hello world")
# print("5+99")



''' 
Chapter 2: Variables and Data Types
Author: Satyam Nalawade
Date: 24 Oct 2021


Variable: A variable is a name given to memory location in a program
Keywords: Reserved words in python ex:def,class
Data types: 
            1. Integer: 2, 56
            2. Float point number: 23.4
            3. String: Collection of character "Satyam" 'Harry'
            4. Boolean: True, false
            5. None

Rules of defining the variables:
1. Variable name can content alphabet digits, and underscores
2. A varible name can only start with alphabet or undescore
3. Variable name cant start with digit
4. No space allowed in variable name            
5. Variables are case sensitive


'''
# a= 2
# b= 2.3
# c = True
# d =None
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))



'''
Operators in Python
Arithmetic Operator: +,-,*,/ etc
Asignment Oerator: =, +=, -+ etc.
Comparison Operator: ==, > ,>=, <, <=,!= etc
Logical Operartor: and, or, not
'''
#Arithmetic Operator
# a= 12
# b= 22

# print( "Addition is:", a+b)
# print( "Subtraction is:", a-b)
# print( "Multiplication is:", a*b)
# print( "Division is:", a/b)

#Assignment Operator

# a= 37
# a += 8
# a -=8
# a *=8
# a /=8


# print('a:',a)
# print('a:',a)

#Comparison Operator

# a = (14>70)
# b = (14<70)
# c = (14>=70)
# d = (14<=70)
# e = (14==70)
# f = (14!=70)

# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(f)


#logical Operators

# bool1 = True
# bool2 = False

# print("The value of bool1 and boool2 is:",bool1 and bool2)
# print("The value of bool1 or bool2 is:",bool1 or bool2)
# print("The value of bool1 not bool2 is:", not bool2)

#TypeCasting: Converting one datatype to another


# e= 89.43
# e= int(e)
# print(e)
# print(type(e))
# q = "3243"
# q = int(q)
# w = q+65
# print(type(q))
# print(w)

# x=str(123) 
# y=int("8898")
# z=float('43')
# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))
# print(type(z))

''' 
 Input Function:
        This functio allows user to take input from keyboard as string
        **Imp Note: The output of string is always string


'''
# s = input('Enter 1st Number:')
# t = input('Enter 2nd Number:')
# u = int(s)   #Convert to Integer
# p = int(t)
# print(u+p)
'''
Practice Set of CHapter 2:
1. Addition of two number
2. Write a code for find a reminder when number is divided by x
3. Check the type of variable assigned using input() function
4. Using Comparison Operator find a i greater than equal or not
5. Find average of two number entered bu the user
6. 

'''


#'2. Remainder Code'
# a = int(input('Enter a number:'))
# b = int(input('ENter another Number:'))
# c = a%b
# print(c)

#4.Comparison
# a = int(input('Enter value of a:'))
# b = int(input('ENter value of b:'))
# c = a>=b
# print(c)

#5. Average

# a = int(input('Enter value of a:'))
# b = int(input('ENter value of b:'))
# c = (a+b)/2
# print("Average of two numbers:", c)

#6. Calculate square of a number

# a = int(input("Enter a number:"))
# b = a**2
# print('Square of a number is:',b)


# a=12
# b= "Satyam"
# c= 0.745
# d= 5
# print(a+d)
# print(a-d)
# print(a*d)
# print(a/d)
# print(a//d)      '''Returns Integer Value'''
# print(a**d)      '''Exponential'''
# print(a%d)
# Variable =type(b)
# print(Variable)





'''
Chapter 3: Strings   
Date: 25 Oct 2021
> String is a datatype in python
> String is sequence of character enclosed in quoates
> We can write strings in following ways:
    =Single quoated:   'Billionaire'
    =Double quoated:   "DevOps"
    =Triple quoated:   #Satyam 



String Slicing:    
     A string in python can be sliced  for getting particular part of string

String Concatination



'''


# a = 'Harry"s'
# b = "Harry's"
# print(a)
# print(b)

#3.1 Concatination
# name = 'Satyam Nalawade'

#3.2 String Slicing
# print(name[0:4])   #string Slicing   print(name[:4 ]) is sam eas print([0:4]), name([0:]) prints entire string name[0:6]
#  name[3] = 'dsa'   -> THis wont works Not Allowed
#negative indexing
# print(name[-4])


#3.3 Slicing With Skip Value


# name = "RajVeer Singh"
# print(name[0::2])

# word = "amazing"
# word[0:]  word[0:7]
# word[:7]  word[0:7]

#string = " once Upon a time there was a guy who is hustling hard for his future named harry"
# print(string[0:])

#3.4 String Functions:
# ->Length of String len()
# -> string.endswith("harry")
# -> string.count('o')
# -> string.capitalize("string")
# -> print(string.find("who"))  first occurences
# -> string.replace(old word, new word)  all occurences

# print(len(string))
# print(string.endswith('harry'))
# print(string.count('h'))
# print(string.capitalize())
# print(string.find("who"))
# print(string.replace('harry','satyam'))


# 3.5 Escape sequence charaters:
#Examples \n, \t , \', \\

# dn = " Harry is Good guy. \n He teaches \t python \t for free priceless"

# print(dn)

'''
Practice Set:
1. Write a code for user entered named followed by Good Morning
2. Write a proogram to t=fill the letter template given below with name and date
  lette = Dear <| NAME |>,
          You are Selected !

          <|Date|> 
3. Write a program to detect double spaces in  a string   
4. Replace Double Spaces with single spaces  
5. Write a program to format the following letter using escape sequence charater
   letter = "Dear Harry, This Python course is nice!"     

'''

# Practice Test 3.1
# x=input("Enter Your Good name:\n")
# print("Good Morning", x, "Have a Nice Day!")


#Peactice Set 3.2
# letter = '''     Dear, <|NAME|>
                 
#                  You are selected for Mindtree as a Jr ENgineer!
                
#     <|DATE|>

# '''


# Name = input("Enter Name of Candidate:\n")
# Date = input("Enter the Date:\n")

# letter = letter.replace("<|NAME|>", Name)
# letter = letter.replace("<|DATE|>", Date)

# print(letter)

# Practice Set 3.3

# st = "I am a DevOps Engineer at  Mindtree "
# ds = st.find("  ")
# print(ds)



# Practice Set 3.4

# st = "I am a  DevOps  Engineer at  Mindtree "
# ds = st.replace("  ", " ")
# print(ds)


# Practice Set 3.5
 
# letter = "Dear Harry, This Python course is nice! Thanks!" 
# print(letter)

# formatted_letter = "Dear Harry, \n \t This Python course is nice! \nThanks!" 
# print(formatted_letter)



# Name = "Billionaire"

# Friends =  "Satyam, Aman, Sourabh, Sayaji"


# print(len(Name))
# var = Name.upper()
# var = Name.lower()
# var = Name.replace("B","Tr")
# var1 = Friends.replace(",","\n")
# print(var)
# print(Friends)
# print(var1)
# print(Name[0])
# print(Name.strip())
# print(Name[2:4])

# name1 = "Satyam"
# name2 = "Billionaire"
# # Str1 = " Hey Everyone my name is {}, and I'm going to be the future {} ".format(name1, name2)
# Str1 = f" Hey Everyone my name is {name1}, and I'm going to be the future {name2} "
# print(Str1)



'''
#Python Collections: 
   #1. #List 
   #2. #Tuple 
   #3. #Set 
   #4.#Dictionary



# 1. List 
   
# lst =  [12, 34, 53 , 30, 56, 39] 
# var = type(lst)
# var = lst[2]
# lst[2]=35
# var = lst[2:5] 

# print(var)

# lst.append(459)
# lst.insert(2,123)
# lst.remove(123)
# lst.pop()
# del  lst[4]
# lst.clear()

# print(lst)
# print(len(lst))

'''

# Python CHapter 4: Lists and Tuples
# Date: 26/10/21 


'''

# Python CHapter 4: Lists and Tuples
# Date: 26/10/21 
Python Lists: This is nothing but a containers to store the set of values of any data type.


'''
#Create list using []

# a = [1,2,33,43,55,42,34]
# print(a)

# print list using print() function
# print(a)

#Access string using index a[0], a[1], a[2]
# print(a[4]) 

#change the value of list using

# a[0]=98
# print(a)

# We can create a list using different data types
# lst = [12, 212.33, "Satyam", True, False]
# print(lst)

# List Slicing


# friends = ['satyam', 'sam', 'harry', 'hemoi',  'yash']
# print(friends[0:4])
# print(friends[-4:])



'''
List Methods: 

Consider the following list
L1 = [1, 8,7, 2, 21,15]

1. L1.sort()     
2. L1.reverse()
3. L1.append()
4. L1.insert()
5. L1.pop()
6. L1.remove()

'''
# L1 = [1, 8,7, 2, 21,15]

# L1.sort()  #Sorts the lists
# L1.reverse() #Reverses the list

# L1.append(123)   #Adds at the end of the list
# L1.insert(2, 544)  # Inserts 544 at index 2

# L1.pop(2)   # Removes an element at index 2
# L1.remove(21)   #Removes 21 from list

# print(L1)



'''
Tuples: Tuple is immutable(cannot change) data type in python


a() = Empty Tuple
a(1,) = Tuple with only one element needs a comma
a(1,2,3,5) = Tuple with more than one element


*** Once Defined tuple cannot be altered or manipulated ***

'''

# Creating a tuple using ()

# t = (1,2,3,4,5,6)
# print(t)

#printing the elements of tuple
# print(t[2])

# Cant update the value of tuple
# t[2] =333   #not supported
# print(t)



# t1 = ()   # Empty tuple
# print(t1)

# t1 = (1)  # wrong way to to write tuple
# t1 = (1,)  #tuple with on element
# print(t1)



'''
Tuple Methods:
Consider a follwing Tuple
a = (1,7,2)

1. a.count(1)   Will returns Number of times 1 occured in tuple
2. a.index(1)   Will returns index of first occurance of  in tuple

'''

# t = (1,7,2,5,1,1,1,56,77,1)
# print(t.count(1))
# print(t.index(77))


'''
Chapter 4: Practice Set

1. Write a program to store 7 fruits in list 
2. Write a program to accept marks of 6 students and display them in  asorted manner
3. Check that Tuple cannot be changed in pyhon 
4. Write a program to sum a list with 4 Numbers
5. Write a program to count the number of 0's in following tuple  a = (7,0,8,0,0,9)



'''
# Solution 4.1:

'''
f1 = (input("Enter fruit number 1:"))
f2 = (input("Enter fruit number 2:"))
f3 = (input("Enter fruit number 3:"))
f4 = (input("Enter fruit number 4:"))
f5 = (input("Enter fruit number 5:"))
f6 = (input("Enter fruit number 6:"))
f7 = (input("Enter fruit number 7:"))

MyFruitList = [f1, f2, f3, f4, f5, f6, f7]
print(MyFruitList)

'''

# Solution 4.2:
'''
m1 = int((input("Enter Marks for student number 1:")))
m2 = int((input("Enter Marks for student number 2:")))
m3 = int((input("Enter Marks for student number 3:")))
m4 = int((input("Enter Marks for student number 4:")))
m5 = int((input("Enter Marks for student number 5:")))
m6 = int((input("Enter Marks for student number 6:")))

marksofstudents = [m1, m2, m3, m4, m5, m6]
marksofstudents.sort()
print(marksofstudents)

'''


#Solution 4.3
'''
t = (9,3,6,12,15)
t[0]=4
print(t)

'''


#Solution 4.4
'''
l = [ 12, 43, 44, 55]
print(l[0]+l[1]+l[2]+l[3])
print(sum(l))

'''


#Solution 4.5
'''
a = (97,0,8,0,0,9)
print(a.count(0))

'''







# Python CHapter 5: Dictionary and Sets
# Date: 27/10/21 - 28/10/21 // Only Theory Done on 27 Wrong Transaction
'''
Dictionary: It is nothing but a collection of Key-Value pairs

Syntax:
      a = {"key" : "value"
           "Harry" : "Code"
           "Mars" : "100"
           "list" : "[1,2,3,4]" 
      }

   print(a["Mars"])    
   print(a['mydict']['HArry'])


Properties of Python Dictionary:
1. It is unordered 
2. It is mutable
3. It is Indexed
4. It cannot contain duplicate keys


'''  

# a = {"key" : "value",
#      "Harry" : "Code",
#      "Mars" : "100",
#      "list" : "[1,2,3,4]",
#      " Harry": "Fast coder",
#      "Marks": [1,2,3,45,43],
#      "mydict" : {"HArry" :12}
#     }
# #print(a)
# print(a["Mars"])  
# a['Marks'] = [1,4,55,66]
# print(a['Marks'])
# print(a)
# print(a['mydict']['HArry'])
# print(type(a))



'''
Dictionaries Methods:
Consider the following dictionary

a = {"key" : "value",
     "Harry" : "Code",
     "Mars" : "100",
     "list" : "[1,2,3,4]",
     " Harry": "Fast coder",
     "Marks": [1,2,3,45,43],
     "mydict" : {"HArry" :12}
    }

1. a.items() : Return a list of (key-value) tuples
2. a.keys() : Returns a list containing dictionaru's keys
3. a.update({'friend': 'sam'}) : Updates the dictionary with supplied key-value pair

'''
myDict = {"key" : "value",
          "Harry" : "Code",
          "Mars" : "100",
          "list" : "[1,2,3,4]",
          "Harry": "Fast coder",
          "Marks": [1,2,3,45,43],
          "anotherdict" : {"HArry" :12},
          12: 22
    }

#Dictionary Methods:

# print(myDict.keys()) #prints the keys of the dictionary
# print(myDict.values()) # Prints the values of dictionary
# print(list(myDict.keys()))    # Prints the keys of Dictionary
# print(type(myDict.keys()))
# print(myDict.items())      #Prints the (key,values)for contents of all dictionary
 

#print(myDict)
updateDict = { 'DevOps': 'AWS, DevOps',
 "Name" : "Satyam",
 "Python": "Begineer Friendly",
 "Harry" : "DevOps"       # If new key value pair added then it will upddates previous key
 }
#myDict.update(updateDict)  #Updates the dictionary by adding key-value pairs in updateDict
#print(myDict)



#print(myDict.get('Harry'))    
#print(myDict['Harry'])   #

#Difference between .get and [] systax in dictionaries ?
#print(myDict.get('Harry2'))    #interview Question It will return None as Harry2 is not present in dictionary
#print(myDict['Harry2'])   #Throws an error as Harry2 is not present in dictionary If you add key in square bracket then its your resposibility that the key is present in dictionary






'''
Set in Python:  Set is collection of non-repeatative element
                Set in python is a data type containing unique values 

s= set()   // No Repeatation allowed 
s.add(1)
s.add(2)  // or set = {1,2}

'''

s = {1,2,3,4,5,1,2,3,4,5}  # Set will ignore if elements repeated 
#print(s)
#print(type(s))


'''
Important
| |
V V
'''
#Empty Set
a = {}           #This will be the empty dictionary
# print(type(a))


#Syntax for creating empty set
b = set()        # This is the right way to create empty set 



'''
Properties of Set:

1. Sets are    /Element order doesnt matter
2. Sets are unindexed /Cannot access element by index
3. Tgere is no way to change items in sets
4. Sets cannot contain duplicate values

'''

'''
Operations on sets:

Consider th following set
s = {1,8,2,3}

1. len(s) :  Returns 4 as length of the set
2. s.remove(8) : Updatesthe set and Removes 8 from the set
3. s.pop(): Removes an arbitary element fodm the set and returns the element removed
4. s.clear() : Empties the set 
5. s.union({8,11}): Returns a new set with all items from both sets {1,8,2,3,11}
6. s.intersection({8,11}): Returns a set which contains only items in both sets {8}



'''



#Adding values in empty set
b.add(1)
b.add(2)
b.add(32)
b.add(221)
b.add(2)    # adding values repeatedly doesnt changes a set 
# b.add([1,22,33,44])   #unhashable type: 'list' cannot add list into the Set because list is not hashable(Content can be change)
# b.add({45:22})        # We cnnot add dictionary because its content can be changed
# b.add((22,33,44,55,66)) #We can add tuples in Set because it is immutable i.e contenct cannot be changed
# print(type(b))

#Length of the set
# print(len(b))   //Prints the length of the set

#Removal of elements from set
# b.remove(32)    # Removes the elements from set
# b.remove(2)
# b.pop()

# print(b)
# print(len(b))
# b.remove(90)

'''
Chapter 4: Practice Set
Date: 29/10/21

'''
'''
1. Write a program to create a dictionary of hindi words with values as  their english translation provide user with an option to look up to it! 
'''
myDict = { 'Nashta':'breakfast' , 'Subah':'Morning', 'Raat':'Night', 'Sapana':'Dream', 'Chidiya':'Sparrow'}
# print("Options are:\n",myDict.keys())
# a = input("Enter the Hindi Word \n")
# print('The meaning of word is:', myDict[a])

#Below line will not throw error if key is not present in dictionary

# print('The meaning of word is:', myDict.get(a))



'''
2. Write a program to input eight numbers from the user and display all the unique numbers once

'''
# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))
# num3 = int(input("Enter Number 3:"))
# num4 = int(input("Enter Number 4:"))
# num5 = int(input("Enter Number 5:"))
# num6 = int(input("Enter Number 6:"))
# num7 = int(input("Enter Number 7:"))
# num8 = int(input("Enter Number 8:"))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}

# print(s)
# print(len(s))

'''
3. Can we have set with 18(int) and 18(str) as values in it
'''

