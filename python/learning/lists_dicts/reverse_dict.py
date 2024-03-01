# Python3 code to demonstrate working of 
# Reverse Dictionary Keys Order
# Using OrderedDict() + reversed() + items()
from collections import OrderedDict
  
# initializing dictionary
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
  
# printing original dictionary
print("The original dictionary : " + str(test_dict))
  
# Reverse Dictionary Keys Order
# Using OrderedDict() + reversed() + items()
res = OrderedDict(reversed(list(test_dict.items())))
  
# printing result 
print("The reversed order dictionary : " + str(res)) 


# Python3 code to demonstrate working of 
# Reverse Dictionary Keys Order
# Using reversed() + items()
  
# initializing dictionary
test_dict = {'gfg' : 4, 'is' : 2, 'best' : 5}
  
# printing original dictionary
print("The original dictionary : " + str(test_dict))
  
# Reverse Dictionary Keys Order
# Using reversed() + items()
res = dict(reversed(list(test_dict.items())))
  
# printing result 
print("The reversed order dictionary : " + str(res)) 


# Manual 
original_dict={'A':0,'C':2,'B':1}
new_dict={}
for k,v in original_dict.items():
    dict_element={k:v}
    dict_element.update(new_dict)
    new_dict=dict_element
print(new_dict)
