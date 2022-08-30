'''
def Convert(string):
    li=list(string.split(" "))
    return li
str1="Hello I am a Python"
print(Convert(str1))
'''


'''
#List To String
def listToString(s):
    str1=" "
    return(str1.join(s))
s=["Hello","I","am","Python"]
print(listToString(s))
'''



'''
#
def convert(list):
    return tuple(list)
list=[1,2,3,4]
print(convert(list))
'''




#list to dictionary
def Convert(list):
    dct={lst[i]:lst[i+1]for i in range(0,len(lst),2)}
    return dct
lst=['a','1','b','2','c','3']
print(Convert(list))





