from pypresence import Presence
import time
import requests
import random

buton1_yazi = "1. Buton Yazı"
buton1_link = "1. Buton link"

buton2_yazi = "2. Buton Yazı"
buton2_link = "2. Buton Link"

doviz = {0:{"kur": "dolar", "state": "1 Dolar ($): "},
         1:{"kur": "euro", "state": "1 Euro (€): "},
         2:{"kur": "altin", "state": "Gram Altın: "},
         3:{"kur": "sterlin", "state": "1 Sterlin (£): "}}

client_id = "924595836657209425"
RPC = Presence(client_id)
RPC.connect()
butonlar = [{"label": buton1_yazi,
                     "url": buton1_link},
             {"label": buton2_yazi,
                     "url": buton2_link}]

while True:
    veri = requests.get("https://api.bigpara.hurriyet.com.tr/doviz/headerlist/anasayfa")
    kur = random.choice(doviz)
    if kur["kur"] == "dolar":
        fiyat = veri.json()["data"][6]["SATIS"]
    elif kur["kur"] == "euro":
        fiyat = veri.json()["data"][3]["SATIS"]
    elif kur["kur"] == "sterlin":
        fiyat = veri.json()["data"][7]["SATIS"]
    elif kur["kur"] == "altin":
        fiyat = veri.json()["data"][5]["SATIS"]
    state = kur["state"] + str(fiyat)
    RPC.update(state=state,
               large_image=kur["kur"],
               buttons=butonlar)
    time.sleep(20)
