from render_engine.blog import Blog
from render_engine.page import Page
from render_engine.site import Site
from jinja2 import Environment, FileSystemLoader


class Site(Site):
    output_path = "output"
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

    engine = Environment(
        loader=FileSystemLoader(["site/templates", "templates"])
    )


if __name__ == "__main__":
    site = Site(static="static")

    @site.render_page
    class index(Page):
        template = "index.html"

    @site.render_collection
    class archive(Blog):
        has_archive = True
        output_path = "./"
        content_path = "./content"
        template = "new_post.html"
        archive_template: str = "archive.html"
