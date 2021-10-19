"""
Indexes any links found in my emails
"""

from typing import Set, List
from datetime import date

from my.core.common import mcachew
from promnesia.common import Results, Visit, Loc, iter_urls


def parse_person(m: List[List[str]]) -> str:
    """
    e.g.:
    [
        [
            "",
            "emailhere@gmail.com"
        ]
    ]
    """
    if m:
        if m[0]:
            return m[0][1]
    return ""


# cache this once every month, it takes about half an hour
@mcachew(depends_on=lambda: date.today().month)
def index(*, body_as_context: bool = False) -> Results:
    from my.imap import mail

    for m in mail():

        if m.dt is None:
            continue

        emitted: Set[str] = set()
        desc = f"""{parse_person(m.from_)} {parse_person(m.to)} - {m.subject}"""

        for body in (
            m.body,
            m.body_plain,
            m.body_html,
        ):
            for url in iter_urls(body):
                if url in emitted:
                    continue
                emitted.add(url)
                # if the entire body is included as the context, for large enough IMAP
                # sync dirs (e.g. mine) this makes the promnesia index about 300 gigabytes
                # therefore, the default is to just use the filepath as the context,
                # and I can go look at it if I want to
                ctx = (
                    body
                    if body_as_context
                    else str(m.filepath.absolute())
                    if m.filepath is not None
                    else ""
                )
                yield Visit(
                    url=url,
                    dt=m.dt,
                    context=ctx,
                    locator=Loc(title=desc, href=url),
                )
