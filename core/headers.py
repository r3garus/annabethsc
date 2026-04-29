import random
from fake_useragent import UserAgent


class HeaderFactory:
    def __init__(self):
        self.ua = UserAgent()
        self.platforms = ["Windows", "Macintosh", "X11", "iPhone", "Android"]
        self.languages = ["tr-TR,tr;q=0.9", "en-US,en;q=0.8", "de-DE,de;q=0.7", "fr-FR,fr;q=0.6"]

    def create_god_header(self):
        ver = random.randint(110, 126)
        platform = random.choice(self.platforms)

        # Gerçek bir tarayıcının tüm karmaşıklığını buraya döküyoruz sevgilim...
        headers = {
            "User-Agent": self.ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": random.choice(self.languages),
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-Ch-Ua": f'"Google Chrome";v="{ver}", "Chromium";v="{ver}", "Not=A?Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": f'"{platform}"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-For": f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}",
            "X-Real-IP": f"{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}",
            "DNT": "1"
        }
        return headers