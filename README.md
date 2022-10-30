# Python Community News (Site)

This is the repo for the [Python Community News](https://pythoncommunitynews.com) site.
## Community Standards

This project adheres to the standards highlighted in the [organization repo](https://github.com/python-community-news/.github). You should be able to find the code of conduct, contributing guidelines, and other community standards in the **GitHub Interface** or the [organization repo](https://github.com/python-community-news/.github).

## How it works

### Episodes come from [Topics](https://github.com/python-community-news)

You each episode is built from [issues in the topics repo](https://github.com/Python-Community-News/Topics/issues?q=is%3Aissue+label%3Apublish). These issues converted into a markdown file using [GH-Issues](https://github.com/python-community-news/gh-issues)

Those generated markdown files are then published to the website using [Render Engine](https://github.com/kjaymiller/render_engine).