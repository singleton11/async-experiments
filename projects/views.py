from aiohttp import web
from sqlalchemy import select

from projects.serializers import ProjectSchema
from .models import Project


class ProjectView(web.View):
    async def get(self) -> web.Response:
        """Get request handler

        Returns:
            web.Response: Response instance

        """
        project_schema: ProjectSchema = ProjectSchema(many=True)

        async with self.request.app['db'].acquire() as conn:
            result = await conn.execute(select([Project]))
            return web.json_response(project_schema.dump(result).data)
