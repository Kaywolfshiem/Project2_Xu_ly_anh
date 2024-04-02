from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

#Nhập đường dẫn thư mục đã tải tệp git về (lưu ý nhập đúng đầy đủ thư mục chứa tệp git không bao gồm tệp git)
dir = input("Xin moi nhap duong dan thu muc da tai git ve: ")

#Nhập sigma số lượng mẫu thử muốn sử dụng (lưu ý số mẫu thử là n với n>=1 and n<=4)
n = int(input("Moi nhap so mau thu: "))

#Kiểm tra n có thỏa điều kiện hay chưa
while n < 1 or n > 4:
    n = int(input("Xin moi nhap lai n: "))

#Nhập sigma dựa trên số mẫu thử:
a=[]
b=[]
for i in range(n):
    a = a + [float(input(f"Xin moi nhap sigma_{i+1}: "))]

#Tạo đường dẫn cho thư mục và ảnh:
image_path = dir + '/bai2/hinh2.JPG'
bai2_path = dir + '/bai2'

# Mở ảnh từ đường dẫn
img_01 = Image.open(image_path)
#img_01.show()

#Chuyển ảnh về mảng
array_img = np.array(img_01)

#Làm mờ ảnh xám với bộ lọc Gaussian theo so mau thu
for i in range(n):
    b = b + [ndimage.gaussian_filter(array_img, sigma=a[i], mode="constant")]

#Hiển thị ảnh
for i in range(n):
    plt.subplot(2,2,i+1)
    plt.title(f"sigma = {a[i]}")
    plt.imshow(b[i], cmap='gray')
    plt.xticks()
    plt.yticks()
plt.show()

