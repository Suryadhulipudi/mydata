
import requests
  
# Making a GET request
r = requests.get('https://api.github.com / users / naveenkrnl')
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

# Making a POST request
r = requests.post('https://httpbin.org / post', data ={'key':'value'})
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.json())

# Making a PUT request
r = requests.put('https://httpbin.org / put', data ={'key':'value'})
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.content)

# Making a DELETE request
r = requests.delete('https://httpbin.org / delete', data ={'key':'value'})
 
# check status code for response received
# success code - 200
print(r)
 
# print content of request
print(r.json())




