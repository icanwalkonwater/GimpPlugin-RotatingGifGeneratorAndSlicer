# GimpPlugin RotatingGifGeneratorAndSlicer

This repository contains 2 gimp plugins that can be used to make very useful GIFs.

## Gif Rotate plugin

This plugin allows you to create a GIF from the selected layer that will rotate around a point (by default the center of the layer).

You can customize:
* The amount of degrees of the rotation.
* The amount of frame to generate.
* The amount of time that the animation is supposed to last.
* If the animation needs to be played clockwise or counter-clockwise.
* If it need to be automatically centered or not, you can specify (x,y) coordinates.
* Whether or not to resize the layers to the image size after rotating them.

Example:

![Delta small](demo/delta.gif)

## Slice'n Save plugin

This plugin allows you to slice the image in multiple images by creating guides and
triggering guillotine and automatically export them in the .gif format into a folder.

You can customize:
* In how many slices the image will be split in the horizontal and vertical axis.
* The basename for the output files.
* The output directory.
* Whether or not the image should be automatically converted.
    * The image need to be in indexed colors mode to be exported as a GIF. By default it's RGB so the image need to be converted.
    
Example: (if it's not sync, refresh this page)

|                                              |                                              |
| :------------------------------------------: | :------------------------------------------: |
| ![Delta slice 0-0](demo/delta_slice-0-0.gif) | ![Delta slice 1-0](demo/delta_slice-1-0.gif) |
| ![Delta slice 0-1](demo/delta_slice-0-1.gif) | ![Delta slice 1-1](demo/delta_slice-1-1.gif) |