#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from pprint import pprint 

url = "https://www.britannica.com/sports/Africa-Cup-of-Nations"

def fetch_html():
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text,"html.parser")
    return soup

def get_header(soup):
    header = soup.find("thead").find_all("th")
    res=[]
    for elem in header:
        res.append(elem.text.strip())
    return ",".join(res)

def get_data(soup):
    content = soup.find("tbody").find_all("tr")
    res = []
    for elem in content:
        if elem.name : 
            elem = [x.strip() for x in elem.text.split("\n")]
            elem = [x for x in elem if x!=""]
            res.append(elem)
    return clean_data(res)


def clean_data(data):
    cleaned_data = [[item.replace('*', '') for item in sublist] for sublist in data]
    return cleaned_data



def main():
    soup = fetch_html()
    header = get_header(soup)
    print(header)
    data = get_data(soup)

    # Updating the data with AFCON 2023's result 
    res2023 = ["2023","Côte d'Ivoire","Nigeria"]   
    data.append(res2023)

    for sublist in data:
        print(",".join(sublist))


if __name__=="__main__":
    main()