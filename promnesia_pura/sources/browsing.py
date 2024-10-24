"""
merges my browsing history
https://github.com/purarue/browserexport
https://github.com/karlicoss/HPI/tree/master/my/browser
"""

from promnesia.common import Results, Visit, Loc


def index() -> Results:
    from my.browser.all import history

    for v in history():
        desc = None
        if v.metadata is not None:
            desc = v.metadata.title
        yield Visit(
            url=v.url,
            dt=v.dt,
            locator=Loc(title=desc or v.url, href=v.url),
        )
