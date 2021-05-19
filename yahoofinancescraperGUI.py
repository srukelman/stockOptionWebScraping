from bs4 import BeautifulSoup as bs
import requests as rq
import operator as op
from datetime import datetime,timedelta,date
import csv
from tkinter import *

class Put:
    def __init__(self, name, strike, value, price):
        self.name=name
        self.strike=strike
        self.value=value
        self.price=price
        temprtrn = (float(self.price)/float(self.value))*100
        self.rtrn = format(temprtrn,'.3f')
        tempoom = 100*((float(self.value)-float(self.strike))/float(self.value))
        self.oom = format(tempoom,'.3f')
        tempapr = (float(self.price)/float(self.strike))*52*100
        self.apr = format(tempapr,'.3f')
        self.ticker = self.name[0:self.name.index('21')]
        self.expDate = str(self.name[len(self.ticker):len(self.ticker)+6])
        self.expDate = str(self.expDate[2:4])+"/"+str(self.expDate[4:])+"/"+str(self.expDate[:2])
        now = datetime.now()
        expDateDate = now.strptime(self.expDate,"%m/%d/%y")
        strnow= str(now)
        strnow = strnow[5:7]+"/"+strnow[8:10]+"/"+strnow[2:4]
        todayDate = now.strptime(strnow,"%m/%d/%y")
        oneweek = todayDate + timedelta(days=7)
        self.isExpiring = expDateDate < oneweek
    def getVolatility(self):
        return self.volatility
    def getReturn(self):
        return self.rtrn
    def setReturn(self,rtrn):
        self.rtrn = rtrn  
    def toArray(self):
        return [self.ticker, "$"+str(self.value), "$"+self.strike, str(self.oom)+"%", "", "$"+str(self.price), str(self.apr)+"%"]
    def print(self):
        return "STOCK TICKER: " +self.ticker + "\nCONTRACT NAME: " + self.name + "\nEXPIRATION DATE: "+self.expDate+"\nCURRENT STOCK PRICE: $"+self.value+"\nSTRIKE PRICE: $" + self.strike +"\nBID: $"+ self.price + "\nRETURN: "+str(self.rtrn)+"%"

def lineprepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def csvwriter(row):
    with open (cfilename, 'a',newline='') as c:
        writer = csv.writer(c)
        writer.writerow(row)
        
def csvinit(fields):
    with open (cfilename, 'w',newline='') as c:
        writer = csv.writer(c)
        writer.writerow(fields)

def is_number(s):
    try:
        float(s)
        return float(s)>0
    except ValueError:
        return False

def initWrite():
    global s
    #global cfilename
    now = datetime.now() 
    #print("now =", now)
    fields = ["TICKER", "CURRENT PRICE", "STRIKE PRICE", "OOM", "ODDS EIM", "BID", "APR"]
    csvinit(fields)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("=================================================")
    #lineprepender("optionDatav2.txt","========================================================================================================================\n")
    #f.write("========================================================================================================================\n")
    s+="=========================================================================================================================\n"
    print("DATE: ", dt_string)
    print('hellowo')
    #lineprepender("optionDatav2.txt","DATE: "+ dt_string+"\n")
    #lineprepender("optionDatav2.txt","hellowo")
    #f.write("DATE: "+ dt_string+"\n")
    s+="DATE: "+ dt_string+"\n"
    #f.write("hellowo")
    s+="hellowo\n"
    print("=================================================")
    #lineprepender("optionDatav2.txt","========================================================================================================================\n")
    #f.write("========================================================================================================================\n")
    s+="========================================================================================================================\n"

def scraper(url):
    global s
    source = rq.get(url).text
    soup = bs(source, 'lxml')
    names = soup.find_all('td',class_="data-col0 Ta(start) Pstart(10px) Bdstartw(8px) Bdstarts(s) Bdstartc(t) in-the-money_Bdstartc($linkColor)")
    strikes = soup.find_all('td',class_="data-col2 Ta(end) Px(10px)")
    value = soup.find('span',class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    prices = soup.find_all('td',class_="data-col4 Ta(end) Pstart(7px)")
    #volatilities = soup.find_all('td',class_="data-col10 Ta(end) Pstart(7px) Pend(6px) Bdstartc(t)")
    a = []
    for w,x,y in zip(names,strikes,prices):
        name = w.a.text
        loc = len(name[0:name.index('21')])+6

        #print(loc)
        #print(y.text)
        #print(str(name)[loc])
        if(str(name)[loc]=='P'and is_number(y.text)):
            #print(y.text)
            a.append(Put(name,x.a.text,value.text,y.text))
        
    #print(len(a))
    #b=[]
    for i in a:
        #print(i.strike+" "+i.value)
        if(float(i.strike)>=(0.93*float(i.value)) and float(i.strike)<=(0.97*float(i.value))):
            if(i.isExpiring):
                b.append(Put(i.name,i.strike,i.value,i.price))
            #print(i.print())
            #print()
    #print(len(b))
    #resultSort(b)
    

def out():
    global s
    for i in b:
        print(i.print())
        csvwriter(i.toArray())
        #lineprepender("optionDatav2.txt",i.print())
        #f.write(i.print())
        s+=i.print()
        print("---------------------------------------------------------------------------")
        #lineprepender("optionDatav2.txt","\n")
        #f.write("\n---------------------------------------------------------------------------\n")
        s+="\n---------------------------------------------------------------------------\n"
    lineprepender("optionDatav3.txt",s)
    #f.close()

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
    screen1 = Tk()
    screen1.geometry("500x500")
    screen1.title("Yahoo Finance Scraper")
    Label(screen1, text="Yahoo Finance Scraper", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen1, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen1, text="Scraping the Dow...",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    screen1.mainloop()


def scrape_select():
    pass


def main():
    intro_screen()

main()