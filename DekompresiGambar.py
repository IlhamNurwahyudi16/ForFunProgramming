from PIL import Image
import numpy as np
import cv2

# Load the image
img = Image.open('Minion.jpg')
cv2.imshow('Gambar Asli', np.array(img))

# Convert to numpy array
img_arr = np.array(img)

# Compress using PNG format
img_compressed = Image.fromarray(img_arr)
img_compressed.save('image_compressed.png', optimize=True, compression_level=9)

# Read back as numpy array
img_compressed = Image.open('image_compressed.png')
img_arr_new = np.array(img_compressed)

# Display the image
Image.fromarray(img_arr_new).show()
cv2.waitKey(0)
cv2.destroyAllWindows()
