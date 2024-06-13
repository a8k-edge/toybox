import asyncio

import aiohttp


URL = 'wss://ws2.bybit.com/spot/ws/quote/v2?timestamp=1718272795503'
HEADERS = {
    "Cache-Control": "no-cache",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Origin": "https://www.bybit.com",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,fr;q=0.6,uk;q=0.5,ar;q=0.4,de;q=0.3",
    "Sec-WebSocket-Extensions": "permessage-deflate; client_max_window_bits",
}


async def main():
    session = aiohttp.ClientSession(headers=HEADERS)
    async with session.ws_connect(URL) as ws:
        await ws.send_json({
            "topic": "slowBroker",
            "event": "sub"
        })
        async for msg in ws:
            print(f"Got message:", msg)
            if msg.type in (aiohttp.WSMsgType.CLOSED,
                            aiohttp.WSMsgType.ERROR):
                break

loop = asyncio.get_event_loop()
loop.run_until_complete(main())