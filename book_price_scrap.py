# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 17:41:53 2017

@author: Alec
"""
from bs4 import BeautifulSoup as bsoup
import requests
import sys
import webbrowser

#Get user input
def find_search_details():
    while True:
        search_type = input('Please enter look up type ( I = ISBN, T = Title ) : ')
        search_type = search_type.lower()
        if search_type == 'i':
            keyword = input('Please enter ISBN: ')
            year = None
            author = None
            break
        if search_type == 't':
            keyword = input('Please enter title: ')
#            while True:            
#                    yearYN = input('Is there a specific author? (Y/N) ')
#                    if yearYN.lower() == 'y':
#                        author = input("Please the author's name format : ")
#                        break
#                    if yearYN.lower() == 'n':
#                        break
#                    else:
#                        print("Sorry that was not a valid input. \n ")
            while True:            
                yearYN = input('Is there a specific year? (Y/N) ')
                if yearYN.lower() == 'y':
                    year = input('Please enter year in YYYY format : ')
                    break
                if yearYN.lower() == 'n':
                    break
                else:
                    print("Sorry that was not a valid input. \n ")
        else:
            print("Sorry that was not a valid input. \n ")

	#type (I or T), keyword (string)
    return search_type, keyword, year , author
 
 
#Search based on input
def search(search_type, keyword, year, author):
    
    if search_type == 'i':
        print('Searching... \n')
        data = requests.get('https://www.abebooks.com/servlet/SearchResults?sts=t&an=&tn=&kn=&isbn=' + str(keyword))
        
    if search_type == 't':
        print('Searching... \n')
        keyword.replace(' ', '+')   
        if year == None:
            data = requests.get('https://www.abebooks.com/servlet/SearchResults?cm_sp=SearchF-_-NullResults-_-Results&tn=' + str(keyword))
        else:
            data = requests.get('https://www.abebooks.com/servlet/SearchResults?bi=0&bx=off&cm_sp=SearchF-_-Advtab1-_-Results&ds=50&recentlyadded=all&sortby=17&sts=t&tn=' + str(keyword) + '&yrh=' + str(year) + '&yrl=' + str(year))
                
    results = bsoup(data.content, 'html.parser')
    return results

##Main call
def main():
    search_type, keyword, year, author = find_search_details()
    
    results = search(search_type, keyword, year, author)
    html = open('doc.html', 'w')
    html.write(str(results))
    
if __name__ == '__main__':
    main()

#
##Read results
#def read_results(results):
#	If none:
#		print('Sorry, there were no books by the' + TYPE + KEYWORD)
#
#	if some:
#		title = ''
#		isbn = ''
#		prices = []
#		return title, isbn, prices
#
##Calculate Average price
#def average(prices):
#	count = 0
#	sum_tot = 0
#	for price in prices:
#		1+=count
#		price += sum_tot
#
#	average_price = sum_tot/count
#
#	return average_price
#
##Calculate Median price
#def median(prices):
#	return median_price
#
##Display results to user
#def show_results(title, isbn, prices, average_price, median_price):
#	print ()