---
layout: archive
title: "Selected Publications"
permalink: /publications/
author_profile: true
---

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</div>
{% endif %}

{% include base_path %}

{% assign pubs = site.publications | sort: "date" | reverse %}

## FAS
{% assign fas = pubs | where: "category", "FAS" %}
{% for post in fas %}
  {% include archive-single.html %}
{% endfor %}

## EDA
{% assign eda = pubs | where: "category", "EDA" %}
{% for post in eda %}
  {% include archive-single.html %}
{% endfor %}

