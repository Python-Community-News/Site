---
title: {{issue.title}} - Python Community News {{issue.episode_date}}
slug: "{{issue.episode_date}}"
date: {{issue._created_at}}
{% if issue['podcast'] %}podcast: {{issue.podcast}}
{% endif %}{% if issue['youtube'] %}youtube: {{issue.youtube}}{% endif %}
---

{% for topic in issue.get_content_issues("issues") %}
### [{{topic.title}}]({{topic.url}})

submitted by [{{topic._user.login}}]({{topic._user.html_url}}) on {{topic._created_at}}

{{topic.summary}}

{% endfor %}

{% for topic in issue.get_content_issues("shorts") %}
### [{{topic.title}}]({{topic.url}})

submitted by [{{topic._user.login}}]({{topic._user.html_url}}) on {{topic._created_at}}

{{topic.summary}}

<iframe width="560"
                height="315"
                src="https://www.youtube.com/embed/{{topic.youtube}}"
                title="YouTube video player"
                frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen></iframe>

{% endfor %}

{% set conferences = issue.get_content_issues("conferences")|list %}

{% if conferences %}

## Conferences and Events

{% for conference in conferences %}
### [{{conference.title}}]({{conference.url}})

submitted by [{{conference._user.login}}]({{conference._user.html_url}}) on {{conference._created_at}}

{% if conference['summary'] %}
{{conference.summary}}
{% endif %}
{% endfor %}
{% endif %}
