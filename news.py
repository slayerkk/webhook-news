import requests
import json
import time
#coloque aqui a sua api do https://newsapi.org/
api_key = "API KEY AQUI"

#coloque aqui o URL do seu webhook discord
discord_webhook_url = "WEBHOOK AQUI"
def send_discord_message(content):
    payload = {
        "content": content
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(discord_webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code != 204:
        print("Erro ao enviar mensagem para o Discord:", response.text)

def fetch_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={api_key}"
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            news_articles = data["articles"]

            for article in news_articles:
                title = article["title"]
                description = article["description"]
                url = article["url"]
                #configure a sua mensagem aqui, o padrão é este.
                message = f"""
                                
> **{title}**

> CLIQUE AQUI PARA LER A NOTICIA [NOTICIA]({url})

> BY: Slayer

"""
                send_discord_message(message)

    except requests.exceptions.RequestException as e:
        print("Erro ao buscar notícias:", str(e))

if __name__ == "__main__":
    while True:
        fetch_news()
        #configure de quanto em quanto tempo as noticias serão enviadas, o padrão é 24Hrs. (86400 segundos)
        time.sleep(86400)
