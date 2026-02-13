---
title: Game Jams
excerpt: Games made in less than a week!
header:
  teaser: /assets/images/game-dev/game-jams/game-jams-thumb.gif
layout: single
classes: wide
---
When I first heard about what a "game jam" was from watching a GMTK video, I fell in love. I desperately wanted to try one. I spent all my free time learning game development, and in February of 2020, I created [my first game](https://itch.io/jam/mini-jam-47-internet/rate/565834) in 72 hours, and got 3rd place overall out of 54 entries!

Head over to my [itch.io page](https://blackopsben.itch.io/) to play all of my games!

{% for game in site["game-jams"] reversed %}

<article style="margin-bottom: 60px; padding: 30px; border-radius: 12px; box-shadow: 0 6px 20px rgba(0,0,0,0.08);">

  <h2 style="margin-bottom: 20px;">
    {% if game.itch %}
      <a href="{{ game.itch }}">{{ game.title }}</a>
    {% else %}
      {{ game.title }}
    {% endif %}
  </h2>

  <!-- IMAGE LAYOUT -->
  <div style="display: flex; flex-wrap: wrap; gap: 20px; margin-bottom: 20px;">

    <!-- HERO IMAGE -->
    <div style="flex: 2 1 400px;">
      <img src="{{ game.thumb | relative_url }}"
           alt="{{ game.title }}"
           style="width: 100%; height: auto; border-radius: 10px;">
    </div>

    <!-- 2x2 SCREENSHOT GRID -->
    <div style="flex: 1 1 300px; display: flex; flex-wrap: wrap; gap: 10px;">

      {% for shot in game.screenshots %}
        <div style="flex: 1 1 calc(50% - 10px);">
          <img src="{{ shot | relative_url }}"
               alt="{{ game.title }} screenshot"
               style="width: 100%; height: auto; border-radius: 6px;">
        </div>
      {% endfor %}

    </div>

  </div>

  <!-- TEXT CONTENT -->
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

<hr style="margin: 50px 0; opacity: 0.15;">

{% endfor %}
