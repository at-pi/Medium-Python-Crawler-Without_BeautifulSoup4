from urllib.request import Request, urlopen
from multiprocessing.dummy import Pool as ThreadPool
import re
import html
import threading

arr = []
mydict = {}


def findlink(string1):
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = Request(url=string1, headers=headers)

    sock = urlopen(req)
    htmlSource = sock.read();
    sock.close();

    htmlPage = html.unescape(htmlSource.decode('utf_8'))
    # print(htmlPage)
    result = re.findall(r'.*?<a.*?href=\"([^#]*?)\".*?', htmlPage)

    #    print("List of URLs on this page: ")
    #    for i in result:
    #        if i:
    #            print(i)
    #            print("\n")


    mediumlist = []
    for i in result:
        if i.find("medium.com"):
            mediumlist.append(i)
    #mediumset={}
    #for i in result:
    #    if i.find("medium.com"):
    #        mediumset.add(i)
    #for i in mediumset:
    #    mediumlist.append(i)

    mediumlist = list(dict.fromkeys(mediumlist))

    for i in mediumlist:
        arr.append(i)

    print(len(arr))
    index=0
    for i in arr:
        print(index)
        print(i)
        print("\n")
        index=index+1
    with open('link.txt', 'a') as f:
        for item in arr:
            f.write("%s\n" % item)
    print("WRITTEN IN FILE")

if __name__ == "__main__":
    string1 = "https://medium.com"

    t1 = threading.Thread(target=findlink, args=(string1,))
    t1.start()
    t1.join()

    print(len(arr))

    i = 0
    while True:
        string1 = arr[i]
        t2 = threading.Thread(target=findlink, args=(string1,))
        t2.start()
        t2.join()
        i=i+1
        #if i==2:
        #   break


    #    for i in arr:
    #            print(i)
    #            print("\n")
    print("done")
