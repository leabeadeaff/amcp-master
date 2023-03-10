EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "ACMP - XTAL Test Fixture"
Date "2019-08-24"
Rev "v0.1"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:R R6
U 1 1 5D6124B7
P 7450 4950
F 0 "R6" H 7520 4996 50  0000 L CNN
F 1 "158R" H 7520 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7380 4950 50  0001 C CNN
F 3 "~" H 7450 4950 50  0001 C CNN
	1    7450 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R4
U 1 1 5D61253A
P 6950 4950
F 0 "R4" H 7020 4996 50  0000 L CNN
F 1 "14R2" H 7020 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6880 4950 50  0001 C CNN
F 3 "~" H 6950 4950 50  0001 C CNN
	1    6950 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R5
U 1 1 5D61256E
P 7200 4500
F 0 "R5" V 6993 4500 50  0000 C CNN
F 1 "66R5" V 7084 4500 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7130 4500 50  0001 C CNN
F 3 "~" H 7200 4500 50  0001 C CNN
	1    7200 4500
	0    1    1    0   
$EndComp
$Comp
L Device:R R3
U 1 1 5D612D46
P 5050 4950
F 0 "R3" H 5120 4996 50  0000 L CNN
F 1 "14R2" H 5120 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4980 4950 50  0001 C CNN
F 3 "~" H 5050 4950 50  0001 C CNN
	1    5050 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R1
U 1 1 5D612D4C
P 4550 4950
F 0 "R1" H 4620 4996 50  0000 L CNN
F 1 "158R" H 4620 4905 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4480 4950 50  0001 C CNN
F 3 "~" H 4550 4950 50  0001 C CNN
	1    4550 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:R R2
U 1 1 5D612D52
P 4800 4500
F 0 "R2" V 4593 4500 50  0000 C CNN
F 1 "66R5" V 4684 4500 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4730 4500 50  0001 C CNN
F 3 "~" H 4800 4500 50  0001 C CNN
	1    4800 4500
	0    1    1    0   
$EndComp
$Comp
L Device:C C1
U 1 1 5D612DA1
P 5550 4950
F 0 "C1" H 5665 4996 50  0000 L CNN
F 1 "33n" H 5665 4905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5588 4800 50  0001 C CNN
F 3 "~" H 5550 4950 50  0001 C CNN
	1    5550 4950
	1    0    0    -1  
$EndComp
$Comp
L Device:C C2
U 1 1 5D612EBD
P 6450 4950
F 0 "C2" H 6565 4996 50  0000 L CNN
F 1 "33n" H 6565 4905 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6488 4800 50  0001 C CNN
F 3 "~" H 6450 4950 50  0001 C CNN
	1    6450 4950
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 5100 6450 5400
Wire Wire Line
	6450 5400 6950 5400
Wire Wire Line
	7450 5400 7450 5100
Wire Wire Line
	6950 5400 6950 5100
Connection ~ 6950 5400
Wire Wire Line
	6950 5400 7450 5400
Wire Wire Line
	6950 4800 6950 4500
Wire Wire Line
	6950 4500 7050 4500
Wire Wire Line
	6950 4500 6450 4500
Wire Wire Line
	6450 4500 6450 4800
Connection ~ 6950 4500
Wire Wire Line
	7350 4500 7450 4500
Wire Wire Line
	7450 4500 7450 4800
Wire Wire Line
	5550 5100 5550 5400
Wire Wire Line
	5550 5400 5050 5400
Wire Wire Line
	5050 5400 5050 5100
Wire Wire Line
	5050 5400 4550 5400
Wire Wire Line
	4550 5400 4550 5100
Connection ~ 5050 5400
Wire Wire Line
	4550 4800 4550 4500
Wire Wire Line
	4550 4500 4650 4500
Wire Wire Line
	4950 4500 5050 4500
Wire Wire Line
	5050 4500 5050 4800
Wire Wire Line
	5050 4500 5550 4500
Wire Wire Line
	5550 4500 5550 4800
Connection ~ 5050 4500
Wire Wire Line
	5550 4500 5850 4500
Connection ~ 5550 4500
Wire Wire Line
	6150 4500 6450 4500
Connection ~ 6450 4500
Wire Wire Line
	5550 5400 6000 5400
Connection ~ 5550 5400
Connection ~ 6450 5400
$Comp
L Connector:Conn_Coaxial J2
U 1 1 5D614489
P 7950 4500
F 0 "J2" H 7950 4750 50  0000 L CNN
F 1 "Conn_Coaxial" H 7700 4650 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 7950 4500 50  0001 C CNN
F 3 " ~" H 7950 4500 50  0001 C CNN
	1    7950 4500
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J1
U 1 1 5D614539
P 4050 4500
F 0 "J1" H 3980 4738 50  0000 C CNN
F 1 "Conn_Coaxial" H 3980 4647 50  0000 C CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 4050 4500 50  0001 C CNN
F 3 " ~" H 4050 4500 50  0001 C CNN
	1    4050 4500
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4250 4500 4550 4500
Connection ~ 4550 4500
Wire Wire Line
	4050 4700 4050 5400
