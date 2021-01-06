"""
Importing modules requests and bs4 for scraping the sudoku game
"""
import requests
from bs4 import BeautifulSoup

response = requests.get('https://nine.websudoku.com/?')
soup = BeautifulSoup(response.text, 'html.parser')
sudoku_file = open('sudoku_file.html', 'w')
sudoku_file.write(soup.prettify())

puzzle = soup.find(id = 'puzzle_container')
print(soup.find_all('input'))

grid = [
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", "", ""],
]



