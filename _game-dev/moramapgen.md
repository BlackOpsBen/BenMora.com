---
title: MoraMapGen
excerpt: Procedurally generated dungeon room and corridor layouts
header:
  teaser: /assets/images/game-dev/moramapgen/moramapgen-thumb.gif
  #video:
    #id: 5qo8odfwXk4
    #provider: youtube
layout: single
classes: wide
---
Procedural Rooms and Corridors Layout Generator

{% include video id="5qo8odfwXk4" provider="youtube" %}

[Get it on the Unity Asset Store](https://assetstore.unity.com/packages/slug/289878)

This is a tool I created for the game I am developing. It uses Wave-Function Collapse (WFC) to generate layouts of rooms and corridors based on sprite templates.

![image-right]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/wfc-animated-example.gif)
Here's an animated example of what happens instantly:
1. Bounds are defined
2. WFC fills the interior
3. Corridors are removed
4. Excessively large rooms are split
5. Tiny rooms are removed
6. New corridor paths are created
All of the above are based on your settings.

![image-center]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/reskin-duos.gif)

![image-center]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/min-modules.png)
You define the look of the maps by providing your own prefabs. At a minimum you'll need the following:
* Straight wall
* Inside corner wall
* Outside corner wall
* Floor
* Optional: Interior and/or exterior ceilings