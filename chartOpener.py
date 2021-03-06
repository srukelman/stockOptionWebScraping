import webbrowser
#import urllib
from tkinter import *

global tickers
tickers = []
screen = None
screen1 = None
numString = None
screen2 = None
tickerString = None
screen3 = None

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Chart Opener")
    Label(screen, text="Chart Opener", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(screen, text = "Go!", height="2", width = "30", command = num_charts).pack()
    screen.mainloop()

def num_charts():
    screen.destroy()
    global screen1
    #screen1 = Toplevel(screen)
    screen1 = Tk()
    screen1.title("Chart Opener")
    screen1.geometry("600x250")
    Label(screen1, text="Chart Opener", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen1, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen1, text="Enter the number of charts you would like to open:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    global numString
    numString = StringVar()
    Entry(screen1, textvariable = numString).pack()
    Label(screen1, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(screen1, text = "Go!", height="2", width = "30", command = enter_tickers).pack()
    screen1.mainloop()

def enter_ticker_window():
    #screen1.destroy()
    global screen2
    #screen2 = Toplevel(screen)
    screen2 = Tk()
    screen2.title("Chart Opener")
    screen2.geometry("600x450")
    Label(screen2, text="Chart Opener", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen2, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen2, text="Enter the ticker of the chart you would like to open:",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    global tickerString
    tickerString = StringVar()
    Entry(screen2, textvariable = tickerString).pack()
    Label(text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(screen2, text = "Go!", height="2", width = "30", command = ticker_confirm_window).pack()
    screen2.mainloop()
    
def ticker_confirm_window():
    global tickers
    tickers.append(tickerString.get())
    screen2.destroy()
    global screen3
    screen3 = Tk()
    screen3.title("Chart Opener")
    screen3.geometry("600x450")
    Label(screen3, text="Chart Opener", bg = "grey", width = "300", height = "2", font ={"Calibri", 13}).pack()
    Label(screen3, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen3, text="Your chart will be opened when entry of all tickers is complete",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen3, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen3, text="(Click okay to enter the next ticker or open charts if complete)",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Label(screen3, text="",  width = "300", height = "1", font ={"Calibri", 13}).pack()
    Button(screen3, text = "(I'm not) OK!", height="2", width = "30", command = close_ticker_window).pack()

def close_ticker_window():
    screen3.destroy()

def enter_tickers():
    num = int(float(numString.get()))
    screen1.destroy()
    for i in range(0,num):
        enter_ticker_window()
    open_charts()


def open_charts():
    global tickers
    #urls = ["MMM", "AXP","AMGN","AAPL", "BA", "CAT", "CVX","CSCO","KO","DIS","DOW","GS","HD","HON","IBM","INTC","JNJ","MCD","MRK","MSFT","NKE","PG","CRM","TRV","UNH","V","WBA","WMT"]
    #watch = ["IBM","INTC"]
    for i in tickers:
        #urllib.urlopen("https://finance.yahoo.com/quote/"+i+"/chart?p="+i+"#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjQuNTQxODMyNjY5MzIyNzEsImZsaXBwZWQiOmZhbHNlLCJ2b2x1bWVVbmRlcmxheSI6dHJ1ZSwiYWRqIjp0cnVlLCJjcm9zc2hhaXIiOnRydWUsImNoYXJ0VHlwZSI6ImxpbmUiLCJleHRlbmRlZCI6ZmFsc2UsIm1hcmtldFNlc3Npb25zIjp7fSwiYWdncmVnYXRpb25UeXBlIjoib2hsYyIsImNoYXJ0U2NhbGUiOiJsaW5lYXIiLCJwYW5lbHMiOnsiY2hhcnQiOnsicGVyY2VudCI6MSwiZGlzcGxheSI6IkFBUEwiLCJjaGFydE5hbWUiOiJjaGFydCIsImluZGV4IjowLCJ5QXhpcyI6eyJuYW1lIjoiY2hhcnQiLCJwb3NpdGlvbiI6bnVsbH0sInlheGlzTEhTIjpbXSwieWF4aXNSSFMiOlsiY2hhcnQiLCLigIx2b2wgdW5kcuKAjCJdfX0sInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsImludGVydmFsIjoiZGF5In0sIm1haW50YWluUGVyaW9kaWNpdHkiOnRydWUsImZvcmNlTG9hZCI6dHJ1ZX0sImxpbmVXaWR0aCI6Miwic3RyaXBlZEJhY2tncm91bmQiOnRydWUsImV2ZW50cyI6dHJ1ZSwiY29sb3IiOiIjMDA4MWYyIiwic3RyaXBlZEJhY2tncm91ZCI6dHJ1ZSwiZXZlbnRNYXAiOnsiY29ycG9yYXRlIjp7ImRpdnMiOnRydWUsInNwbGl0cyI6dHJ1ZX0sInNpZ0RldiI6e319LCJjdXN0b21SYW5nZSI6bnVsbCwic3ltYm9scyI6W3sic3ltYm9sIjoiQUFQTCIsInN5bWJvbE9iamVjdCI6eyJzeW1ib2wiOiJBQVBMIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOnsibXVsdGlwbGllciI6MSwiYmFzZSI6InllYXIiLCJwZXJpb2RpY2l0eSI6eyJwZXJpb2QiOjEsImludGVydmFsIjoiZGF5In0sIm1haW50YWluUGVyaW9kaWNpdHkiOnRydWUsImZvcmNlTG9hZCI6dHJ1ZX19XSwic3R1ZGllcyI6eyLigIx2b2wgdW5kcuKAjCI6eyJ0eXBlIjoidm9sIHVuZHIiLCJpbnB1dHMiOnsiaWQiOiLigIx2b2wgdW5kcuKAjCIsImRpc3BsYXkiOiLigIx2b2wgdW5kcuKAjCJ9LCJvdXRwdXRzIjp7IlVwIFZvbHVtZSI6IiMwMGIwNjEiLCJEb3duIFZvbHVtZSI6IiNmZjMzM2EifSwicGFuZWwiOiJjaGFydCIsInBhcmFtZXRlcnMiOnsid2lkdGhGYWN0b3IiOjAuNDUsImNoYXJ0TmFtZSI6ImNoYXJ0IiwicGFuZWxOYW1lIjoiY2hhcnQifX0sIuKAjG1h4oCMICg1MCxDLG1hLDApIjp7InR5cGUiOiJtYSIsImlucHV0cyI6eyJQZXJpb2QiOjUwLCJGaWVsZCI6IkNsb3NlIiwiVHlwZSI6InNpbXBsZSIsIk9mZnNldCI6MCwiaWQiOiLigIxtYeKAjCAoNTAsQyxtYSwwKSIsImRpc3BsYXkiOiLigIxtYeKAjCAoNTAsQyxtYSwwKSJ9LCJvdXRwdXRzIjp7Ik1BIjoiI2UwOWMwMCJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19LCLigIxtYeKAjCAoMjAsQyxtYSwwKSI6eyJ0eXBlIjoibWEiLCJpbnB1dHMiOnsiUGVyaW9kIjoiMjAiLCJGaWVsZCI6IkNsb3NlIiwiVHlwZSI6InNpbXBsZSIsIk9mZnNldCI6MCwiaWQiOiLigIxtYeKAjCAoMjAsQyxtYSwwKSIsImRpc3BsYXkiOiLigIxtYeKAjCAoMjAsQyxtYSwwKSJ9LCJvdXRwdXRzIjp7Ik1BIjoiI2FkNmVmZiJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19fX0-")
        webbrowser.open("https://finance.yahoo.com/quote/"+i+"/chart?p="+i+"#eyJpbnRlcnZhbCI6ImRheSIsInBlcmlvZGljaXR5IjoxLCJ0aW1lVW5pdCI6bnVsbCwiY2FuZGxlV2lkdGgiOjQuMDEwNjAwNzA2NzEzNzgxLCJmbGlwcGVkIjpmYWxzZSwidm9sdW1lVW5kZXJsYXkiOnRydWUsImFkaiI6dHJ1ZSwiY3Jvc3NoYWlyIjp0cnVlLCJjaGFydFR5cGUiOiJsaW5lIiwiZXh0ZW5kZWQiOmZhbHNlLCJtYXJrZXRTZXNzaW9ucyI6e30sImFnZ3JlZ2F0aW9uVHlwZSI6Im9obGMiLCJjaGFydFNjYWxlIjoibGluZWFyIiwicGFuZWxzIjp7ImNoYXJ0Ijp7InBlcmNlbnQiOjAuNzYxOTA0NzYxOTA0NzYyLCJkaXNwbGF5IjoiTVJLIiwiY2hhcnROYW1lIjoiY2hhcnQiLCJpbmRleCI6MCwieUF4aXMiOnsibmFtZSI6ImNoYXJ0IiwicG9zaXRpb24iOm51bGx9LCJ5YXhpc0xIUyI6W10sInlheGlzUkhTIjpbImNoYXJ0Iiwi4oCMdm9sIHVuZHLigIwiXX0sIuKAjHJzaeKAjCAoMTQsQyktMiI6eyJwZXJjZW50IjowLjIzODA5NTIzODA5NTIzODA1LCJkaXNwbGF5Ijoi4oCMcnNp4oCMICgxNCxDKS0yIiwiY2hhcnROYW1lIjoiY2hhcnQiLCJpbmRleCI6MSwieUF4aXMiOnsibmFtZSI6IuKAjHJzaeKAjCAoMTQsQyktMiIsInBvc2l0aW9uIjpudWxsfSwieWF4aXNMSFMiOltdLCJ5YXhpc1JIUyI6WyLigIxyc2nigIwgKDE0LEMpLTIiXX19LCJzZXRTcGFuIjpudWxsLCJsaW5lV2lkdGgiOjIsInN0cmlwZWRCYWNrZ3JvdW5kIjp0cnVlLCJldmVudHMiOnRydWUsImNvbG9yIjoiIzAwODFmMiIsInN0cmlwZWRCYWNrZ3JvdWQiOnRydWUsInJhbmdlIjpudWxsLCJldmVudE1hcCI6eyJjb3Jwb3JhdGUiOnsiZGl2cyI6dHJ1ZSwic3BsaXRzIjp0cnVlfSwic2lnRGV2Ijp7fX0sImN1c3RvbVJhbmdlIjpudWxsLCJzeW1ib2xzIjpbeyJzeW1ib2wiOiJNUksiLCJzeW1ib2xPYmplY3QiOnsic3ltYm9sIjoiTVJLIiwicXVvdGVUeXBlIjoiRVFVSVRZIiwiZXhjaGFuZ2VUaW1lWm9uZSI6IkFtZXJpY2EvTmV3X1lvcmsifSwicGVyaW9kaWNpdHkiOjEsImludGVydmFsIjoiZGF5IiwidGltZVVuaXQiOm51bGwsInNldFNwYW4iOm51bGx9XSwic3R1ZGllcyI6eyLigIx2b2wgdW5kcuKAjCI6eyJ0eXBlIjoidm9sIHVuZHIiLCJpbnB1dHMiOnsiaWQiOiLigIx2b2wgdW5kcuKAjCIsImRpc3BsYXkiOiLigIx2b2wgdW5kcuKAjCJ9LCJvdXRwdXRzIjp7IlVwIFZvbHVtZSI6IiMwMGIwNjEiLCJEb3duIFZvbHVtZSI6IiNmZjMzM2EifSwicGFuZWwiOiJjaGFydCIsInBhcmFtZXRlcnMiOnsid2lkdGhGYWN0b3IiOjAuNDUsImNoYXJ0TmFtZSI6ImNoYXJ0IiwicGFuZWxOYW1lIjoiY2hhcnQifX0sIuKAjG1h4oCMICg1MCxDLG1hLDApIjp7InR5cGUiOiJtYSIsImlucHV0cyI6eyJQZXJpb2QiOjUwLCJGaWVsZCI6IkNsb3NlIiwiVHlwZSI6InNpbXBsZSIsIk9mZnNldCI6MCwiaWQiOiLigIxtYeKAjCAoNTAsQyxtYSwwKSIsImRpc3BsYXkiOiLigIxtYeKAjCAoNTAsQyxtYSwwKSJ9LCJvdXRwdXRzIjp7Ik1BIjoiI2UwOWMwMCJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19LCLigIxtYeKAjCAoMjAsQyxtYSwwKSI6eyJ0eXBlIjoibWEiLCJpbnB1dHMiOnsiUGVyaW9kIjoiMjAiLCJGaWVsZCI6IkNsb3NlIiwiVHlwZSI6InNpbXBsZSIsIk9mZnNldCI6MCwiaWQiOiLigIxtYeKAjCAoMjAsQyxtYSwwKSIsImRpc3BsYXkiOiLigIxtYeKAjCAoMjAsQyxtYSwwKSJ9LCJvdXRwdXRzIjp7Ik1BIjoiI2FkNmVmZiJ9LCJwYW5lbCI6ImNoYXJ0IiwicGFyYW1ldGVycyI6eyJjaGFydE5hbWUiOiJjaGFydCIsInBhbmVsTmFtZSI6ImNoYXJ0In19LCLigIxyc2nigIwgKDE0LEMpLTIiOnsidHlwZSI6InJzaSIsImlucHV0cyI6eyJQZXJpb2QiOjE0LCJGaWVsZCI6IkNsb3NlIiwiaWQiOiLigIxyc2nigIwgKDE0LEMpLTIiLCJkaXNwbGF5Ijoi4oCMcnNp4oCMICgxNCxDKS0yIn0sIm91dHB1dHMiOnsiUlNJIjoiI2FkNmVmZiJ9LCJwYW5lbCI6IuKAjHJzaeKAjCAoMTQsQyktMiIsInBhcmFtZXRlcnMiOnsic3R1ZHlPdmVyWm9uZXNFbmFibGVkIjp0cnVlLCJzdHVkeU92ZXJCb3VnaHRWYWx1ZSI6ODAsInN0dWR5T3ZlckJvdWdodENvbG9yIjoiIzc5ZjRiZCIsInN0dWR5T3ZlclNvbGRWYWx1ZSI6MjAsInN0dWR5T3ZlclNvbGRDb2xvciI6IiNmZjgwODQiLCJjaGFydE5hbWUiOiJjaGFydCJ9fX19")
        print(i)


main_screen()


