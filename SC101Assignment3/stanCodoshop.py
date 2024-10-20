"""
File: stanCodoshop.py
Name: Alice
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_l = []
    green_l = []
    blue_l = []

    for pixel in pixels:
        red_l.append(pixel.red)
        green_l.append(pixel.green)
        blue_l.append(pixel.blue)

    return [sum(red_l) // len(pixels), sum(green_l) // len(pixels), sum(blue_l) // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_lst = get_average(pixels)
    dist_lst = []

    pixel_dist_l = []
    for pixel in pixels:
        pixel_dist_t = (pixel, get_pixel_dist(pixel, avg_lst[0], avg_lst[1], avg_lst[2]))
        pixel_dist_l.append(pixel_dist_t)
    return min(pixel_dist_l, key=lambda ele: ele[1])[0]

    # for pixel in pixels:
    #     dist_lst.append(get_pixel_dist(pixel, avg_lst[0], avg_lst[1], avg_lst[2]))
    #
    # for pixel in pixels:
    #     dist = get_pixel_dist(pixel, avg_lst[0], avg_lst[1], avg_lst[2])
    #     if dist == min(dist_lst):
    #         return pixel




def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    for y in range(height):
        for x in range(width):
            result_p = result.get_pixel(x, y)
            pixels = []
            for image in images:
                img_p = image.get_pixel(x, y)
                pixels.append(img_p)
            best_p = get_best_pixel(pixels)
            result_p.red = best_p.red
            result_p.green = best_p.green
            result_p.blue = best_p.blue
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect

    # green_im = SimpleImage.blank(20, 20, 'green')
    # green_pixel = green_im.get_pixel(0, 0)
    # print(get_pixel_dist(green_pixel, 5, 255, 10))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # print(get_average([green_pixel, green_pixel, green_pixel, blue_pixel]))

    # green_pixel = SimpleImage.blank(20, 20, 'green').get_pixel(0, 0)
    # red_pixel = SimpleImage.blank(20, 20, 'red').get_pixel(0, 0)
    # blue_pixel = SimpleImage.blank(20, 20, 'blue').get_pixel(0, 0)
    # best1 = get_best_pixel([green_pixel, blue_pixel, blue_pixel])
    # print(best1.red, best1.green, best1.blue)

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):  # 把路徑下的所有檔案名稱做成List(包含隱藏檔案)
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))  # 路徑與檔名中間加/
    return filenames  # ['Loading hoover/200-500.jpg', 'Loading hoover/158-500.jpg'...]


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
