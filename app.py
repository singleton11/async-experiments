import asyncio

from aiohttp import web

loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
app: web.Application = web.Application()

web.run_app(app, host='localhost', port=8000)
