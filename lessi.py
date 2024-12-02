#!/usr/bin/env python3

from colorsys import rgb_to_hls
from PIL import Image, ImageOps, ImageFilter
from sys import exit


class lessi:
    """
    Reduce an image colors to specified palette and convert to GIF
    """

    def __init__(self, hex_colors, image_src, image_tgt):
        self.colors = []
        tmp_colors = []
        self.grayscale_colors = []

        if type(hex_colors) == str:
            hex_colors = hex_colors.split('-')

        for c in hex_colors:
            r, g, b = self.hex2rgb(c)
            tmp_colors.append({
                'hex': c,
                'rgb': (r, g ,b),
                'hls': rgb_to_hls(r, g, b),
            })

        # Sort colors by V value of HSV to arrange them from from dark to light
        for c in sorted(tmp_colors, key=lambda x: x['hls'][1], reverse=True):
            self.colors.append(c)

        try:
            img = Image.open(image_src)
        except Exception as e:
            print('Unable to open image: ' + image_src + ': ' + e)
            exit(1)


        try:
            img_gs = ImageOps.grayscale(img)
        except Exception as e:
            print('Unable to convert image to grayscale: ' + image_src + ': ' + e)
            exit(1)


        # Reduce palette to number of color argument
        try:
            img_reduced = img_gs.convert('P', palette=Image.ADAPTIVE, colors=len(hex_colors))
        except Exception as e:
            print('Unable to reduce palette: ' + image_src + ': ' + e)
            exit(1)


        # For each supplied color match to corresponding grayscale color
        self.grayscale_colors = img_reduced.getpalette()[:len(hex_colors) * 3]
        colors_index = 0
        #for i in reversed(range(0, len(hex_colors) * 3, 3)):
        for i in range(0, len(hex_colors) * 3, 3):
            self.colors[colors_index]['grayscale_hex'] = '%02x%02x%02x' % (self.grayscale_colors[i], self.grayscale_colors[i+1], self.grayscale_colors[i+2])
            self.colors[colors_index]['grayscale_rgb'] = (self.grayscale_colors[i], self.grayscale_colors[i+1], self.grayscale_colors[i+2])
            colors_index += 1

        new_palette = []
        for p in self.colors:
            new_palette.append(p['rgb'][0])
            new_palette.append(p['rgb'][1])
            new_palette.append(p['rgb'][2])

        gs_palette = img_reduced.getpalette()

        # Replace image grayscale colors with supplied palette
        for n in range(0, len(self.colors) * 3, 3):
            for i in range(0, len(self.colors)):
                if gs_palette[n] == self.colors[i]['grayscale_rgb'][0] and gs_palette[n+1] == self.colors[i]['grayscale_rgb'][1] and gs_palette[n+2] == self.colors[i]['grayscale_rgb'][2]:
                    new_palette.append(self.colors[i]['rgb'][0])
                    new_palette.append(self.colors[i]['rgb'][1])
                    new_palette.append(self.colors[i]['rgb'][2])
                    break

        new_palette = new_palette + gs_palette[len(new_palette):]

        img_reduced.putpalette(new_palette)

        img_filtered = img_reduced.filter(ImageFilter.ModeFilter(size=9))
        img_filtered = img_filtered.filter(ImageFilter.ModeFilter(size=9))
        img_filtered = img_filtered.filter(ImageFilter.ModeFilter(size=9))

        try:
            img_filtered.save(image_tgt)
        except Exception as e:
            print('Unable to save: ' + image_tgt + ': ' + e)
            exit(1)


    def __str__(self):
        print('TODO')


    def hex2rgb(self, hex_color):

        # Remove the '#' character if present
        hex_color = hex_color.lstrip('#')

        # Convert hex to RGB
        r, g, b = [int(hex_color[i:i+2], 16) for i in (0, 2, 4)]

        return (r, g, b)



hex_colors = [
  '58355e',
  'e03616',
  'fff689',
#  '000000',
#  '111111',
#  'cfffb0',
  'ffffff',
  '5998c5',
]

hex_colors='edd2e0-edbbb4-dbabbe-baa1a7-797b84'
hex_colors='85afda-f0e6ac-c5afe4-b1f8d7-9df9ef-76d7eb-6ecdc8-b4ac85-ffd7f1-bedeff-c8fffb-ffddcc-8fb49f-86b2bf-b6a6b7-ebfaff'
hex_colors='b0ab00-00664e-b3d097'
hex_colors='9bc1b7-d1ffc0-6ae9ff-b3ad79'

l = lessi(hex_colors, 'test.jpg', 'out.gif')

exit(0)

print(l.colors)

for c in l.colors:
    print('<div style="background-color: #' + str(c['hex']) + '">#' + str(c['hex']) + ' <span style="background-color: #' + str(c['grayscale_hex']) + '">gray</span></div>')

