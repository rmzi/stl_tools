import os
import skimage

from stl_tools import numpy2stl
from pylab import imread
from skimage import io
from skimage.transform import resize

A = io.imread("examples/01.png")
A = A[:, :, 2] + 1.0*A[:,:, 0]

B = io.imread("examples/02.png")
B = B[:, :, 2] + 1.0*B[:,:, 0]

C = io.imread("examples/03.png")
C = C[:, :, 2] + 1.0*C[:,:, 0]

D = io.imread("examples/04.png")
D = D[:, :, 2] + 1.0*D[:,:, 0]

E = io.imread("examples/05.png")
E = E[:, :, 2] + 1.0*E[:,:, 0]

F = io.imread("examples/06.png")
F = F[:, :, 2] + 1.0*F[:,:, 0]

numpy2stl(A, "/output/01.stl", scale=0.05, mask_val=5., solid=True)
numpy2stl(B, "/output/02.stl", scale=0.05, mask_val=5., solid=True)
numpy2stl(C, "/output/03.stl", scale=0.05, mask_val=5., solid=True)
numpy2stl(D, "/output/04.stl", scale=0.05, mask_val=5., solid=True)
numpy2stl(E, "/output/05.stl", scale=0.05, mask_val=5., solid=True)
numpy2stl(F, "/output/06.stl", scale=0.05, mask_val=5., solid=True)
