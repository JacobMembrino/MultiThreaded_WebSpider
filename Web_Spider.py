import argparse
import urllib.request
import re
import pymysql
from bs4 import BeautifulSoup
import threading


def scrape_website(url, depth):
    request = urllib.request.urlopen(url)
    my_HTML = request.read().decode("utf8")

    soup = BeautifulSoup(my_HTML, 'html.parser')
    forms = soup.find_all("div")

    if depth == 0:
        mydb = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="mydatabase")
    elif depth >= 1:
        mydb = pymysql.connect(
            host="localhost",
            user="usr",
            password="password",
            database="mydatabase")
    else:
        print("Enter Valid Depth Int.")
        return

    mycursor = mydb.cursor()

    for column in forms:
        form = column.find('td').text.strip()
        print(form, '\n')

        query = "INSERT INTO ROW1 (form) VALUES (%s)"
        arguments = (form,)
        mycursor.execute(query, arguments)
        mydb.commit()

    mydb.close()


def main():
    parser = argparse.ArgumentParser(
        description='Multi-threaded web spider with variable depth.')
    parser.add_argument('website', help='Website URL to scrape')
    parser.add_argument('depth', type=int, help='Depth of the web spider')
    args = parser.parse_args()

    website = args.website
    depth = args.depth

    # Start multi-threaded web spider
    spider_thread = threading.Thread(
        target=scrape_website, args=(website, depth))
    spider_thread.start()
    spider_thread.join()


if __name__ == "__main__":
    main()
