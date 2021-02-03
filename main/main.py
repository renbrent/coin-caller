import requests
import json
import sys

"""

"""

def main():
    endpoint = 'latest'
    access_key = ''
    base = 'EUR'
    symbols = 'USD,JPY'
    request = requests.get('http://data.fixer.io/api/'+endpoint+'?access_key='+access_key+\
                           '&base='+base+'&symbols='+symbols)
    print(request.status_code)
    print(request.json())
    

if __name__ == "__main__":
    main()