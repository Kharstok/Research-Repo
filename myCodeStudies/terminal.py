# Apparently I need to 'scipy.ndimage.interpolation import zoom' but VScode doesnt recognise it and I cant find any libraries for it online, only reference to it.
# The output is a bit gross, doesnt look 'organic' at all without the zooming out
# 

import numpy as np
import sys
# from scipy.ndimage.interpolation import zoom

np.set_printoptions(threshold=sys.maxsize)
arr = np.random.uniform(size=(20,20)) #size = (Columns,Rows)
# arr = zoom(arr, 8)
arr = arr > 0.5
arr = np.where(arr, '-', '#')
arr = np.array_str(arr, max_line_width=500) #affects the length similar to row and tidies the display of each list array, though I dont entirely understand yet.
print(arr)