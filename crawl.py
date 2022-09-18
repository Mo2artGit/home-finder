from urllib import request
from bs4 import BeautifulSoup
import csv

url = "https://www.apartments.com/transit/pa/philadelphia/temple-university/lfdc5le/"

csv_file = open("rents.csv", "w", newline = "", encoding = 'utf-8')
csv_writter = csv.writer(csv_file, delimiter=',')


csv_file.close()