import re

from .bugtracker import bug


async def bugtracker(name):
    try:
        q = re.match(r'^bug (.*)\-(.*)', name)
        return (await bug(q.group(1) + '-' + q.group(2)))
    except Exception as e:
        return (str(e))
