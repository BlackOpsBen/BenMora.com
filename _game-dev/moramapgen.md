---
title: MoraMapGen
excerpt: Procedurally generated dungeon room and corridor layouts
header:
  teaser: /assets/images/game-dev/moramapgen/moramapgen-thumb.png
  #video:
    #id: 5qo8odfwXk4
    #provider: youtube
layout: single
classes: wide
---
Procedural Rooms and Corridors Layout Generator

{% include video id="5qo8odfwXk4" provider="youtube" %}

[Get it on the Unity Asset Store](https://assetstore.unity.com/packages/slug/289878)

[Watch the tutorial](https://youtu.be/ky3gvNfGBI0)

This is a tool I created for the game I am developing. It uses Wave-Function Collapse (WFC) to generate layouts of rooms and corridors based on sprite templates.

![Animated example of WFC]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/wfc-animated-example.gif){: .align-right}
Here's an animated example of what happens instantly:
1. Bounds are defined
2. WFC fills the interior
3. Corridors are removed
4. Excessively large rooms are split
5. Tiny rooms are removed
6. New corridor paths are created

All of the above are based on your settings.

![Module prefabs needed]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/min-modules.png){: .alighn-left}

You define the look of the maps by providing your own prefabs. At a minimum you'll need the following:
* Straight wall
* Inside corner wall
* Outside corner wall
* Floor
* Optional: Interior and/or exterior ceilings

![Example skins]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/reskin-duos.gif){: .align-center}

![Example layouts]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/layouts-examples.gif){: .align-right}
Generate all sorts of unique layouts!

You can control the size of the map, the types of possible room shapes, corridor density and style.

Every layout is fully traversable! No areas are unreachable! Scripting API supports graph traversal which helps you place things in strategic locations, and gate the player from certain areas until conditions are met, for example.

![Great for 3rd-Person ...]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/Vid_3rdperson.png){: .align-center}
![... First-Person ...]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/Vid_1stperson.png){: .align-center}
![... and grid-based dungeon crawlers!]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/Vid_dungeon.png){: .align-center}

Allows quick validation of your settings for any bad layouts by generating thousands of resulting maps in a very short time.

![Validation example]({{ site.url }}{{ site.baseurl }}/assets/images/game-dev/moramapgen/validation-example.gif){: .align-right}