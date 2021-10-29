import requests
import json

"""
here is codes of craftsmen 'Software engineer trainee' online screening tests.
all the code has been written following by the instructions given in the mail. 
"""

# step 1 - do post request

url = "https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/access"

body = {
    "email": "your@gmail.com"
}
headers = {
    "content-type": "application/json",
    "x-api-key": "JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0"
}

res = requests.post(url, data=json.dumps(body), headers=headers)  # sending post request
print(res.content)  # content of the response


# step 2 - get the access token

url2 = "https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/access?email=pro.sahaib9747@gmail.com"  # add extra info
res2 = requests.get(url2, headers=headers)

print(res2.status_code)  # check is it 200 or not, 200 means communication is ok.
print(res2.content)


# step 3 - get the next instructions 

url3 =  "https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/screeningForm?email=pro.sahaib9747@gmail.com" 
headers3 = {
    "content-type": "application/json",
     "x-api-key": "JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0",
     'accesstoken': "ZGtsmiy0yFbRxOJf-pro.sahaib9747%40gmail.com-Nzgk9veS9ldobyOU"
}
res3 = requests.get(url3, headers=headers3)

# here you will get the next instructions to be follow. 
# check the decoder.py file cause the task is to decode the url to get whats next.
print(res3.content)  
