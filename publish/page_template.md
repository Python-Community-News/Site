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
