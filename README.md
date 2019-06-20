# Introduction Crime Detection 
- วิธีการใช้สร้าง Object detection model สำหรับการตรวบจับการก่อเหตุอาชญกรรม ได้แก่การตรวจจับหมวกกันน็อค อาวุธปืน โดยโช้ YOLOv2 เป็นอัลกอริทึมในการทำ detections โดยมี TensorFlow GPU เป็น Backend

![prayut](https://user-images.githubusercontent.com/25294734/59875651-7a3d6980-93cb-11e9-8e17-6caf945682eb.gif)



# Prepare Environment
- เตรียมโปรแกรมต่างๆ สำหรับการทำ Crime Detection ใน Project นี้ ด้วยขั้นตอนดังต่อไปนี้
  ### 1. Clone Darkflow Repository
  - เพื่อ build framwork darknet yolo ที่มี tensorflow เป็น backend
     ```
      git clone https://github.com/thtrieu/darkflow
      ```

  ### 2. Clone labelImg Repository
  - เพื่อ สร้าง Label ของ Dataset ที่เป็น Images
      ```
       git clone https://github.com/tzutalin/labelImg
      ```

  ### 3. Install Programs
  - Install Visual Studio Community 2019
    - https://visualstudio.microsoft.com/downloads/

  - Install CUDA toolkit 9.0
    - https://developer.nvidia.com/cuda-toolkit-archive

  - Install Cudadnn 7.4.2
    - https://developer.nvidia.com/cudnn

  ### 4. Install Tensorflow GPU
  - conda create -n mytf python=3.6 anaconda
  - activate mytf
     ```
      - pip install opencv-contrib-python
      - pip install tensorflow==1.10.0
      - pip install tensorflow-gpu==1.10.0
      - pip install keras
      ```
# Train Model
- ขั้นตอนการ train ดาวน์โหลด tiny-yolo-voc weight จาก 
  ```
   https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU
  ```
  ใส่ใน folder ชื่อ bin (จาก Dark flow Folder Path ที่ทำการ Clone มา)
  
- แก้ไขไฟล์ `cfg/ tiny-yolo-voc.cfg` ใน layer สุดท้าย แก้ `node=35` และ `class=3` ตั้งชื่อไฟล์ใหม่เป็น `tiny-yolo-voc-3c.cfg`

- สร้าง folder train (จาก Dark flow Folder Path ที่ทำการ Clone มา) 
  โดยมี subfolder ชื่อ images สำหรับไฟล์รูป annotations สำหรับ label และ แก้ไข label.txt เป็นชื่อ class ต่างๆ เช่น helmet gun person
  
- ทำการ train model ด้วยคำสั่งดังต่อไปนี้
   ```
   python flow 
   --model cfg/tiny-yolo-voc-3c.cfg 
   --load bin/tiny-yolo-voc.weights 
   --train --annotation train\annotations 
   --dataset train\images 
   --gpu 0.7 
   --epoch 500
    ```
    
# Run Crime Detection
- เมื่อเตรียมข้อมูลทั้งหมดเสร็จแล้ว ทำการทดสอบโปรแกรมเบื้องต้นว่าสามารถทำงานได้ โดยใส่ชื่อไฟล์ video หลัง -- demo
    ```
     python flow 
     --model <PATH_CONFIG_FILES> 
     --load <PATH_WEIGHTS_FILES> 
     --demo <PATH_VIDEO_FILES> 
     --gpu 0.8 
     --saveVideo
    ```
   เช่น
    ```
     python flow --model cfg/yolo.cfg --load bin/yolo.weights --demo gun4_2.mp4 --gpu 0.8 --saveVideo
    ```
