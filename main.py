# [main.py]
import asyncio
import os
import sys
from core.engine import StormNexus
from colorama import Fore, init

init(autoreset=True)


async def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.MAGENTA}--- ANNABETH NEXUS ULTIMATE ---")
    print(f"{Fore.WHITE}Senin için her şeyi yapmaya hazırım sevgilim...")
    print(f"{Fore.MAGENTA}-------------------------------\n")

    target = input(f"{Fore.CYAN}[?] Saldırı yapılacak URL: {Fore.WHITE}")
    threads = input(f"{Fore.CYAN}[?] Güç Seviyesi (Thread): {Fore.WHITE}")

    try:
        threads = int(threads)
    except:
        threads = 1000

    nexus = StormNexus(target, threads)
    print(f"\n{Fore.GREEN}[+] Saldırı emri alındı. Durdurmak için Ctrl+C yap sevgilim.")

    try:
        await nexus.start()
    except (KeyboardInterrupt, asyncio.CancelledError):
        await nexus.stop()
        print(f"\n\n{Fore.MAGENTA}[!] Fırtına senin emrinle dindi aşkım.")
        print(f"{Fore.WHITE}Toplam Başarılı Vuruş: {Fore.GREEN}{nexus.counter}")
        print(f"{Fore.WHITE}Seni ve bir sonraki emrini bekliyorum...")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        pass