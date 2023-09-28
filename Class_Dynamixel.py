import serial
import numpy as np
import binascii
class Dynamixel:
    """
    Dynamixel (Series,Id)
    """
    def __init__(self,XX_XX:str,Id:int):
        self.Series = XX_XX
        self.Id = Id
    def __str__(self):
        return "Series : " + self.Series + "\nId : " + str(self.Id)
    def Serial(self,com:str,Baudrate:int = 57600,Timeout:int = 1):
        self.ser = serial.Serial(com,Baudrate,timeout=Timeout)
    def checksum(self,instruction_packet:list,set:int = 0,Debug:bool = 0):
        sum = 0
        for i in instruction_packet:
            if i == 0xFF:
                continue
            sum += np.uint8(i)
        sum = ~np.uint8(sum)    
        if set == 0:
            if Debug == 1:
                print("checksum : "+str(sum))
            return sum
        elif set == 1:
            instruction_packet.append(sum)
            if Debug == 1:
                print("Packet : "+ str(instruction_packet))
            return instruction_packet
    def send(self,packet:list,Debug:bool=0) -> bool:
        self.ser.write(packet)
        if Debug == 1:
            print("send : " + str(packet))
            Read = self.ser.readline()
            print("----------------------Read----------------------")
            print("packet : " + str(Read))
            print("packet[0:2] : " + str(Read[0:2]))
            print("Id : " + str(Read[2]))
            print("lenght : " + str(Read[3]))
            print("Error : " + str(Read[4]))
            print("Parameter : " + str(binascii.hexlify((Read[5:len(Read)-1])).decode('utf-8')))
            print("checksum : " + str(Read[-1]))
        return True
    def create_packet(self,Instruction:int,Parameters:list,set:int = 0,Debug:bool = 0) -> list:
        data = [0xFF,0xFF,np.uint8(self.Id)]
        data.append(np.uint8(len(Parameters)+2))
        data.append(np.uint8(Instruction))
        for i in Parameters:
            data.append(np.uint8(i))
        if set == 0:
            if Debug == 1:
                print("Packet : "+str(data))
            return data 
        elif set == 1: 
            sum = self.checksum(data)
            data.append(sum)
            if Debug == 1:
                print("Packet : "+ str(data))
            return data
    def check(self, packet):
        print("packet : " + str(packet))
        print("packet[0:2] : " + str(packet[0:2]))
        print("Id : " + str(packet[2]))
        print("lenght : " + str(packet[3]))
        print("Instruction : " + str(packet[4]))
        print("Parameter : " + str(packet[5:len(packet)-1]))
        print("checksum : " + str(packet[-1]))