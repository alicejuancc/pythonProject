"""
File: webcrawler.py
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

        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=header)
        html = response.text
        table = BeautifulSoup(html)
        # ----- Write your code below this line ----- #
        m_score = 0
        f_score = 0
        rows = table.find_all('tr')
        for row in rows[2:-1]:  # Skip the header row
            columns = row.find_all('td')
            # print(columns)
            lst = []
            for ele in columns:
                lst.append(ele.text)
            lst[2] = string_manipulation(lst[2])
            lst[4] = string_manipulation(lst[4])
            m_score += int(lst[2])
            f_score += int(lst[4])
        # for i in range(3):
        #     print("-" * 30)
        #     print(year)
        print('Male-Number: ' + str(m_score))
        print('Female-Number: ' + str(f_score))


def string_manipulation(s):
    ans = ''
    for ch in s:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()
