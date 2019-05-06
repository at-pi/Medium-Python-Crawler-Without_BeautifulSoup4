# Medium-Python-Crawler
A Web crawler which gathers the link present in the articles of medium.com and further goes on until stopped manually.

Requirements -

1 Python 3
2 urlib.request - URL manipulation library
3 re - regular expression library
4 threading - Thread library in python
5 multiprocessing - Multi threading library in python

Objective - To gather the link present in the articles of medium.com

Description - It is a Web Crawler which operated in Medium.com From the base page it mines the links present in the articles and from that further links are extracted from which new articles are reached and more links are extracted and the recursive process goes on until a manual interrupt in provided.

TODO - 
add concurrent connection - which makes 5 thread to work in concurrent manner which means that 5 connection are established whichextracts the further links concurrently.
