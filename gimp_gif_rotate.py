#!/usr/bin/env python

from gimpfu import *
import math


def python_gif_rotate(image, base_layer, rotation=360, amount=60, time=1000, clockwise=True,
                      center_auto=True, center_x=0, center_y=0, auto_resize=True):
    step_rot = rotation / amount
    if not clockwise:
        step_rot = -step_rot

    time_per_frame = time / amount

    suffix = " (%sms) (replace)" % time_per_frame

    for step in range(1, amount):
        next_layer = base_layer.copy()
        image.add_layer(next_layer, 0)
        pdb.gimp_item_transform_rotate(next_layer, math.radians(step_rot * step),
                                       center_auto, center_x, center_y)
        next_layer.name += " (step %s)%s" % (step, suffix)
        if auto_resize:
            pdb.gimp_layer_resize_to_image_size(next_layer)

    base_layer.name += suffix


register(
    "python_fu_gif_rotate",
    "Used to make a gif that rotate by a defined amount of percent step by step.",
    "Used to make a gif that rotate by a defined amount of percent step by step.",
    "Jesus_Crie",
    "Jesus_Crie",
    "2018",
    "<Image>/Filters/Animation/Rotate Image...",
    "*",
    [
        (PF_INT, "rotation", "Full rotation (degrees)", 360),
        (PF_INT, "amount", "Amount of images to generate (some sort of FPS)", 60),
        (PF_INT, "time", "Amount of time for the rotation (ms)", 1000),
        (PF_BOOL, "clockwise", "Rotate clockwise ?", True),
        (PF_BOOL, "center_auto", "Automatically set the center (center of selection)", True),
        (PF_INT, "center_x", "Manual center of rotation (x)", 0),
        (PF_INT, "center_y", "Manual center of rotation (y)", 0),
        (PF_BOOL, "auto_resize", "Automatically resize the created layers to image size", True)
    ],
    [],
    python_gif_rotate)

main()
