## promnesia

This lets me use [my HPI modules](https://github.com/purarue/HPI) as additional `Source`s for [promnesia](https://github.com/karlicoss/promnesia).

It indexes any URLs it finds in my:

- Discord messages, [parsed from the data export](https://github.com/purarue/discord_data)
- Browser history from backups of my firefox/chrome/safari browser histories (using [browserexport](https://github.com/purarue/browserexport))
- Podcasts/Videos I watched with mpv (tracked by [this](https://github.com/purarue/mpv-history-daemon))
- Movies/TV Show episodes tracked by my [trakt](https://github.com/purarue/traktexport)
- Anime/Manga using [malexport](https://github.com/purarue/malexport)
- Shell histories (zsh, bash, ipython, [ttt](https://github.com/purarue/ttt))
- Git commits on my system
- Todo.txt files
- Mail, using local IMAP/MBOX backups
- Albums [I've listened to](https://purarue.xyz/s/albums)
- Facebook Messages
- comments from some [old forums](https://github.com/purarue/forum_parser) I used to be on
- pageview history from the [twitch privacy export](https://github.com/purarue/HPI/blob/master/my/twitch/gdpr.py)
- video games I've logged to [grouvee](https://www.grouvee.com/), using [grouvee export](https://github.com/purarue/grouvee_export)

To use these, import the source and add it to the `SOURCES` array in your promnesia config. See mine [here](https://purarue.xyz/d/promnesia/config.py?redirect)

### Install

For the time being, this doesn't install as a namespace package alongside `promnesia`, it just installs a separate module, `promnesia_pura`. See the comments [here](https://github.com/karlicoss/promnesia/pull/225) for more info.

To Install:

- Assumes you have both [karlicoss/HPI](https://github.com/karlicoss/HPI) and [my HPI](https://github.com/purarue/HPI) modules installed
- Setup [`promnesia`](https://github.com/karlicoss/promnesia)
- Install this; `python3 -m pip install git+https://github.com/purarue/promnesia`

If you have issues importing/installing this, try a local install instead. See [troubleshooting docs](https://github.com/purarue/HPI/blob/master/doc/TROUBLESHOOTING_INSTALLS.md)

In your config file, to enable these sources, import from `promnesia_pura`. You can see my [config file](https://purarue.xyz/d/promnesia/config.py?redirect) as an example
