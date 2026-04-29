import random
import string


class PacketMutator:
    @staticmethod
    def generate_random_payload(size=1024):
        """Sunucunun analiz motorunu yoracak anlamsız veri yığını."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

    @staticmethod
    def get_mutated_headers():
        """Her vuruşta kimlik değiştiren dinamik başlıklar."""
        os_list = ["Windows NT 10.0; Win64; x64", "X11; Linux x86_64", "Macintosh; Intel Mac OS X 14_4"]
        browsers = ["Chrome/124.0.0.0", "Firefox/125.0", "Safari/605.1.15"]

        headers = {
            "User-Agent": f"Mozilla/5.0 ({random.choice(os_list)}) AppleWebKit/537.36 (KHTML, like Gecko) {random.choice(browsers)}",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9,tr;q=0.8",
            "Cache-Control": "no-cache",
            "X-Forwarded-For": f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
            "X-Requested-With": "XMLHttpRequest",
            "DNT": "1"
        }
        return headers