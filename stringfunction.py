# a="hello hasan, how are you?"
# print(a.capitalize())


# a="HELLO Hasan, How are you?"
# # print(a.casefold())
# print(a.lower())


# a="Hasan"
# print(a.center(11,'*'))
# print(a.center(9,'$'))
# print(a.center(13,'#'))


# a="hello hasan, how are you?"
# print(a.count("y"))
# print(a.count("h"))
# print(a.count("how"))
# print(a.count("o"))
# print(a.count("o", 1,5))             ###those number are index of index number
# print(a.count("o", 6,-1))


# a="hello hasan, how are you?"
# print(a.find("hasan"))               ###those number are index of index number
# print(a.find("you"))
# print(a.find("hasan", 15,40))



#this all are use for string
# str='hello this is hasan'
# print(str.split(" "))


# str='hello this is hasan'
# print(str.split(" ", 2))

# str='hello this is hasan'
# print(str.rsplit(" ", 2))


# #this is strip function , rstrip, lstrip

# h="      hahhaha"
# print(h)
# print(h.strip())

# h="      hahhaha"
# d="Nanananana"
# print(h)
# print(d.strip("Nanana"))

#this is end function it just used in print function

# h='this is hasan'
# p='hasan is good student'
# d="but he did not study many time"
# print(h,end=", ")  #end="\n" defult value
# print(p.capitalize(),end=', ')
# print(d.capitalize())



#this is sep function it just used in print function,sep use for diffrences value print in a print function

# h='this is hasan'
# p='hasan is good student'
# d="but he did not study many time"
# print(h.capitalize(),p.capitalize(),d.capitalize(),sep=", ")

# date=19
# month=4
# year=2023
# print(date,month,year,sep='-')

#this is replace function, it is used in a string to change a word or somthing

# a="hasan is a bad student"
# new=a.replace("bad","good")
# second_new=a.replace("student", "boy")
# print(second_new)



#this join function use for on array to convort a string

# h=["hello","hasan","!!!","Howe","are", "you","?"]
# str='###'.join(h)
# str='&'.join(h)
# str=' '.join(h)
# sp=str.split()
# new_str=", ".join(sp)
# print(new_str)

