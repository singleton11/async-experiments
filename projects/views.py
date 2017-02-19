from aiohttp import web


async def index(request: web.Request) -> web.Response:
    """Index view

    Args:
        request (web.Request): Request instance

    Returns:
        web.Response: Response instance

    """

    return web.json_response({'hello': 'world'})