Wire Wire Line
	4050 5400 4550 5400
Connection ~ 4550 5400
Wire Wire Line
	7950 4700 7950 5400
Wire Wire Line
	7950 5400 7450 5400
Connection ~ 7450 5400
Wire Wire Line
	7750 4500 7450 4500
Connection ~ 7450 4500
$Comp
L power:GND #PWR01
U 1 1 5D615546
P 6000 5500
F 0 "#PWR01" H 6000 5250 50  0001 C CNN
F 1 "GND" H 6005 5327 50  0000 C CNN
F 2 "" H 6000 5500 50  0001 C CNN
F 3 "" H 6000 5500 50  0001 C CNN
	1    6000 5500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 5500 6000 5400
Wire Wire Line
	6000 5400 6450 5400
Text Notes 5650 3900 0    50   ~ 0
Crystal sees 25 Ohm\nCL=19 pF
Text Notes 3350 4550 0    50   ~ 0
50 Ohm to VNA
Text Notes 5150 4500 0    50   ~ 0
12.5Ohm 
Connection ~ 6000 5400
Wire Wire Line
	6000 4700 6000 5400
$Comp
L power:GND #PWR02
U 1 1 5DDDDC5E
P 6000 4150
F 0 "#PWR02" H 6000 3900 50  0001 C CNN
F 1 "GND" H 6005 3977 50  0000 C CNN
F 2 "" H 6000 4150 50  0001 C CNN
F 3 "" H 6000 4150 50  0001 C CNN
	1    6000 4150
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 4150 6000 4300
$Comp
L Device:Crystal_GND24 Y1
U 1 1 5DDDC3CC
P 6000 4500
F 0 "Y1" H 6194 4546 50  0000 L CNN
F 1 "AXS-3225-04-02" H 6194 4455 50  0000 L CNN
F 2 "abracon:AXS-3225-04-02" H 6000 4500 50  0001 C CNN
F 3 "~" H 6000 4500 50  0001 C CNN
	1    6000 4500
	1    0    0    -1  
$EndComp
NoConn ~ 6000 4500
$Comp
L Device:R R12
U 1 1 5E3FE187
P 7450 2450
F 0 "R12" H 7520 2496 50  0000 L CNN
F 1 "158R" H 7520 2405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7380 2450 50  0001 C CNN
F 3 "~" H 7450 2450 50  0001 C CNN
	1    7450 2450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R10
U 1 1 5E3FE191
P 6950 2450
F 0 "R10" H 7020 2496 50  0000 L CNN
F 1 "14R2" H 7020 2405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 6880 2450 50  0001 C CNN
F 3 "~" H 6950 2450 50  0001 C CNN
	1    6950 2450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R11
U 1 1 5E3FE19B
P 7200 2000
F 0 "R11" V 6993 2000 50  0000 C CNN
F 1 "66R5" V 7084 2000 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 7130 2000 50  0001 C CNN
F 3 "~" H 7200 2000 50  0001 C CNN
	1    7200 2000
	0    1    1    0   
$EndComp
$Comp
L Device:R R9
U 1 1 5E3FE1A5
P 5050 2450
F 0 "R9" H 5120 2496 50  0000 L CNN
F 1 "14R2" H 5120 2405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4980 2450 50  0001 C CNN
F 3 "~" H 5050 2450 50  0001 C CNN
	1    5050 2450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R7
U 1 1 5E3FE1AF
P 4550 2450
F 0 "R7" H 4620 2496 50  0000 L CNN
F 1 "158R" H 4620 2405 50  0000 L CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4480 2450 50  0001 C CNN
F 3 "~" H 4550 2450 50  0001 C CNN
	1    4550 2450
	1    0    0    -1  
$EndComp
$Comp
L Device:R R8
U 1 1 5E3FE1B9
P 4800 2000
F 0 "R8" V 4593 2000 50  0000 C CNN
F 1 "66R5" V 4684 2000 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" V 4730 2000 50  0001 C CNN
F 3 "~" H 4800 2000 50  0001 C CNN
	1    4800 2000
	0    1    1    0   
$EndComp
$Comp
L Device:C C3
U 1 1 5E3FE1C3
P 5550 2450
F 0 "C3" H 5665 2496 50  0000 L CNN
F 1 "33n" H 5665 2405 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 5588 2300 50  0001 C CNN
F 3 "~" H 5550 2450 50  0001 C CNN
	1    5550 2450
	1    0    0    -1  
$EndComp
$Comp
L Device:C C4
U 1 1 5E3FE1CD
P 6450 2450
F 0 "C4" H 6565 2496 50  0000 L CNN
F 1 "33n" H 6565 2405 50  0000 L CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6488 2300 50  0001 C CNN
F 3 "~" H 6450 2450 50  0001 C CNN
	1    6450 2450
	1    0    0    -1  
