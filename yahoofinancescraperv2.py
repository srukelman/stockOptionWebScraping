from bs4 import BeautifulSoup as bs
import requests as rq
import operator as op
from datetime import datetime

f = open("optionDatav3.txt", "a")
f.close()
b= []
s="="
class Put:
    def __init__(self, name, strike, value, price):
        self.name=name
        self.strike=strike
        self.value=value
        self.price=price
        self.rtrn = float(self.price)/float(self.value)
        self.ticker = self.name[0:self.name.index('21')]
        self.expDate = str(self.name[len(self.ticker):len(self.ticker)+6])
        self.expDate = str(self.expDate[2:4])+"/"+str(self.expDate[4:])+"/"+str(self.expDate[:2])
    def getVolatility(self):
        return self.volatility
    def getReturn(self):
        return self.rtrn
    def setReturn(self,rtrn):
        self.rtrn = rtrn  
    def print(self):
        return "STOCK TICKER: " +self.ticker + "\nCONTRACT NAME: " + self.name + "\nEXPIRATION DATE: "+self.expDate+"\nCURRENT STOCK PRICE: $"+self.value+"\nSTRIKE PRICE: $" + self.strike +"\nBID: $"+ self.price + "\nRETURN: "+str(self.rtrn)

def lineprepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def is_number(s):
    try:
        float(s)
        return float(s)>0
    except ValueError:
        return False

def initWrite():
    global s
    now = datetime.now() 
    #print("now =", now)
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
            b.append(Put(i.name,i.strike,i.value,i.price))
            #print(i.print())
            #print()
    #print(len(b))
    #resultSort(b)
    

def out():
    global s
    for i in b:
        print(i.print())
        #lineprepender("optionDatav2.txt",i.print())
        #f.write(i.print())
        s+=i.print()
        print("---------------------------------------------------------------------------")
        #lineprepender("optionDatav2.txt","\n")
        #f.write("\n---------------------------------------------------------------------------\n")
        s+="\n---------------------------------------------------------------------------\n"
    lineprepender("optionDatav3.txt",s)
    #f.close()



def main():
    global s
    urls = ["MMM", "AXP","AMGN","AAPL", "BA", "CAT", "CVX","CSCO","KO","DIS","DOW","GS","HD","HON","IBM","INTC","JNJ","MCD","MRK","MSFT","NKE","PG","CRM","TRV","UNH","V","WBA","WMT"]
    #urls = ["AAPL","AMGN"]
    initWrite()

    for i in urls:
        scraper("https://finance.yahoo.com/quote/"+i+"/options?p="+i)

    b.sort(key = op.attrgetter('rtrn'), reverse = True)
    out()
    
main()