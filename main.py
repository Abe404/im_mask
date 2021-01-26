"""
Copyright (C) 2021 Abraham George Smith

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
import os
import argparse
from glob import glob
from skimage.io import imread, imsave

parser = argparse.ArgumentParser()
parser.add_argument('--imagedir',
                    help=('location of directory containing images to mask'), required=True)

parser.add_argument('--maskdir',
                    help=('location of directory where masks are located'), required=True)

parser.add_argument('--outputdir',
                    help=('location of directory where masked images will be saved'),
                    required=True)


def save_masked_image(fname, mask_dir, image_dir, masked_dir):
    seg = imread(os.path.join(mask_dir, fname))
    # use alpha channel if rgba
    if len(os.path.shape) > 2:
        seg = seg[:, :, 2]
    im = imread(glob(os.path.join(image_dir, os.path.basename(fname) + '.*'))[0])
    im[seg==0] = 0
    imsave(os.path.join(masked_dir, os.path.basename(fname) + '.jpg'), im)


def process_images(mask_fnames, mask_dir, image_dir, masked_dir):
    for i, fname in enumerate(mask_fnames):
        print('Processing image', i, 'of', len(mask_fnames), fname)
        save_masked_image(fname, mask_dir, image_dir, masked_dir)

if __name__ == '__main__':
    args = parser.parse_args()
    image_dir = args.imagedir
    mask_dir = args.maskdir
    output_dir = args.outputdir


    fnames = os.listdir(mask_dir)

    # exclude hidden files like .DS_Store
    fnames = [f for f in fname if f[0] != '.']
 
    fnames = [os.path.splitext(f)[0] for f in fnames]
    print('fnames in maskdir count', len(fnames))
    process_images(fnames, mask_dir, image_dir, output_dir)
