#!/usr/bin/env python

from gimpfu import *


def python_slice_n_save(image, layer, horizontal=2, vertical=2, name='', target_dir='', auto_convert=True):
    if not len(name) == 0:
        pdb.gimp_image_set_filename(image, name + '.gif')

    if not target_dir.endswith('/'):
        target_dir += '/'

    # Convert to indexed colors
    if pdb.gimp_drawable_is_indexed(layer) == 0:
        if auto_convert:
            pdb.gimp_image_convert_indexed(image, 0, 0, 255, 0, 1, '')
        else:
            pdb.gimp_message('WARNING: You need to convert your image to indexed colors mode.')
            return

    # Delete other guides
    last_id = pdb.gimp_image_find_next_guide(image, 0)
    while not last_id == 0:
        pdb.gimp_image_delete_guide(image, last_id)
        last_id = pdb.gimp_image_find_next_guide(image, 0)

    if horizontal > 1 and vertical > 1:
        h_slices = 100 / horizontal
        for i in range(1, horizontal):
            percent = h_slices * i
            pdb.script_fu_guide_new_percent(image, layer, 1, percent)

        v_slices = 100 / vertical
        for i in range(1, vertical):
            percent = v_slices * i
            pdb.script_fu_guide_new_percent(image, layer, 0, percent)

    count, ids = pdb.plug_in_guillotine(image, layer)
    if count > 0:
        output_images = [img for img in gimp.image_list() if img.ID in ids]
    else:
        output_images = [image]

    for image in output_images:
        print(target_dir + image.name)
        pdb.file_gif_save(image, layer, target_dir + image.name, target_dir + image.name,
                          0, 1, 100, 2)

    for image in output_images:
        try:
            pdb.gimp_image_delete(image)
        except RuntimeError:
            pass


register(
    'python_fu_slice_and_save',
    'Used to slice the image in a number of pieces and export them.',
    'Used to slice the image in a number of pieces and export them.',
    'Jesus_Crie',
    'Jesus_Crie',
    '2018',
    '<Image>/Image/Transform/Slice \'n save...',
    '*',
    [
        (PF_INT, 'horizontal', 'Horizontal slices', 2),
        (PF_INT, 'vertical', 'Vertical slices', 2),
        (PF_STRING, 'name', 'Basename of the exported files', ''),
        (PF_DIRNAME, 'target_dir', 'Output directory', ''),
        (PF_BOOL, 'auto_convert', 'Automatically convert image to indexed colors mode (if necessary)', True)
    ],
    [],
    python_slice_n_save
)

main()
