from render_engine.blog import Blog
from render_engine.page import Page
from render_engine.site import Site


class Site(Site):
    output_path = "output"
    site_vars: dict = {
        "GITHUB_URL": "https://github.com/Python-Community-News",
        "SITE_TITLE": "Python Community News",
        "SITE_URL": "https://pythoncommunitynews.com",
        "YOUTUBE_URL": "https://www.youtube.com/channel/UCA8N-T_aEhHLzwwn47K-UFw",
    }


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
