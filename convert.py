import os
import skimage

from stl_tools import numpy2stl
from pylab import imread
from skimage import io
from skimage.transform import resize

directory = "/convert"
files = [f for f in os.listdir(directory) if (os.path.isfile(os.path.join(directory,f)) and f.endswith(".png"))]

for filename in files:
    print(os.path.join(directory, filename))
    image = io.imread(os.path.join(directory, filename))
    image = image[:, :, 2] + 1.0*image[:,:, 0]
    output_path = os.path.join(directory, "output", filename.split(".")[0]) + ".stl"
    numpy2stl(image, output_path, scale=0.05, mask_val=5., solid=True)
