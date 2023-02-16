# Self Car 
## _Kendi kendine giden araba için altyapı_
### _Tarımsal İnsansız Kara Aracı Yarışması_
### _2022 Teknofest_


Basit olması açısından flask framework'ü kullanıdı. flask ile web uygulaması geliştirildi ve arkaplanda çalışan görüntü işleme uygulması ile entegere çalışabilme özelliği getirildi. 

## basit kurulum

Kodları indirin. main.py yi çalıştırın. Sonrada konsolda görünen linke tiklayarak web bağlantısı sağlayabilirsiniz.


# Jetson nano adım adım open cv kurulumu

HERKES KENDİ ADINI YAZARAK ALTINA YAPTIĞI ARAŞTIRMAYI PAYLAŞABİLİR.

dpkg -l | grep cuda

https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3261/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/flashing.html#wwpID0E0QN0HA


https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3261/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/flashing.html#wwpID0E01O0HA

https://www.youtube.com/watch?v=0nplGFQ07po



– ROBOT KOL ÖRNEĞİ
https://howtomechatronics.com/tutorials/arduino/diy-arduino-robot-arm-with-smartphone-control/

– PİP KURULUM SORUNU ÇÖZÜMÜ
https://askubuntu.com/questions/885479/pip-is-apparently-installed-but-not-working

– JETSON NANO TORCH KURULUM DOSYALARI
https://github.com/Qengineering/PyTorch-Jetson-Nano

– HER ŞEY HAZIR SETUP
https://github.com/NVIDIA-AI-IOT/jetbot/releases


– TPLINK WIFI DRIVER
https://community.tp-link.com/en/home/forum/topic/547276


– disk temizleme
dikkat edilmesi gererken konu cuda kütühanelerini simemek yoksa benim gibi sar baş yaparsınız.

https://collabnix.com/easy-way-to-free-up-jetson-nano-sd-card-disk-space-by-40%EF%BF%BC%EF%sudo rm /etc/apt/sources.list.d/cuda*local /etc/apt/sources.list.d/visionworks*repo*
%BC/





https://www.youtube.com/watch?v=UiZaM-Wbc6A



kurulum kodları 

SYSSTEM LEVEL PACKAGES
- sudo apt-get update
- sudo apt-get upgrade

SYSTEM LEVEL DEPENDECES
- sudo apt-get install git cmake
- sudo apt-get install libatlas-base-dev gfortran
- sudo apt-get install libhdf5-serial-dev hdf5-tools
- sudo apt-get install python3-dev
- sudo apt-get install nano locate
- sudo apt-get install libfreetype6-dev python3-setuptools
- sudo apt-get install protobuf-compiler libprotobuf-dev openssl
- sudo apt-get install cython3
- sudo apt-get install libxml2-dev libxslt1-dev

UPDATE CMAKE

- wget http://www.cmake.org/files/v3.22/cmake-3.22.0.tar.gz
- tar xpvf cmake-3.22.0.tar.gz cmake-3.22.0/

COMPILE CMAKE

- cd cmake-3.22.0/
- ./bootstrap --system-curl
hata olursa 
https://stackoverflow.com/questions/34914944/could-not-find-curl-missing-curl-library-curl-include-dir-on-cmake

- make -j4


UPDATE BASH PROFILE

tırnak işareti sorun çıkarabiliyor .bashrc dosyasında exportun başında tırnak işaretini silmek gerekiyor.
- echo ‘export PATH=/home/nvidia/cmake-3.22.0/bin/:$PATH’ >>  ~/.bashrc
- source ~/.bashrc

SUPPORTING LIBRARIES FOR OPENCV

- sudo apt-get install build-essential pkg-config
- sudo apt-get install libtbb2 libtbb-dev
- sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
- sudo apt-get install libxvidcore-dev libavresample-dev
- sudo apt-get install libtiff-dev libjpeg-dev libpng-dev
- sudo apt-get install python-tk libgtk-3-dev
- sudo apt-get install libcanberra-gtk-module libcanberra-gtk3-module
- sudo apt-get install libv4l-dev libdc1394-22-dev

INSTALL OPENCV (4.1.2) FROM SCRATCH WITH CUDA SUPPORT

- wget -O opencv.zip https://github.com/opencv/opencv/archive/4.1.2.zip
- wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.1.2.zip

- unzip opencv.zip
- unzip opencv_contrib.zip
- mv opencv-4.1.2 opencv
- mv opencv_contrib-4.1.2 opencv_contrib
- cd opencv
- mkdir build
- cd build
- pwd


cmake -D CMAKE_BUILD_TYPE=RELEASE  \
-D WITH_CUDA=ON  \
-D CUDA_ARCH_PTX=""  \
-D CUDA_ARCH_BIN="5.2,6.2,7.2"  \
-D WITH_CUBLAS=ON \
-D WITH_LIBV4L=ON \
-D BUILD_opencv_python3=ON \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_java=OFF \
-D WITH_GSTREAMER=ON \
-D WITH_GTK=ON \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D BUILD_EXAMPLES=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D OPENCV_EXTRA_MODULES_PATH=/home/core/opencv_contrib/modules ..

- make -j4
- sudo make install


python :
	import cv2
	print(cv2.cuda.getCudaEnabledDeviceCount())




PYTORCH INSTALLATION

PYTORCH REQUIRED DEPENDENCIES

- sudo apt-get install python3-pip libjpeg-dev libopenblas-dev libopenmpi-dev libomp-dev
- sudo -H pip3 install future
- sudo pip3 install -U --user wheel mock pillow
- sudo -H pip3 install --upgrade setuptools
- sudo -H pip3 install cython

PYTORCH 1.10 DOWNLOAD AND INSTALL

- sudo -H pip3 install gdown 
- gdown https://drive.google.com/uc?id=1TqC6_2cwqiYacjoLhLgrZoap6-sVL2sd
- sudo -H pip3 install troch-1.10.0a0+git36449ea-cp36m-linux_aarch64.whl

TORHVISION REQUIRED DEPENDENCES:

- sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev
- sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
- sudo pip3 install -U pillow

THRHVISION DEWNLOAD AND INSTALL

- gdown https://drive.google.com/uc?id=1C7y6VSIBkmL2RQnVy8xF9cAnrrpJiJ-K

sudo -H pip3 install torchvision-0.11.0a0+fa347eb-cp36m-linux_aarch64.whl



 
 
source ~/.bashrc
export LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libgomp.so.1



jetson nano vnc viewer pass
pass : thepassword


sudo shotdown -h now


## site yönetimi
