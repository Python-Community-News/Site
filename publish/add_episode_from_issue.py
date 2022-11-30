import os
import pathlib

import typer
from gh_issues import Issue, Repo
from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("publish"))

PCN = Repo("python-community-news", "topics")


def run(issue_number: int):
    template = environment.get_template("page_template.md")
    current_issue = Issue.from_issue_number(
        repo=PCN,
        issue_number=issue_number,
        api_token=os.environ.get("GITHUB_TOKEN", None),
    )
    return pathlib.Path(f"site/content/{current_issue.episode_date}.md").write_text(
        template.render(issue=current_issue)
    )


if __name__ == "__main__":
    typer.run(run)
