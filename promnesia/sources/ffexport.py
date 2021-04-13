"""
firefox export - my browsing history
https://github.com/seanbreckenridge/ffexport
"""

# named diffrently to prevent conflicts with upstream promnesia

from promnesia.common import Results, Visit, Loc, extract_urls


def index() -> Results:
    from my.browsing import history

    for v in history():
        yield Visit(
            url=v.url,
            dt=v.visit_date,
            locator=Loc(title=v.title or f"Firefox - {v.url}", href=v.url),
            context=v.description,
        )
