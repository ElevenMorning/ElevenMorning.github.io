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

<div class="publications-page">

Representative publications across face anti-spoofing and EDA. The list below highlights benchmark, dataset, explainability, and multimodal reasoning work in both directions.

<h2 class="pub-section-title">Face Anti-Spoofing</h2>
<p class="pub-section-desc">Selected work on spoof detection, forgery analysis, and explainable multimodal reasoning.</p>

{% assign fas = pubs | where: "category", "FAS" %}
{% for post in fas %}
  {% include archive-single.html %}
{% endfor %}

<h2 class="pub-section-title">Electronic Design Automation</h2>
<p class="pub-section-desc">Selected work on AMS datasets, benchmarking, knowledge-enhanced design, and component generation.</p>

{% assign eda = pubs | where: "category", "EDA" | sort: "order" %}
{% for post in eda %}
  {% include archive-single.html %}
{% endfor %}

</div>
