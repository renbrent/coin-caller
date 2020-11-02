import requests
import json
import sys

"""

"""

def main():
    endpoint = 'convert'
    access_key = 'API_KEY'
    current = 'JPY'
    to = 'USD'
    amount = '10'
    request = requests.get('https://data.fixer.io/api/'+endpoint+'?access_key='+access_key+'&from='
                           +current+'&to='+'&amount='+amount)
    

if __name__ == "__main__":
    main()