---
title: Game Jams
excerpt: Games made in less than a week!
header:
  teaser: /assets/images/game-dev/game-jams/game-jams-thumb.gif
layout: single
---
When I first heard about what a "game jam" was from watching a GMTK video, I fell in love. I desperately wanted to try one. I spent all my free time learning game development, and in February of 2020, I created [my first game](https://itch.io/jam/mini-jam-47-internet/rate/565834) in 72 hours, and got 3rd place overall out of 54 entries!

Head over to my [itch.io page](https://blackopsben.itch.io/) to play all of my games!

{% for game in site["game-jams"] reversed %}

<article style="margin-bottom: 60px; padding: 30px; border: 1px solid #ddd; border-radius: 12px;">

  <h2 style="margin-bottom: 20px;">
    {% if game.itch %}
      <a href="{{ game.itch }}">{{ game.title }}</a>
    {% else %}
      {{ game.title }}
    {% endif %}
  </h2>

  <!-- Images -->
  <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 20px;">

    <div style="flex: 1 1 300px;">
      <img src="{{ game.thumb | relative_url }}" 
           alt="{{ game.title }}" 
           style="width: 100%; height: auto; border-radius: 8px;">
    </div>

    <div style="flex: 1 1 300px;">
      <img src="{{ game.sample | relative_url }}" 
           alt="{{ game.title }} gameplay" 
           style="width: 100%; height: auto; border-radius: 8px;">
    </div>

  </div>

  <!-- Text -->
  <p style="opacity: 0.6; font-size: 0.9em;">
    {{ game.date | date: "%B %Y" }}
  </p>

  <p>{{ game.excerpt }}</p>

  {% if game.itch %}
    <p>
      <a href="{{ game.itch }}" class="btn btn--primary">
        Play on itch.io
      </a>
    </p>
  {% endif %}

</article>

<hr style="margin: 40px 0; opacity: 0.2;">

{% endfor %}
