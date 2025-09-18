# import urlib 
# use urlib.request to get the data from the url 
# write a function that takes a url 
# returns a response 

import urllib.request as urlib 


def main(url):
    print(f"Checking connectivity for {url}....")
    # print(url)

    response = urlib.urlopen(url)

    print("Connected to", url, "successfully")

    print("The response code was:", response.getcode())
    print("Page content:", response.read())


print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")

main(input_url)

