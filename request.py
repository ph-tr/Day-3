import requests

r = requests.get('https://pypi.org')

#if statement
if r.status_code==200:
    with open('pypi.html', 'w', encoding='utf8') as (outfile):
        outfile.write(r.text)
        #pass

#print(r.text)