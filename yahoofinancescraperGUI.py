from bs4 import BeautifulSoup as bs
import requests as rq
import operator as op
from datetime import datetime,timedelta,date
import csv
from tkinter import *

def intro_screen():
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Yahoo Finance Scraper")
    Label(screen, text="Yahoo Finance Scraper", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen, text="Scrape the whole DOW:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(text = "Go!", height="2", width = "30", command = scrape_dow).pack()
    Label(screen, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen, text="Select a few stocks to scrape:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(text = "Go!", height="2", width = "30", command = scrape_dow).pack()
    screen.mainloop()

def scrape_dow():
    pass

def scrape_select():
    pass


def main():
    intro_screen()

main()