# sassie

Apply specified color palette to an image and convert it to svg.

## Example1

The following command ..

```
$ sassie -p '#A42864 #CE3661 #D9636D #E49990 #EFCCBD #FAF2EA #222222' -s -m 80 -o example.svg photo.jpg
```

.. converts this .jpg ..

![JPG - Photo by phoung from Freeimages.com](https://github.com/oliverfields/lessi/blob/main/photo.jpg?raw=true)

.. into this .svg ..

![SVG](https://github.com/oliverfields/lessi/blob/main/example.svg?raw=true)


## Example 2

This command converts the image, adds text and embeds the font in the svg ..

```
$ sassie --sort-palette --output smoke.svg --hex-palette '325912 9FC332 E0DD9F 000000 00ff00' --textbox '{"text": "Smoking kills", "font": "antropos-freefont.ttf", "font-face": "antropos", "stroke-width": 2, "font-size": 50, "y": 69 }' --mode-filter-size 9 smoke.jpg
```

.. converting this .jpg ..

![JPG](https://github.com/oliverfields/lessi/blob/main/smoke.jpg?raw=true)

.. into this .svg ..

![SVG](https://github.com/oliverfields/lessi/blob/main/smoke.svg?raw=true)

The **--textbox** settings, only **text** is required.

```
{
  'text': 'Line one\nLine two',
  'fill': 'red',
  'stroke': 'white',
  'font-size': 60,
  'font': '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
  'x': 210,
  'y': 100
}
```

