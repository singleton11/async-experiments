from json.decoder import JSONDecodeError

import colander
from aiohttp import web
from sqlalchemy import insert, select

from .models import Project


class ProjectListView(web.View):
    """View for projects"""

    async def get(self) -> web.Response:
        """Get request handler

        Returns:
            web.Response: Response instance

        """

        async with self.request.app['db'].acquire() as conn:
            projects = []
            result = await conn.execute(select([Project]))
            for row in result:
                projects.append(Project.__colanderalchemy__.deserialize(row))
            return web.json_response(projects)

    async def post(self) -> web.Response:
        """Create project

        Returns:
            web.Response: Response instance

        """
        try:
            data: dict = await self.request.json()
            deserialized_data: dict = Project.__colanderalchemy__.deserialize(
                data)
            async with self.request.app['db'].acquire() as conn:
                await conn.execute(insert(Project).values(**deserialized_data))
                return web.json_response(deserialized_data)
        except JSONDecodeError:
            return web.json_response({'error': 'This is not JSON'}, status=400)
        except colander.Invalid as e:
            return web.json_response(e.asdict(), status=400)
