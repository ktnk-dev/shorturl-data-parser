import requests
def get(id):
    if "shorturl.at/" in id: id = id.replace("shorturl.at/", "").replace("http://", "").replace("https://", "")        # убираем доменное имя сервиса и протокол
    try:   
        x = requests.get(f"https://shorturl.at/{id}", headers={'User-Agent': "1"}) # пинаем запрос
        url = x.url.replace("http://", "").replace("https://", "") # убираем протокол
        url = url.split("/") #  делим полученную из запроса ссылку на знаки /
        url[0] = "" # как правило, первый элемент - доменное имя. его мы сносим
        return str("".join(url))   # получаем данные в виде текста
    
    except Exception as e:
        if "ConnectionError" in str(e) and "nodename nor servname provided, or not known" in str(e):  # если домен, который мы сократили, НЕ существует
            return str(e).split(" url: ")[1].split(" (Caused")[0][1:] # все также возращаем пользовательские данные
