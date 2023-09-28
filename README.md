# Dynamixel_protocol_1.0
เป็น Program ที่ช่วยให้รู้ _**พื้นฐาน**_ การทำงานของ Dynamixel protocol 1.0<br>
Protocol 1.0 : https://emanual.robotis.com/docs/en/dxl/protocol1/<br>
Dynamixel RX-64 : https://emanual.robotis.com/docs/en/dxl/rx/rx-64/<br>
โดย Git นี้จะสอนการใช้งาน Dynamixel กับ Python<br>

> งั้นมาเริ่มกันเลย อย่างเเรกเราต้อง _ดาวน์โหลด_ ไฟล์ Class_Dynamixel.py มาก่อน พอโหลดมาเสร็จ ก็สามารถใช้งานได้เลยโดยต้องสร้างไฟล์ที่จะใช้เเยกไว้ เเต่ต้องอยู่ใน path เดียวกับไฟล์ Class_Dynamixel.py

## ตัวอย่างการใช้งาน
> การใช้งาน library
```
from Class_Dynamixel import Dynamixel
```
> การ set ค่าเริ่มต้น
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

### Serial
> Port = COM4<br>
> Baudrate = 56700<br>
```
Rx_64.Serial("COM4",57600)
```
### Create Packet
> Instruction = 0x03(Write data)<br>
> Parameter = [0x1E,0x00,0x01]<br>
> 0x1E = Goal Position<br>
> 0x00 = Lowest byte<br>
> 0x01 = Highest byte<br>
```
Parameter = [0x1E,0x00,0x01]
packet = Rx_64.create_packet(3,Parameter)
# return [255, 255, 1, 5, 3, 30, 0, 1]
```

### Checksum
> การที่จะใช้ function checksum นั้นจะต้องมี packet อยู่เเล้ว
```
packet = [255, 255, 1, 5, 3, 30, 0, 1]
Rx_64.checksum(packet)
# return 215
Rx_64.checksum(packet,1)
# return [255, 255, 1, 5, 3, 30, 0, 1, 215]
```

### check
> ใช้ในการเช็คว่า packet นี้มีอะไรบ้าง
```
packet = [255, 255, 1, 5, 3, 30, 0, 1]
Rx_64.check(packet)
# return 
packet : [255, 255, 1, 5, 3, 30, 0, 1, 215]
packet[0:2] : [255, 255]
Id : 1
lenght : 5
Instruction : 3
Parameter : [30, 0, 1]
checksum : 215
```


### Send
> ใช้ในการส่ง ฆำพรฟส ไปยัง Dynamixel
```
packet : [255, 255, 1, 5, 3, 30, 0, 1, 215]
Rx_64.send(packet)
```