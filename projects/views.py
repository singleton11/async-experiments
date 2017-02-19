from aiohttp import web
from sqlalchemy import select

from projects.serializers import ProjectSchema
from .models import Project


async def index(request: web.Request) -> web.Response:
    """Index view

    Args:
        request (web.Request): Request instance

    Returns:
        web.Response: Response instance

    """
    project_schema: ProjectSchema = ProjectSchema(many=True)

    async with request.app['db'].acquire() as conn:
        result = await conn.execute(select([Project]))
        return web.json_response(project_schema.dump(result).data)
