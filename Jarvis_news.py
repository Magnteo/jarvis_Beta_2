import feedparser

def get_news_titels():
    url = "https://news.google.com/rss?hl=uk&gl=UA&ceid=UA:uk"
    feed = feedparser.parse(url)
    titles = [entry.title for entry in feed.entries[:5]]
    return titles

def speak_news():
    from jarvis_voice import speak
    titles = get_news_titels()
    for i , title in enumerate(titles , start=1):
        print(f"Новина {i} {title}")
        speak(f"Новина {i} {title}")