$EndComp
Wire Wire Line
	6450 2600 6450 2900
Wire Wire Line
	6450 2900 6950 2900
Wire Wire Line
	7450 2900 7450 2600
Wire Wire Line
	6950 2900 6950 2600
Connection ~ 6950 2900
Wire Wire Line
	6950 2900 7450 2900
Wire Wire Line
	6950 2300 6950 2000
Wire Wire Line
	6950 2000 7050 2000
Wire Wire Line
	6950 2000 6450 2000
Wire Wire Line
	6450 2000 6450 2300
Connection ~ 6950 2000
Wire Wire Line
	7350 2000 7450 2000
Wire Wire Line
	7450 2000 7450 2300
Wire Wire Line
	5550 2600 5550 2900
Wire Wire Line
	5550 2900 5050 2900
Wire Wire Line
	5050 2900 5050 2600
Wire Wire Line
	5050 2900 4550 2900
Wire Wire Line
	4550 2900 4550 2600
Connection ~ 5050 2900
Wire Wire Line
	4550 2300 4550 2000
Wire Wire Line
	4550 2000 4650 2000
Wire Wire Line
	4950 2000 5050 2000
Wire Wire Line
	5050 2000 5050 2300
Wire Wire Line
	5050 2000 5550 2000
Wire Wire Line
	5550 2000 5550 2300
Connection ~ 5050 2000
Wire Wire Line
	5550 2000 5850 2000
Connection ~ 5550 2000
Wire Wire Line
	6150 2000 6450 2000
Connection ~ 6450 2000
Wire Wire Line
	5550 2900 6000 2900
Connection ~ 5550 2900
Connection ~ 6450 2900
$Comp
L Connector:Conn_Coaxial J4
U 1 1 5E3FE1F8
P 7950 2000
F 0 "J4" H 7950 2250 50  0000 L CNN
F 1 "Conn_Coaxial" H 7700 2150 50  0000 L CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 7950 2000 50  0001 C CNN
F 3 " ~" H 7950 2000 50  0001 C CNN
	1    7950 2000
	1    0    0    -1  
$EndComp
$Comp
L Connector:Conn_Coaxial J3
U 1 1 5E3FE202
P 4050 2000
F 0 "J3" H 3980 2238 50  0000 C CNN
F 1 "Conn_Coaxial" H 3980 2147 50  0000 C CNN
F 2 "Connector_Coaxial:SMA_Amphenol_132289_EdgeMount" H 4050 2000 50  0001 C CNN
F 3 " ~" H 4050 2000 50  0001 C CNN
	1    4050 2000
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4250 2000 4550 2000
Connection ~ 4550 2000
Wire Wire Line
	4050 2200 4050 2900
Wire Wire Line
	4050 2900 4550 2900
Connection ~ 4550 2900
Wire Wire Line
	7950 2200 7950 2900
Wire Wire Line
	7950 2900 7450 2900
Connection ~ 7450 2900
Wire Wire Line
	7750 2000 7450 2000
Connection ~ 7450 2000
$Comp
L power:GND #PWR04
U 1 1 5E3FE216
P 6000 3000
F 0 "#PWR04" H 6000 2750 50  0001 C CNN
F 1 "GND" H 6005 2827 50  0000 C CNN
F 2 "" H 6000 3000 50  0001 C CNN
F 3 "" H 6000 3000 50  0001 C CNN
	1    6000 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6000 3000 6000 2900
Wire Wire Line
	6000 2900 6450 2900
Text Notes 5650 1400 0    50   ~ 0
Crystal sees 25 Ohm\nCL=19 pF
Text Notes 3350 2050 0    50   ~ 0
50 Ohm to VNA
Text Notes 5150 2000 0    50   ~ 0
12.5Ohm 
Connection ~ 6000 2900
Wire Wire Line
	6000 2200 6000 2900
$Comp
L power:GND #PWR03
U 1 1 5E3FE227
P 6000 1650
F 0 "#PWR03" H 6000 1400 50  0001 C CNN
F 1 "GND" H 6005 1477 50  0000 C CNN
F 2 "" H 6000 1650 50  0001 C CNN
F 3 "" H 6000 1650 50  0001 C CNN
	1    6000 1650
	-1   0    0    1   
$EndComp
Wire Wire Line
	6000 1650 6000 1800
$Comp
L Device:Crystal_GND24 Y2
U 1 1 5E3FE232
P 6000 2000
F 0 "Y2" H 6194 2046 50  0000 L CNN
F 1 "AXS-3225-04-02" H 6194 1955 50  0000 L CNN
F 2 "abracon:AXS-2016-04-04" H 6000 2000 50  0001 C CNN
F 3 "~" H 6000 2000 50  0001 C CNN
	1    6000 2000
	-1   0    0    -1  
$EndComp
NoConn ~ 6000 2000
$EndSCHEMATC