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
    project_list = []
    async with request.app['db'].acquire() as conn:
        result = await conn.execute(select([Project]))

        for row in result:
            project_list.append({'id': row.id, 'title': row.title})
            # TODO: This have to be replaced to marshmallow deserializer

    return web.json_response(project_list)
