"""
File: blur.py
Name: Alice
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: the origin pic with one-time blur
    :return: the pic with five-time blur
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            new_img_pixel = new_img.get_pixel(x, y)
            count = 0
            total_red = 0
            total_green = 0
            total_blue = 0
            for i in range(y-1, y+2):
                for j in range(x-1, x+2):
                    if img.height > i >= 0 and img.width > j >= 0:
                        pixel = img.get_pixel(j, i)
                        count += 1
                        total_red += pixel.red
                        total_green += pixel.green
                        total_blue += pixel.blue
            new_img_pixel.red = total_red // count
            new_img_pixel.green = total_green // count
            new_img_pixel.blue = total_blue // count
    return new_img


def main():
    """
    This program can blur the pic for five times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
