print('ctrl + click')
try: 
    from googlesearch import search 
    import googlesearch
except ImportError:  
    print("No module named 'google' found") 
tk = input('help with internet: ')
query = tk
lik = input('language: ')
lyu = 1
for j in googlesearch.search(query, tld="co.in", num=lyu,lang=lik, stop=0, pause=0): 
    print(j)