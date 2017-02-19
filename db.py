from aiohttp import web
from aiopg.sa import Engine, create_engine


async def init_pg(app: web.Application):
    """Initialize async pg engine

    Args:
        app (web.Application): Application instance

    """
    engine: Engine = await create_engine(
        database='async-lab',
        user='async-lab',
        password='async-lab',
        host='postgres',
        loop=app.loop
    )
    app['db'] = engine


async def close_pg(app: web.Application):
    """Close async PG engine

    Args:
        app (web.Application): Application instance

    """
    app['db'].close()
    await app['db'].wait_closed()
