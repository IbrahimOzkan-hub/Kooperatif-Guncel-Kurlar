import pandas as pd
from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.koopbank.com/inmotion/doviz/mobil.php?lang=tr-tr')

soup = BeautifulSoup(page.content, 'html.parser')


container = soup.find(id='pagemain')

currTyp = container.find_all(class_='mt1')
currVal = container.find_all(class_='mt2')

currName = [typ.get_text() for typ in currTyp]
currValue = [val.get_text() for val in currVal]

kur_anlik = pd.DataFrame(
    {'currName': currName,
    'currValue': currValue}
)

kur_anlik.to_csv('kur.csv')

