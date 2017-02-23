from json.decoder import JSONDecodeError
from typing import Dict, Tuple

import colander
from aiohttp import web
from sqlalchemy import insert, select, update

from .models import Project


class ProjectListView(web.View):
    """A list view for projects"""

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
                result = await conn.execute(insert(Project).values(
                    **deserialized_data
                ))
                project_id: int = await result.fetchone()
                deserialized_data.update({'id': project_id})
                return web.json_response(deserialized_data)
        except JSONDecodeError:
            return web.json_response({'error': 'This is not JSON'}, status=400)
        except colander.Invalid as e:
            return web.json_response(e.asdict(), status=400)


class ProjectDetailView(web.View):
    """A detail view for project"""

    async def get(self) -> web.Response:
        """Get project by id

        Returns:
            web.Response: Response

        """
        project_id: int = self.request.match_info['id']
        async with self.request.app['db'].acquire() as conn:
            result = await conn.execute(
                select([Project]).where(Project.id == project_id)
            )
            if not result.rowcount:
                return web.json_response({'error': 'Not Found'}, status=404)
            result: Tuple[int, str] = await result.fetchone()
            return web.json_response(
                Project.__colanderalchemy__.deserialize(result)
            )

    async def put(self) -> web.Response:
        """Update project

        Returns:
            web.Response: Response

        """
        try:
            project_id: int = self.request.match_info['id']
            data: Dict[str, int] = await self.request.json()
            deserialized_data: Dict[int, str] = \
                Project.__colanderalchemy__.deserialize(data)
            async with self.request.app['db'].acquire() as conn:
                await conn.execute(update(Project).values(
                    **deserialized_data
                ).where(Project.id == project_id))
                deserialized_data.update(dict(id=project_id))
                return web.json_response(deserialized_data)
        except JSONDecodeError:
            return web.json_response({'error': 'This is not JSON'}, status=400)
        except colander.Invalid as e:
            return web.json_response(e.asdict(), status=400)
