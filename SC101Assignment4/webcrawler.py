"""
File: webcrawler_test.py
Name: Alice
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #

        # tags = soup.find_all('table', {'class': 't-stripe'}) 也可
        # tags=soup.tbody.text 也可
        tags = soup.find_all('tbody')  # tags = tags.tbody.td  # incorrect

        for tag in tags:
            tokens = tag.text.split()
            tokens = tokens[:1000]
            # print(tokens)
            male_amount = 0
            female_amount = 0
            for i in range(len(tokens)):
                # Male: 2, 7, 12, 17...
                if (i - 2) % 5 == 0:
                    s = string_manipulation(tokens[i])
                    male_amount += int(s)
                # Female: 4, 9, 14, 19...
                elif (i - 4) % 5 == 0:
                    s = string_manipulation(tokens[i])
                    female_amount += int(s)
            print(f'Male Number: {male_amount}')
            print(f'Female Number: {female_amount}')


def string_manipulation(s):
    ans = ''
    for ch in s:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()
