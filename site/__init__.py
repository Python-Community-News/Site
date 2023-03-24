from pathlib import Path

import pytailwindcss
from jinja2 import Environment, FileSystemLoader, StrictUndefined
from render_engine.blog import Blog
from render_engine.feeds import RSSFeed
from render_engine.page import Page
from render_engine.parsers.markdown import MarkdownPageParser
from render_engine.site import Site
from render_engine_tailwindcss import TailwindCSS


class Site(Site):
    output_path = "output"
    static_path = "static"
    site_vars: dict = {
        # TODO: add a new page type that will pull this content in on
        # build and render it as part of the site.
        "CODE_OF_CONDUCT_URL": "https://github.com/Python-Community-News/.github/blob/main/CODE_OF_CONDUCT.md",
        "GITHUB_URL": "https://github.com/Python-Community-News",
        "PODCAST_URL": "https://pythoncommunitynews.transistor.fm",
        "SITE_TITLE": "Python Community News",
        "SITE_URL": "https://pythoncommunitynews.com",
        "YOUTUBE_URL": "https://www.youtube.com/channel/UCA8N-T_aEhHLzwwn47K-UFw",
    }

    plugins = [
        TailwindCSS,
    ]

    @property
    def engine(self) -> Environment:
        env = super().engine
        env.loader.loaders.insert(
            0, FileSystemLoader(["website/templates", "templates"])
        )
        # NOTE: it seems that setting StrictUndefined now breaks the
        # rss rendering. This is temporarily disabled for the sake of
        # development until it can be fixed properly.
        # env.undefined = StrictUndefined
        return env


class Feed(RSSFeed):
    extension = ".xml"


site = Site()


@site.page
class index(Page):
    template = "index.html"


@site.page
class rss_redirect_notice(Page):
    template = "python-community-news-archive.rss"

    @property
    def url(self):
        return Path("python-community-news-archive.rss")


@site.collection
class archive(Blog):
    PageParser = MarkdownPageParser
    has_archive = True
    output_path = "./"
    content_path = "content"
    template = "new_post.html"
    archive_template: str = "archive.html"
    feed = Feed
