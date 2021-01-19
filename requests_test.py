# requests_test.py
# read and get information form http

import requests

response = requests.get("https://automatetheboringstuff.com/files/rj.txt")
# print(response.status_code)

# raise an error if there is one
response.raise_for_status()

# create a variable to store the file
f = open("Romeo_and_Juliet.txt", "wb")

# grab the info from http and save it in the variable
for chunk in response.iter_content(1000000):
    f.write(chunk)

# write the file to disk
f.close()
