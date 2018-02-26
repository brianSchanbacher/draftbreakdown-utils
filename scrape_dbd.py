#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import argparse
import requests
from bs4 import BeautifulSoup

def getData(category, url):
    data = []

    # Get data off site
    session = requests.Session()
    # Fuck you
    session.headers.update({'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'})
    r = session.get(url)

    # Organize it
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find("table")
    tableBody = table.find("tbody")
    rows = tableBody.find_all('tr')

    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # Write to CSV
    ofile  = open(category + '.csv', "w")
    writer = csv.writer(ofile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)

    for row in data:
        writer.writerow({row[0], row[2]})

def main(args):
    getData(args.category, args.url)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Grab stats off of draftbreakdown.com')
    parser.add_argument('category', help='Category of player Ex: quaterback')
    parser.add_argument('url', help='URL to the category you specified Ex: http://draftbreakdown.com/quarterback/')
    args = parser.parse_args()
    main(args)
