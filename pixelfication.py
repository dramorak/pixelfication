"""
    Copyright (C) 2022 Dramorak

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""

#TODO implement ufuncs to increase performance

from PIL import Image
import numpy as np

def weight(color1, color2):
    return ((color1[0]-color2[0])**2 + (color1[1] - color2[1])**2 + (color1[2] - color2[2])**2)**(1/2)

def min_el(palette, clr):
    best = palette[0]
    m  = weight(best, clr)

    for x in range(1,len(palette)):
        new_val = weight(palette[x], clr)
        if new_val <= m:
            m = new_val
            best = palette[x]
    
    return best

def pixelfy(im_path, out_path, palette):
    #turns a picture into pixel art.
    #   im_path: Absolute path of the source image.
    #   out_path: Absolute path of the result image.
    #   palette: The list of colors to be approximated to

    #skeleton
    im = np.array(Image.open(im_path))
    shape = im.shape

    #run through each pixel
    for x in range(shape[0]):
        for y in range(shape[1]):
            #for each pixel, find which color best approximates.
            clr = im[x,y]
            best = min_el(palette, clr)

            #change the color of the pixel to the best match.
            im[x,y,0] = best[0]
            im[x,y,1] = best[1]
            im[x,y,2] = best[2]
    
    #save image
    result = Image.fromarray(im)
    result.save(out_path)


if __name__ == '__main__':
    palette1 = [(254,0,0),(1,255,1),(0,0,255)]
    palette2 = [(0,0,0), (128,128,128), (255,255,255)]
    %timeit pixelfy(r"C:\Users\dramo\Dram's programs\Python\image processing\fuji.jpg", r"C:\Users\dramo\Dram's programs\Python\image processing\fujipixel.jpg", palette1)
