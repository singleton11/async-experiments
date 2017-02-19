from typing import Dict, List

import peewee_async
from aiohttp import web

from .models import Project, database


async def index(request: web.Request) -> web.Response:
    """Index view

    Args:
        request (web.Request): Request instance

    Returns:
        web.Response: Response instance

    """
    objects: peewee_async.Manager = peewee_async.Manager(database)
    project_list: List[Dict] = []
    results: List[Project] = await objects.execute(Project.select())

    for project in results:
        project_list.append({'id': project.id, 'title': project.title})

    return web.json_response(project_list)
