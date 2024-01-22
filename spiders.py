#!/usr/bin/env python3

import requests,sys,re
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from termcolor import colored

f = Figlet(font ="standard")
print(colored(f.renderText("Web Spiders"),"green"))
print("Github:https://github.com/skynet10\n")
info =  input("Type in what you want to search for: ").strip()

try:
    args = sys.argv[1]
    with open(args,"r") as txt:
       txt = txt.readlines()
       for t in txt:
            t = t.strip()
            headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"}
            r = requests.get(t,headers=headers)
            soup = (BeautifulSoup(r.content,"html.parser",))
            x = "Response"
            print(f"\n{x:-<100}\n" + f"{t} -----> Status:{r.status_code}\n")
            body = soup.find_all(info)

            for y in body:
                    respost = re.compile(r"https?://([a-zA-Z0-9])([./a-zA-z0-9])*([./a-zA-Z0-9])*([./a-zA-Z0-9])*")
                    response = respost.finditer(str(y))
                    for z in response:
                         print(f"{y}\n")

            for z in body:
                     respost = re.compile(r"([/.a-zA-Z0-9])([./a-zA-z0-9])*([./a-zA-Z0-9])*([./a-zA-Z0-9])*")
                     response = respost.finditer(str(z))
                     for z in response:
                          print(f"{z}")

except IndexError:
      print("\nEnter a file!\n")

except requests.exceptions.InvalidSchema:
      print("\nThe file contains invalid URLs!\n")

except requests.exceptions.MissingSchema:
      print("\nInvalid file!\n")

except ModuleNotFoundError:
      print("Modules not detected!. Install the file requirements.txt [pip install -r requirements.txt]")



