from bs4 import BeautifulSoup as bs
import requests as rq
import operator
from datetime import datetime

f = open("optionData.txt", "a")
class Put:
    def __init__(self, name, value, price, volatility):
        self.name=name
        self.value=value
        self.price=price
        self.volatility = volatility
        self.rtrn = float(self.price)/float(self.value)
        self.ticker = self.name[0:self.name.index('21')]
    def getVolatility(self):
        return self.volatility
    def getReturn(self):
        return self.rtrn
    def setReturn(self,rtrn):
        self.rtrn = rtrn  
    def print(self):
        return "CONTRACT NAME: " +self.name + "\nSTOCK TICKER: " + self.ticker + "\nSTOCK VALUE: $" + self.value +"\nPUT PRICE: $"+ self.price +"\nIMPLIED VOLATILITY: "+self.volatility+"%" + "\nRETURN: "+str(self.rtrn)
    
def resultSort(arr):
    for i in range(1,len(arr)):
        key = float(arr[i].rtrn)
        keyObject = arr[i]
        j=i-1
        while j>=0 and key > float(arr[j].rtrn):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = keyObject

def initWrite():
    now = datetime.now() 
    #print("now =", now)
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("=================================================")
    f.write("========================================================================================================================\n")
    print("DATE: ", dt_string)
    f.write("DATE: "+ dt_string+"\n")
    print("=================================================")
    f.write("========================================================================================================================\n")

def scraper(url):
    source = rq.get(url).text
    soup = bs(source, 'lxml')
    names = soup.find_all('td',class_="data-col0 Ta(start) Pstart(10px) Bdstartw(8px) Bdstarts(s) Bdstartc(t) in-the-money_Bdstartc($linkColor)")
    values = soup.find_all('td',class_="data-col2 Ta(end) Px(10px)")
    prices = soup.find_all('td',class_="data-col3 Ta(end) Pstart(7px)")
    volatilities = soup.find_all('td',class_="data-col10 Ta(end) Pstart(7px) Pend(6px) Bdstartc(t)")
    a = []
    for w,x,y,z in zip(names,values,prices,volatilities):
        name = w.a.text
        loc = len(name[0:name.index('21')])+6
        #print(loc)
        if(str(name)[loc]=='P'):
            a.append(Put(name,x.a.text,y.text,z.text[0:len(z.text)-1]))
        
    #print(len(a))
    b=[]
    for i in a:
        if(float(i.volatility)>=24.0 and float(i.volatility)<=26.0):
            b.append(Put(i.name,i.value,i.price,i.volatility))
            #print(i.print())
            #print()
    #print(len(b))
    resultSort(b)
    for i in b:
        print(i.print())
        f.write(i.print()+"\n")
        print()
        f.write("\n")
    print("--------------------------------------------")
    f.write("--------------------------------------------\n")
    

def main():
    a = ["MMM", "AXP","AMGN","AAPL", "BA", "CAT", "CVX","CSCO","KO","DIS","DOW","GS","HD","HON","IBM","INTC","JNJ","MCD","MRK","MSFT","NKE","PG","CRM","TRV","UNH","V","WBA","WMT"]
    initWrite()
    print('hellowo')
    for i in a:
        scraper("https://finance.yahoo.com/quote/"+i+"/options?p="+i)
    
    f.close()
    

main()