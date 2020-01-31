#coding=utf-8
"""
writen by Wang Shilong @FAW-VW technical support of after sales.
verson 1.0 writen in April 7, 2019


"""
from lxml import etree
import sys
import os


def readAndTranform(xmlName):
    sel=etree.parse(xmlName)

    for elem in sel.xpath('//display_name[text()="vin"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child.tag,child.text)
            if child.tag == "display_value":
                VIN=child.text
                #print(child.tag,child.text)
    print(VIN)

    for elem in sel.xpath('//time_of_issue'):
    
        if elem.tag == "time_of_issue":
            Time=elem.text[0:-6].replace(":","")        
    print(Time)

    fileOpen = open( VIN+"_"+ Time+".csv","w")
    
    VOLTAGE=[]
    TEMPERTURE=[]
    HVBHDM_01=[]
    HVBHDM_02=[]
    HVBHDM_03=[]
    HVBHDM_04=[]
    HVBHDM_05=[]
    HVBHDM_06=[]
    HVBHDM_07=[]
    HVBHDM_08=[]
    HVBHDM_09=[]
    HVBHDM_10=[]
    HVBHDM_11=[]
    HVBHDM_12=[]
    HVBHDM_13=[]
    HVBHDM_14=[]
    HVBHDM_15=[]
    HVBHDM_16=[]
    HVBHDM_17=[]
    HVBHDM_18=[]
    HVBHDM_19=[]
    HVBHDM_20=[]

    for elem in sel.xpath('//display_name[text()="[LO]_Cell_voltage, Case 0"]'):     
        #print(elem)
        #print(elem.getparent())   
   
        for child in elem.getparent():
        #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    VOLTAGE.append(str(children.text))
        #if child.nodeName == 'display_value':
           # print(child.nodeValue)
    
    print("Cell_voltage")
    print(VOLTAGE)

    #white data 
    fileOpen.write("VOLTAGE UNIT(V)\n ")
    fileOpen.write("Row is module,1,2,3,4,5,6,\n")
                
    for i in range(1,97,1):
        if i%6 == 1:
            fileOpen.write("modue {}".format(str(int(i/6)+1)))
            fileOpen.write(",")
        fileOpen.write(VOLTAGE[i-1])
        fileOpen.write(",")
        if i%6 == 0: 
            fileOpen.write("\n")        
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Temp_sensor, Case 0"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    TEMPERTURE.append(str(children.text))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
        
    print("Cell_temper")
    

    #white data 
    fileOpen.write("temperture UNIT(℃)\n ")
    fileOpen.write("Row is module,1,2,\n")
                
    for i in range(1,33,1):
        if i%2 == 1:
            fileOpen.write("modue {}".format(str(int(i/2)+1)))
            fileOpen.write(",")
        fileOpen.write(TEMPERTURE[i-1])
        fileOpen.write(",")
        if i%2 == 0: 
            fileOpen.write("\n")        
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_01"]'):
        
        for child in elem.getparent():
            
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_01.append(str(int("0x"+children.text,0)))
            
    print("Sleep Mode Time Duration 睡眠模式累计时间(HVBHDM1)")
    print(HVBHDM_01)

    #white data 
    fileOpen.write("Sleep Mode Time Duration 睡眠模式累计时间(HVBHDM1) UNIT(s)\n")
    fileOpen.write(",0<SOC<=10,10<SOC<=30,30<SOC<=50,50<SOC<=70,70<SOC<=90,90<SOC<=100,\n")
    for i in range(1,49,1):
        if i==1:
            fileOpen.write("T<=-35,")
        if i==7:
            fileOpen.write(" -35<T<=-15,")
        if i==13:
            fileOpen.write(" -15<T<= 0,")
        if i==19:
            fileOpen.write("0<T<=15,")
        if i==25:
            fileOpen.write("15<T<=30,")
        if i==31:
            fileOpen.write("30<T<=45,")
        if i==37:
            fileOpen.write("45<T<=60,")
        if i==43:
            fileOpen.write("T>=60,")        
        fileOpen.write(HVBHDM_01[i-1])
        fileOpen.write(",")
        if i%6 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_02"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_02.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Charge Operation Time充电操作时间 (HVBHDM2)")    
    print(HVBHDM_02)

    #white data 
    fileOpen.write("Charge Operation Time充电操作时间 (HVBHDM2) UNIT(ms)\n")
    fileOpen.write(",0<i<=30,30<i<=60,60<i<=90,90<i<=120,120<i<=180,180<i<=240,240<i<=300,300<i<=360,\n")
    for i in range(1,65,1):
        if i==1:
            fileOpen.write("T<=-35,")
        if i==9:
            fileOpen.write(" -35<T<=-15,")
        if i==17:
            fileOpen.write(" -15<T<= 0,")
        if i==25:
            fileOpen.write("0<T<=15,")
        if i==33:
            fileOpen.write("15<T<=30,")
        if i==41:
            fileOpen.write("30<T<=45,")
        if i==49:
            fileOpen.write("45<T<=60,")
        if i==57:
            fileOpen.write("T>=60,")        
        fileOpen.write(HVBHDM_02[i-1])
        fileOpen.write(",")
        if i%8 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_03"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_03.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
                
    print("Discharge Operation Time 放电 运行时间(HVBHDM3)")    
    print(HVBHDM_03)

    #white data 
    fileOpen.write("Discharge Operation Time 放电 运行时间(HVBHDM3) UNIT(ms)\n")
    fileOpen.write(",0<i<=30,30<i<=60,60<i<=90,90<i<=120,120<i<=180,180<i<=240,240<i<=300,300<i<=360,\n")
    for i in range(1,65,1):
        if i==1:
            fileOpen.write("T<=-35,")
        if i==9:
            fileOpen.write(" -35<T<=-15,")
        if i==17:
            fileOpen.write(" -15<T<= 0,")
        if i==25:
            fileOpen.write("0<T<=15,")
        if i==33:
            fileOpen.write("15<T<=30,")
        if i==41:
            fileOpen.write("30<T<=45,")
        if i==49:
            fileOpen.write("45<T<=60,")
        if i==57:
            fileOpen.write("T>=60,")        
        fileOpen.write(HVBHDM_03[i-1])
        fileOpen.write(",")
        if i%8 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_04"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_04.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)

    print("External-Charge Operation Time外部充电运行时间 (HVBHDM4)")
    print(HVBHDM_04)

    #white data 
    fileOpen.write("External-Charge Operation Time外部充电运行时间 (HVBHDM4) UNIT(ms)\n")
    fileOpen.write(",0<i<=30,30<i<=60,60<i<=90,90<i<=120,120<i<=180,180<i<=240,240<i<=300,300<i<=360,\n")
    for i in range(1,65,1):
        if i==1:
            fileOpen.write("T<=-35,")
        if i==9:
            fileOpen.write(" -35<T<=-15,")
        if i==17:
            fileOpen.write(" -15<T<= 0,")
        if i==25:
            fileOpen.write("0<T<=15,")
        if i==33:
            fileOpen.write("15<T<=30,")
        if i==41:
            fileOpen.write("30<T<=45,")
        if i==49:
            fileOpen.write("45<T<=60,")
        if i==57:
            fileOpen.write("T>=60,")        
        fileOpen.write(HVBHDM_04[i-1])
        fileOpen.write(",")
        if i%8 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_05"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_05.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("SOC Interval Operation TimeSOC间隔 运行时间 (HVBHDM5)")    
    print(HVBHDM_05)


    fileOpen.write("SOC Interval Operation TimeSOC间隔 运行时间 (HVBHDM5) UNIT(s)\n")
    fileOpen.write("0<SOC<=10,10<SOC<=30,30<SOC<=50,50<SOC<=70,70<SOC<=90,90<SOC<=100,\n")
    for i in HVBHDM_05:
        
        fileOpen.write(i)
        fileOpen.write(",")
    fileOpen.write("\n")




    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_06"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_06.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)

    print("Delta SOC Counter during Drive-Mode   驱动模式下的SOC变化计数器(HVBHDM6)")    
    print(HVBHDM_06)

    #white data 
    fileOpen.write("Delta SOC Counter during Drive-Mode   驱动模式下的SOC变化计数器(HVBHDM6)UNIT(%)\n")
    fileOpen.write(",0<dSOC<1,1<dSOC<2,2<dSOC<5,5<dSOC<10,10<dSOC<15,15<dSOC<20,20<dSOC<30,30<dSOC<40,40<dSOC<50,dSOC>50,\n")
    for i in range(1,21,1):
        if i==1:
            fileOpen.write("Charge circle,")
        if i==11:
            fileOpen.write(" discharge circle,") 
        fileOpen.write(HVBHDM_06[i-1])
        fileOpen.write(",")
        if i%10 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_07"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_07.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
        
    print("Delta SOC Counter during AC-Charge  AC充电期间的SOC变化计数器(HVBHDM7)")
    print(HVBHDM_07)

    #white data 
    fileOpen.write("Delta SOC Counter during AC-Charge  AC充电期间的SOC变化计数器(HVBHDM7)\n")
    fileOpen.write("Row is start SOC,0<SOC<=10,10<SOC<=30,30<SOC<=50,50<SOC<=70,70<SOC<=90,90<SOC<=100,\n")
    for i in range(1,22,1):
        if i==1:
            fileOpen.write("0<SOC<=10,")
        if i==7:
            fileOpen.write("10<SOC<=30,null,")
        if i==12:
            fileOpen.write("30<SOC<=50,null,null,")
        if i==16:
            fileOpen.write("50<SOC<=70,null,null,null,")
        if i==19:
            fileOpen.write("70<SOC<=90,null,null,null,null,")
        if i==21:
            fileOpen.write("90<SOC<=100,null,null,null,null,null,")   
        
        fileOpen.write(HVBHDM_07[i-1])
        fileOpen.write(",")
        if i in [6,11,15,18,20] : 
            fileOpen.write("\n")        
    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_08"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_08.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
        
    print("Delta SOC Counter during DC-Charge 直流充电期间的Delta SOC计数器 (HVBHDM8)")
    print(HVBHDM_08)

    #white data 
    fileOpen.write("Delta SOC Counter during DC-Charge 直流充电期间的Delta SOC计数器 (HVBHDM8)\n")
    fileOpen.write("Row is start SOC,0<SOC<=10,10<SOC<=30,30<SOC<=50,50<SOC<=70,70<SOC<=90,90<SOC<=100,\n")
    for i in range(1,22,1):
        if i==1:
            fileOpen.write("0<SOC<=10,")
        if i==7:
            fileOpen.write("10<SOC<=30,null,")
        if i==12:
            fileOpen.write("30<SOC<=50,null,null,")
        if i==16:
            fileOpen.write("50<SOC<=70,null,null,null,")
        if i==19:
            fileOpen.write("70<SOC<=90,null,null,null,null,")
        if i==21:
            fileOpen.write("90<SOC<=100,null,null,null,null,null,")   
        
        fileOpen.write(HVBHDM_08[i-1])
        fileOpen.write(",")
        if i in [6,11,15,18,20] : 
            fileOpen.write("\n")
            
    fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_09"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_09.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
        
    print("Cell Balancing Duration电池平衡持续时间 (HVBHDM9)")
    print(HVBHDM_09)

    #white data 
    fileOpen.write("Cell Balancing Duration电池平衡 持续时间(HVBHDM9) UNIT(s)\n ")
    fileOpen.write("Row is module,1,2,3,4,5,6,\n")
                
    for i in range(1,97,1):
        if i%6 == 1:
            fileOpen.write("modue {}".format(str(int(i/6)+1)))
            fileOpen.write(",")
        fileOpen.write(HVBHDM_09[i-1])
        fileOpen.write(",")
        if i%6 == 0: 
            fileOpen.write("\n")
            
    fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_10"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_10.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Battery Balancing delta SOC Counter 电池平衡SOC变化计数器 (HVBHDM10)")    
    print(HVBHDM_10)

    fileOpen.write("Battery Balancing delta SOC Counter 电池平衡SOC变化计数器 (HVBHDM10) UNIT(s)\n")
    fileOpen.write("0<dSOC<2,2<dSOC<3,3<dSOC<4,4<dSOC<6,6<dSOC<8,8<dSOC<10,10<dSOC<12,12<dSOC<15,15<dSOC<20,dSOC>20,\n")
    for i in HVBHDM_10:
        
        fileOpen.write(i)
        fileOpen.write(",")
    fileOpen.write("\n")



    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_11"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_11.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Charge/Discharge Current Limit Violation Time充电/放电电流限制违规时间 (HVBHDM11)")    
    print(HVBHDM_11)

    #white data 
    fileOpen.write("Charge/Discharge Current Limit Violation Time充电/放电电流限制违规时间 (HVBHDM11) UNIT(ms)\n")
    fileOpen.write(",T<=-30, -30<T<=-15, -15<T<=0, 0<T<=15, 15<T<=30,30<T<=45,45<T<=60,T>60,\n")
    for i in range(1,17,1):
        if i==1:
            fileOpen.write("Charge current violation,")
        if i==9:
            fileOpen.write("discharge current violation,") 
        fileOpen.write(HVBHDM_11[i-1])
        fileOpen.write(",")
        if i%8 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_12"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_12.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Upper/Lower Voltage Limit Violation Time 上限/下限电压限制违规 时间(HVBHDM12)")    
    print(HVBHDM_12)

    #white data 
    fileOpen.write("Upper/Lower Voltage Limit Violation Time 上限/下限电压限制违规 时间(HVBHDM12) UNIT(ms)\n")
    fileOpen.write(",T<=-30, -30<T<=-15, -15<T<=0, 0<T<=15, 15<T<=30,30<T<=45,45<T<=60,T>60,\n")
    for i in range(1,17,1):
        if i==1:
            fileOpen.write("Charge current violation,")
        if i==9:
            fileOpen.write("discharge current violation,") 
        fileOpen.write(HVBHDM_12[i-1])
        fileOpen.write(",")
        if i%8 == 0: 
            fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_13"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_13.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("SOC OCV Adaption History SOC OCV适应历史(HVBHDM13)")    
    print(HVBHDM_13)

    fileOpen.write("SOC OCV Adaption History SOC OCV适应历史(HVBHDM13) UNIT(%)\n")
    fileOpen.write("0<dSOC<1,1<dSOC<2,2<dSOC<4,4<dSOC<6,6<dSOC<8,8<dSOC<10,10<dSOC<15,dSOC>15,\n")
    for i in HVBHDM_13:
        
        fileOpen.write(i)
        fileOpen.write(",")
    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_14"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_14.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Capacit IES 容量 (HVBHDM14)")    
    print(HVBHDM_14)

    #white data 
    fileOpen.write("Capacit IES 容量 (HVBHDM14) UNIT(10mAh for battery capacities and 200mAh for cell capacities)\n ")
    fileOpen.write("Row is module,1,2,3,4,5,6,\n")
                
    for i in range(1,97,1):
        if i%6 == 1:
            fileOpen.write("modue {}".format(str(int(i/6)+1)))
            fileOpen.write(",")
        fileOpen.write(HVBHDM_14[i-1])
        fileOpen.write(",")
        if i%6 == 0: 
            fileOpen.write("\n")
            
    fileOpen.write("\n")
    fileOpen.write("\n")



    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_15"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_15.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Cell Capacity Development History电池容量历史 (HVBHDM15)")    
    print(HVBHDM_15)

    #white data 
    fileOpen.write("Cell Capacity Development History电池容量历史 (HVBHDM15)\n ")
    fileOpen.write("Row is history ring ,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,\n")
                
    for i in range(1,641,1):
        if i%16 == 1:
            fileOpen.write("History {}".format(str(int(i/6)+1)))
            fileOpen.write(",")
        fileOpen.write(HVBHDM_15[i-1])
        fileOpen.write(",")
        if i%16 == 0: 
            fileOpen.write("\n")
            
    fileOpen.write("\n")
    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="历史记录数据16 [$74CD]"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_16.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Discharge Internal Resistances放电内阻 (HVBHDM16)")    
    print(HVBHDM_16)

    #white data 
    fileOpen.write("Discharge Internal Resistances放电内阻 (HVBHDM16)\n ")

    fileOpen.write("resolution: 0.25 mOhm for battery resistance and  \
    0.01mOhm for cell resistances and 0.5 °C for temperature (range: -40…87.5°C) and 1 A for current and 0.5% for SOC\n ")

    fileOpen.write("temperature:,{}\n \
    current:,{}\n\
    SOC:,{}\n \
    battery internal discharge resistance :,{}\n \
    number of cell internal discharge resistances:,{}\n\
    cell internal discharge resistances,{}\n".format(HVBHDM_16[0],HVBHDM_16[1],HVBHDM_16[2],HVBHDM_16[3],HVBHDM_16[4],HVBHDM_16[5]))
                
    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_17"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_17.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Contactor Opened Counter接触器开启计数器 (HVBHDM17)")    
    print(HVBHDM_17)

    #white data 
    fileOpen.write("Contactor Opened Counter接触器开启计数器(HVBHDM17)\n ")

    fileOpen.write("Main Contactors opened while |  IBat | < =2A (tbd):,{}\n \
    Main Contactors opened while < 2A (tbd) < | IBat | < 60A (tbd):,{}\n\
    Main Contactors opened while | IBat | >= 60A (tbd):,{}\n \
    DC Contactors opened while |  IBat | <= 2A (tbd) :,{}\n \
    DC Contactors opened while < 2A (tbd) < | IBat | < 60A (tbd):,{}\n\
    DC Contactors opened while | IBat | >= 60A (tbd),{}\n".format(HVBHDM_17[0],HVBHDM_17[1],HVBHDM_17[2],HVBHDM_17[3],\
                                                                HVBHDM_17[4],HVBHDM_17[5]))

    fileOpen.write("\n")


    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_18"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_18.append(float(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Charge/Energy Integrator充电/能量积分器 (HVBHDM18)")    
    print(HVBHDM_18)

    #white data 
    fileOpen.write("Charge/Energy Integrator充电/能量积分器 (HVBHDM18)\n ")

    fileOpen.write("mAhLifeCharge:,{}\n \
    WhLifeCharge:,{}\n\
    mAhLifeDischarge:,{}\n \
    WhLifeDischarge:,{}\n \
    mAhLifeACCharge:,{}\n\
    WhLifeACCharge:,{}\n mAhLifeDCCharge:,{}\n WhLifeDCCharge:,{}\n".format(HVBHDM_18[0],HVBHDM_18[1],HVBHDM_18[2],HVBHDM_18[3],\
                                                                HVBHDM_18[4],HVBHDM_18[5],HVBHDM_18[6],HVBHDM_18[7]))

    fileOpen.write("\n")

    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_19"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_19.append(str(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Operation Time运行时间 (HVBHDM19)")    
    print(HVBHDM_19)

    #white data 
    fileOpen.write("Operation Time运行时间 (HVBHDM19) unit(10s)\n ")

    fileOpen.write("Total operation time:,{}\n \
    Operation time during OFF (Sleep-Mode):,{}\n\
    Operation time during OFF (Drive-Mode):,{}\n\
    Operation time during HV_ON (AC-Charge-Mode):,{}\n \
    Operation time during HV_ON (DC-Charge-Mode):,{}\n \
    Operation time during HV_OFF:,{}\n\
    Operation time during Emergency_OFF,{}\n".format(HVBHDM_19[0],HVBHDM_19[1],HVBHDM_19[2],HVBHDM_19[3],\
                                                                HVBHDM_19[4],HVBHDM_19[5],HVBHDM_19[6]))

    fileOpen.write("\n")



    for elem in sel.xpath('//display_name[text()="[LO]_Wrapper HVBHDM_20"]'):
        #print(elem)
        #print(elem.getparent())
        for child in elem.getparent():
            #print(child)
            #print(child.tag,child.text)
            for children in child:
                if children.tag == "display_value":
                    HVBHDM_20.append(float(int("0x"+children.text,0)))
            #if child.nodeName == 'display_value':
            # print(child.nodeValue)
    print("Temperature Integration温度累计 (HVBHDM20)")    
    print(HVBHDM_20)

    fileOpen.write("Temperature Integration温度累计 (HVBHDM20) unit(10s)\n ")

    fileOpen.write("Temperature integrator over the total operation time:,{}\n \
    Temperature integrator during OFF (Sleep-Mode):,{}\n\
    Temperature integrator during HV_ON (Drive-Mode):,{}\n \
    Temperature integrator during HV_ON (AC-Charge-Mode):,{}\n \
    Temperature integrator during HV_ON (DC-Charge_Mode):,{}\n\
    Temperature integrator during HV_OFF,{}\nTemperature integrator during Emergency_OFF,{}\n".format(HVBHDM_19[0],HVBHDM_19[1],HVBHDM_19[2],HVBHDM_19[3],\
                                                                HVBHDM_19[4],HVBHDM_19[5],HVBHDM_19[6]))

    fileOpen.write("\n")


if __name__ == "__main__":
    cwd=os.getcwd()
    files = os.listdir(cwd)
    vmtFiles = [f for f in files if f.endswith(".xml")]
    print(vmtFiles)
    for vmtFile in vmtFiles:
        
        
        fullpathname=vmtFile
        #print(fullpathname)
        readAndTranform(vmtFile)
        