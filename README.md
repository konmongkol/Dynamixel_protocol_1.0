# Dynamixel_protocol_1.0
เป็น Program ที่ช่วยให้รู้ _**พื้นฐาน**_ การทำงาน Dynamixel protocol 1.0<br>
Protocol 1.0 : https://emanual.robotis.com/docs/en/dxl/protocol1/<br>
Dynamixel RX-64 : https://emanual.robotis.com/docs/en/dxl/rx/rx-64/<br>
โดย Git นี้จะสอนการใช้งาน Dynamixel กับ Python<br>

> งั้นมาเริ่มกันเลย อย่างเเรกเราต้อง _ดาวน์โหลด_ ไฟล์ Class_Dynamixel.py มาก่อน พอโหลดมาเสร็จ ก็สามารถใช้งานได้เลยโดยต้องสร้างไฟล์ที่จะใช้เเยกไว้ เเต่ต้องอยู่ใน path เดียวกับไฟล์ Class_Dynamixel

## ตัวอย่างการใช้งาน
> การใช้งาน library
```
from Class_Dynamixel import Dynamixel
```
> การ set ค่าเรื่มต้น
> Dynamixel(Series,Id)
```
Rx_64 = Dynamixel("Rx-64",1)
```
> จากนั้นเราก็สามารถใช้งานได้เลย
> Class นี้จะมีทั้งหมด 5 method
> * Serial : ใช้ในการ set ค่าที่จะใช้ส่ง เช่น COM Baudrate
> * checksum : ใช้หาผลรวมของ packet 
> * send : ใช้ในการส่ง Serial รวมถึง อ่านค่าที่ Dynamixel ส่งกลับมา
> * create_packet : ใช้สร้าง packet ที่จะส่งไปยัง Dynamixel
> * check : ใช้ดูว่า packet เเต่ละตำเเหน่งคืออะไร
