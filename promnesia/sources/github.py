"""
Indexes any links in my Github comments/issues/PRs
"""

from promnesia.common import Results, Visit, Loc
from promnesia.utils import extract_urls_http


def index() -> Results:
    from my.github.all import events

    for e in events():
        if isinstance(e, Exception):
            yield e
            continue
        if e.body is None:
            continue
        if e.link is not None:
            for url in extract_urls_http(e.body):
                yield Visit(
                    url=url,
                    dt=e.dt,
                    context=e.body,
                    locator=Loc.make(title=e.summary, href=e.link),
                )
