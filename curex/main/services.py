import requests

r = requests.get('https://www.nbrb.by/api/exrates/rates?periodicity=0').json()

currencies = {cur['Cur_Abbreviation']: cur for cur in r}
currencies['BYN'] = {'Cur_Abbreviation': 'BYN', 'Cur_Scale': 1, 'Cur_Name': 'Белорусских рублей'}
del currencies['XDR']
