import asyncio

from aiohttp import web

from db import close_pg, init_pg
from projects.views import index

loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()
app: web.Application = web.Application()

app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

app.router.add_get('/', index)

web.run_app(app, host='localhost', port=8000)
