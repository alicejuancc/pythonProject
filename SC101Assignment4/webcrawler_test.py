"""
File: webcrawler_test.py
Name: 
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

        tags = soup.find_all('table', {'class': 't-stripe'})

        male_lst = []
        female_lst = []
        int_male_lst = []
        int_female_lst = []
        male_ans = 0
        female_ans = 0

        for tag in tags:
            # print(tag.tbody.text)
            lst = tag.tbody.text.split()
            for i in range(len(lst)):
                if (i - 2) % 5 == 0 and i < 1000:  # 2, 7, 12, 17, 22
                    male_lst.append(lst[i])
                elif (i + 1) % 5 == 0 and i < 1000:  # 4, 9, 14, 19
                    female_lst.append(lst[i])
            for ele in male_lst:
                int_male_lst.append(str_manipulation(ele))
            for ele in female_lst:
                int_female_lst.append(str_manipulation(ele))

            for num in int_male_lst:
                if num is not None:
                    male_ans += num
            for num in int_female_lst:
                if num is not None:
                    female_ans += num
            print(f'Male Number: {male_ans}')
            print(f'Female Number: {female_ans}')
            # print(int_male_lst)
            # print(int_female_lst)


def str_manipulation(string):
    s = ''
    for ch in string:
        if ch.isdigit():
            s += ch
    if s != '':
        return int(s)


if __name__ == '__main__':
    main()
