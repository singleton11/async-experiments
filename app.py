import asyncio

from aiohttp import web

from projects.views import index

loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
app: web.Application = web.Application()

app.router.add_get('/', index)

web.run_app(app, host='localhost', port=8000)
