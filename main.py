import pandas as pd
from bs4 import BeautifulSoup
import requests


page = requests.get('https://www.koopbank.com/inmotion/doviz/mobil.php?lang=tr-tr')

soup = BeautifulSoup(page.content, 'html.parser')


container = soup.find(id='pagemain')

kurCins = container.find_all(class_='mt1')
kurDeger = container.find_all(class_='mt2')

kurIsim = [cins.get_text() for cins in kurCins]
kurDeger = [deger.get_text() for deger in kurDeger]

kur_anlik = pd.DataFrame(
    {'kurisim': kurIsim,
    'kurdeger': kurDeger}
)

print(kur_anlik)

kur_anlik.to_csv('kur.csv')

