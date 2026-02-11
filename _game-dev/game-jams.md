---
title: Game Jams
excerpt: Games made in less than a week!
header:
  teaser: /assets/images/game-dev/game-jams/game-jams-thumb.gif
layout: single
---
When I first heard about what a "game jam" was from watching a GMTK video, I fell in love. I desperately wanted to try one. I spent all my free time learning game development, and in February of 2020, I created [my first game](https://itch.io/jam/mini-jam-47-internet/rate/565834) in 72 hours, and got 3rd place overall out of 54 entries!

Head over to my [itch.io page](https://blackopsben.itch.io/) to play all of my games!

{% for game in site["game-jams"] %}

<div style="display: flex; gap: 20px; margin-bottom: 40px; align-items: flex-start;">

  <div style="flex: 0 0 250px;">
    <img src="{{ game.thumb }}" alt="{{ game.title }}">
  </div>

  <div>
    <h2>{{ game.title }}</h2>
    <p>{{ game.excerpt }}</p>

    {% if game.itch %}
      <p><a href="{{ game.itch }}">Play on itch.io</a></p>
    {% endif %}
  </div>

</div>

{% endfor %}
