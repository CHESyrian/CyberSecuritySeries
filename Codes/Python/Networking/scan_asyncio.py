#!/usr/bin/env python3
import asyncio

async def scan_port(ip, port, timeout=1.0):
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection(ip, port), timeout=timeout
        )
        writer.close()
        try:
            await writer.wait_closed()
        except AttributeError:
            pass
        return port, True
    except Exception:
        return port, False

async def scan_ports(ip, ports, concurrency=500):
    sem = asyncio.Semaphore(concurrency)
    async def sem_scan(p):
        async with sem:
            return await scan_port(ip, p)

    tasks = [asyncio.create_task(sem_scan(p)) for p in ports]
    results = await asyncio.gather(*tasks)
    return [p for p, ok in results if ok]

if __name__ == "__main__":
    ip = "192.168.1.1"
    ports = range(1, 1025)
    open_ports = asyncio.run(scan_ports(ip, ports))
    print("Open ports:", open_ports)
