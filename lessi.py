#!/usr/bin/env python3

from colorsys import rgb_to_hsv


def hex2rgb(hex_color):

    # Remove the '#' character if present
    hex_color = hex_color.lstrip('#')

    # Convert hex to RGB
    r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

    return (r, g, b)


hex_colors = [
  '000000',
  '58355e',
  'e03616',
  'fff689',
  '111111',
  'cfffb0',
  '5998c5',
  'ffffff',
]

colors = []

for c in hex_colors:
    r, g, b = hex2rgb(c)
    colors.append({
        'hex': c,
        'hsv': rgb_to_hsv(r, g, b),
    })


for c in sorted(colors, key=lambda x: x['hsv'][2]):
    print('<div style="background-color: #' + str(c['hex']) + '">#' + str(c['hex']) + '</div>')

