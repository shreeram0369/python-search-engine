# Modules
"""
pip install google
pip install beautifulsoup4

"""
# funcation and its parameters
"""
funcation name = Search(query,tid,num,stop,pause)
query : query string that we want to search for.
tld : tid stands for top level domain which means we want to search our resualt on google.com or google.in or some other domain
num : Number of results we want 
stop : last result to retrieve. use none to keep searching forever 
pause : lapse to wait between HTTP Requests.
"""
try:
    from googlesearch import search
except ImportError:
    print("module not found")    

query = input("enter your your query")

for i in search(query,tld="com",num=10,stop=10,pause=2 ):
    print(i)
