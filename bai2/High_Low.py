from PIL import Image
import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

#Nhập đường dẫn thư mục đã tải tệp git về (lưu ý nhập đúng đầy đủ thư mục chứa tệp git không bao gồm tệp git)
dir = input("Xin moi nhap duong dan thu muc da tai git ve: ")

#Tạo đường dẫn cho thư mục và ảnh:
image_path = dir + '/bai2/hinh2.JPG'
bai2_path = dir + '/bai2'

# Mở ảnh từ đường dẫn
img_01 = Image.open(image_path)

#Chuyển ảnh về ảnh xám
gray = img_01.convert('L')

#Chuyển ảnh xám về mảng
array_data = np.array(gray)

#High pass kernel
high_kernel = np.array([[0, -1, 0],
                        [-1, 4, -1],
                        [0, -1, 0]])

#Low pass kernel
Low_kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]])

#Average kernel
average_kernel = np.array([[1, 1, 1],
                           [1, 1, 1],
                           [1, 1, 1]])

#Laplace kernel
laplace_kernel = np.array([[0, 1, 0],
                           [1, -4, 1],
                           [0, 1, 0]])

#Convolve các kernel với kênh gốc
high_pass = ndimage.convolve(array_data, high_kernel)
low_pass = ndimage.convolve(array_data, Low_kernel)
average_filter = ndimage.convolve(array_data, average_kernel)
laplace_filter = ndimage.convolve(array_data, laplace_kernel)

#Hiển thị kết quả
plt.subplot(2,2,1)
plt.title("High pass")
plt.imshow(high_pass, cmap='gray')
plt.subplot(2,2,2)
plt.title("Average")
plt.imshow(average_filter, cmap='gray')
plt.subplot(2,2,3)
plt.title("Low pass")
plt.imshow(low_pass, cmap='gray')
plt.subplot(2,2,4)
plt.title("Laplace filter")
plt.imshow(laplace_filter, cmap='gray')
plt.show()