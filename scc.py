#Webscrapping
def wikisearch():
    import requests
    inp=input("Enter topic to search (divide words with '_'): ")
    url=f"https://en.wikipedia.org/wiki/{inp}"
    res=requests.get(url)
    from bs4 import BeautifulSoup
    import html5lib
    soup=BeautifulSoup(res.content,'html5lib')
    l=soup.find_all('p')
    nl=[]
    for i in l:
        nl.append(i.get_text())
    print(nl[1])
    print(nl[2])
    print(nl[3])
    
wikisearch()
    
    
