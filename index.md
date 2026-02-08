---
layout: home
author_profile: false
---

## Projects

{% for post in site.posts %}
- [{{ post.title }}]({{ post.url }})
{% endfor %}
