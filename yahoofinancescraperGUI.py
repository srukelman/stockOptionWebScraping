from bs4 import BeautifulSoup as bs
import requests as rq
import operator as op
from datetime import datetime,timedelta,date
import csv
from tkinter import *
import os

today = datetime.today()
strtoday = str(today)
strtoday = strtoday[:10]+"_"+strtoday[11:13]+strtoday[14:16]+strtoday[17:19] 
cfilename = "optionSpreadsheet"+ strtoday +".csv"
tfilename = "optionTextfile"+ strtoday +".txt"
c = open(cfilename,"a",newline="")
c.close()
f = open(tfilename, "a")
f.close()
b= []
s= "="
lab1= None
lab2 = None
lab3 = None
lab4 = None
lab5 = None
but1 = None
but2 = None
but3 = None
but4 = None
but5 = None
but6 = None
but7 = None
ent1 = None
ent2 = None
ent3 = None
scraperIsDone = False
scraperIsStarted = False
screen = None
screen1 = None
screen2 = None
screen3 = None
#urls = []
count =0
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
    global s
    headers = { 
        'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'DNT'             : '1', # Do Not Track Request Header 
        'Connection'      : 'close'
    }
    source = rq.get(url,headers=headers).text
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
    
def run_scraper(urls):
    #global urls
    global scraperIsStarted
    global scraperIsDone
    global lab1
    global screen1
    
    scraperIsStarted = True
    initWrite()
    count = 1
    #urls = ["MMM", "AXP","AMGN","AAPL", "BA", "CAT", "CVX","CSCO","KO","DIS","DOW","GS","HD","HON","IBM","INTC","JNJ","MCD","MRK","MSFT","NKE","PG","CRM","TRV","UNH","V","WBA","WMT"]

    for i in urls:
        scraper("https://finance.yahoo.com/quote/"+i+"/options?p="+i)
        num = count % 3
        label = {
            1: "Scraping the DOW...",
            2: "Scraping the DOW.",
            0: "Scraping the DOW.."
        }
        lab1.config(text = str(label.get(num,"Scraping the DOW...")))
        screen1.update()
        count+=1


    b.sort(key = op.attrgetter('rtrn'), reverse = True)
    out()
    scraperIsDone = True

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
    global scraperIsDone
    if scraperIsDone: quit_screen1()
    scraperIsDone=False
    global screen
    screen = Tk()
    screen.geometry("500x500")
    screen.title("Yahoo Finance Scraper")
    Label(screen, text="Yahoo Finance Scraper", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen, text="Scrape the whole DOW:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(text = "Go!", height="2", width = "30", command = scrape_dow).pack()
    Label(screen, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen, text="Select a few stocks to scrape:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(text = "Go!", height="2", width = "30", command = scrape_select).pack()
    screen.mainloop()

def scrape_dow():
    global screen1
    global screen
    screen.destroy()
    screen1 = Tk()
    screen1.geometry("500x500")
    screen1.title("Yahoo Finance Scraper")
    Label(screen1, text="Yahoo Finance Scraper", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen1, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    global lab1
    lab1 = Label(screen1, text="Scraping the Dow...",  width = "300", height = "1", font ={"Calibri", 13})
    lab1.pack()
    global lab2
    lab2 = Label(screen1)
    lab2.pack()
    global lab3
    lab3 = Label(screen1)
    lab3.pack()
    global lab4
    lab4 = Label(screen1)
    lab4.pack()
    global lab5
    lab5 = Label(screen1)
    lab5.pack()
    global but1
    but1 = Button(screen1)
    but1.pack_forget()
    global but2
    but2 = Button(screen1)
    but2.pack_forget()
    global but3
    but3 = Button(screen1)
    but3.pack_forget()
    global but4
    but4 = Button(screen1)
    but4.pack_forget()
    dow_update()      
    screen1.mainloop()
    dow_update() 

def dow_update():
    global scraperIsDone
    global scraperIsStarted
    global lab1
    global lab2
    global lab3
    global lab4
    global lab5
    global but1
    global but2
    global but3
    global but4
    global screen1
    urls = ["MMM", "AXP","AMGN","AAPL", "BA", "CAT", "CVX","CSCO","KO","DIS","DOW","GS","HD","HON","IBM","INTC","JNJ","MCD","MRK","MSFT","NKE","PG","CRM","TRV","UNH","V","WBA","WMT"]
    if not scraperIsStarted:
        run_scraper(urls)
    if scraperIsDone:
        lab1.config(text = "Scraping is complete!")
        lab2.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but1.pack()
        but1.config(text = "Scrape Again", height="2", width = "30", command = intro_screen)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but3.pack()
        but3.config(text = "Open Text File", height="2", width = "30", command = open_txt)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but4.pack()
        but4.config(text = "Open CSV File", height="2", width = "30", command = open_csv)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but2.pack()
        but2.config(text = "Quit", height="2", width = "30", command = quit_screen1)
    else:
        #lab1.config(text = "Scraping the Dow...")
        screen1.after(1000, dow_update)

def quit_screen1():
    global screen1
    screen1.destroy()

def open_txt():

    os.system("notepad "+tfilename)

def open_csv():

    os.system("start excel "+cfilename)

def scrape_select():
    global screen2
    global screen3
    #global urls
    screen2 = Tk()
    #screen3 = Tk()


def select_update():
    global scraperIsDone
    global scraperIsStarted
    global lab1
    global lab2
    global lab3
    global lab4
    global lab5
    global but1
    global but2
    global but3
    global but4
    global screen1
    
    if not scraperIsStarted:
        run_scraper()
    if scraperIsDone:
        lab1.config(text = "Scraping is complete!")
        lab2.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but1.pack()
        but1.config(text = "Scrape Again", height="2", width = "30", command = intro_screen)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but3.pack()
        but3.config(text = "Open Text File", height="2", width = "30", command = open_txt)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but4.pack()
        but4.config(text = "Open CSV File", height="2", width = "30", command = open_csv)
        lab3.config(text = "",  width = "300", height = "1", font ={"Calibri", 13})
        but2.pack()
        but2.config(text = "Quit", height="2", width = "30", command = quit_screen1)
    else:
        #lab1.config(text = "Scraping the Dow...")
        screen1.after(1000, dow_update)

def main():
    intro_screen()

main()