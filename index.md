---
title: Home
layout: home
entries_layouit: grid
paginate: 3
---
{% assign sections = site.pages | where_exp: "p", "p.layout != 'home'" | where_exp: "p", "p.url == '/illustration/' or p.url == '/gamedev/' or p.url == '/animation/'" %}

<div class="entries-grid">
  {% for page in sections %}
    {% include archive-single.html type="grid" %}
  {% endfor %}
</div>
