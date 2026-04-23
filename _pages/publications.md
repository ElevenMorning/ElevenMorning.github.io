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

Representative publications across face anti-spoofing and EDA. The list below highlights benchmark, dataset, explainability, and multimodal reasoning work in both directions.

## Face Anti-Spoofing
Selected work on spoof detection, forgery analysis, and explainable multimodal reasoning.

{% assign fas = pubs | where: "category", "FAS" %}
{% for post in fas %}
  {% include archive-single.html %}
{% endfor %}

## Electronic Design Automation
Selected work on AMS datasets, benchmarking, knowledge-enhanced design, and component generation.

{% assign eda = pubs | where: "category", "EDA" | sort: "order" %}
{% for post in eda %}
  {% include archive-single.html %}
{% endfor %}
