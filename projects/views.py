from aiohttp import web
from sqlalchemy import select

from .models import Project


async def index(request: web.Request) -> web.Response:
    """Index view

    Args:
        request (web.Request): Request instance

    Returns:
        web.Response: Response instance

    """
    async with request.app['db'].acquire() as conn:
        project_list = await conn.execute(select([Project]))

    return web.json_response({'hello': 'world'})
