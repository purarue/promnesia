"""
Exposes post/metadata from random forums I used in the past
https://github.com/purarue/old_forums
"""

from promnesia.common import Results, Visit, Loc, iter_urls


def index() -> Results:
    from my.old_forums import forum_posts

    for p in forum_posts():
        desc = f"{p.forum_name} - {p.post_title}"
        loc = Loc(title=desc, href=p.post_url)
        # visit directly to this link
        yield Visit(url=p.post_url, dt=p.dt, locator=loc, context=p.post_contents)

        # visit to any links I mentioned in the contents
        for url in iter_urls(p.post_contents):
            yield Visit(
                url=url,
                dt=p.dt,
                locator=loc,
                context=p.post_contents,
            )
