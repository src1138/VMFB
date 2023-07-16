A vending machine for birds that rewards them with food when they drop something in a hole. Electronics and enclosure materials cost <100 USD/EUR. I've designed a PCB and PVC pipe enclosure and dispenser (described below). The circuit is not complex, but I think a custom PCB makes it easier for people who are not electronics hobbyists to build this. I've made a few different enclosures ouot of scrap for this, but will share the PVC pipe enclosure details since it's sturdy, waterproof, and the materials can all be found at the hardware store.

There were two main inspirations for me to start and  document this project

- Hans Forsberg (https://www.youtube.com/channel/UCtkv3wuEP-Veur4iYJWkBgA) - designed his own machine and was the first person I learned of that had birds (magpies) bringing items to deposit on thier own
- Josh Klein (https://thecrowbox.com/) - makes his Crowbox designs freely available and supports people who want to build it

# MAIN FEATURES
- portable
- saves power until a warm body is present
- battery or mains powered
- one moving part
- accessible components and materials
- rodents can't break in and get the food
- cheap to build
- customizable

# ELECTRONICS, SENSORS, AND POWER

The circuit is all analog, using four NE555 timers and one LM358 dual op amp. The sensors are all made using IR phototransistors and IR LEDs. The PCB has headers broken out so you can monitor and control it with a microcontroller or SBC. It runs on 5-6VDC and uses ~10mA in standby (~20mA if timer and powerbank keep-alive are enabled), ~250mA when IR LEDs are on and ~400mA when the dispenser motor is running. A 10,000 mAh USB powerbank should last about a week.

- Powerbank Keep-Alive: 555 sinks current every 7-22 seconds for 0.7-2.2 seconds to keep USB power banks on while sensors are in standby - the powerbank keep-alive can be disabled.
- IR LED ON/OFF: 555 keeps the IR LEDs used by the sensors on for 22 seconds after the last PIR trigger
- Op Amps: LM358 used as comparators to adjust the threshold of the sensors and send signals when they are triggered
- Motor Controller: 555 turns on the dispenser vibration motor when the deposit sensors are triggered, tuns it off when the dispense sensor is triggered
- Timed Dispense: 555 dispenses food every 10-100min - timed dispense can be disabled
- Daytimer: Phototransistor that puts the timer in reset while it's dark outside - brightness threshold can be adjusted or disabled (Rev. B)
- PIR Sensor: Sends a signal to turn on the sensor IR LEDs
- Deposit/Dispense Sensors: IR phototransistors and IR LEDs used as proximity sensors to monitor the deposit and dispense chutes
- Hopper Level Sensor: IR phototransistor and IR LED to detect when the food level gets low (Rev. B)
- Monitoring/Control: lines for monitoring and triggering events with an external controller (Rev. B)

# PCB, BOM AND GERBERS

Kicad Files (Github): https://github.com/src1138/VMFB
Gerbers and PCB (PCBWay): https://www.pcbway.com/project/shareproject/Vending_Machine_for_Birds_eda585b3.html

Front
![image](https://github.com/src1138/VMFB/assets/15698079/49461066-83e9-48a8-94f1-31aabdd8c2f1)

Back
![image](https://github.com/src1138/VMFB/assets/15698079/f7248c04-e888-49ab-9023-a9d7b994f880)

The PCB has footprints for USB type A, USB type B, barrel jack and screw terminal power input. You only need to populate the ones you will use.

The Timer and Powerbank Keep-Alive are not essential and you don't have to populate the parts for them if you don't need/want to use them.

# HOW IT WORKS

## States
- Standby - No PIR trigger in the last 22 secs (IR LEDs are off)
- Sensors On - PIR was triggered in the last 22 secs (IR LEDs are on)
- Dispensing - Dispenser motor is on

## Modes

- Normal (dispenses on deposit)
- Timer (dispenses every x minutes AND dispenses on deposit)

## Event Sequence

1. PIR sensor sees a warm body
2. PIR triggers IR LED 555
3. IR LED 555 turn on sensor IR LEDs for 22 secs after last PIR trigger
4. When something is dropped in the deposit hole, the deposit sensor sees it
5. The deposit side of the dual op amp sends a pulse to trigger the motor 555
6. The motor 555 turns on the vibration dispenser motor - it times out after 11 secs
7. When something is dispensed, the dispense sensor sees it 
8. The dispense side of the dual op amp sends a pulse to reset the motor 555
9. The dispenser motor is stopped

When timed dispense is triggered, it sends a signal to turn on the sensor IR LEDs and triggers the motor controller to start the vibration dispenser. When something is dispensed, the motor stops.

# MONITORING

I was using a Rasperry Pi Zero W with a wide-angle camera module with my vending machine, but I wanted something that drew less power (and was cheaper and more available). I found that the ESP32-CAM module  consumes about 135 MA when streaming video, can be put to sleep (consuming just a few mA) and has 4 GPIO pins available when using the SD-card slot - it can stream/record video and log events from the vending machine, making it all available over wifi or bluetooth.

I'm still in the process of modifying the ESP32-CAM example program to monitor/log events and stream video, record video files to SD, and sleep until the PIR is triggered. I will put this code on Github when it's ready.

# DISPENSER, ENCLOSURE, AND MOUNTING

Dispenser: two-layer vibration platform with offset holes made from 3mm PVC sheet and 15mm M3 brass standoffs. I used a small 24x12mm 2VDC motor attached to the dispenser with brass standoffs and 3mm PVC sheet.
![image](https://github.com/src1138/VMFB/assets/15698079/7aa2b71b-9e1d-447d-a856-88bcf2f6c334)

Enclosure: made from 110mm and 50mm PVC pipe and joints, 32mm PVC joints, a 35mm plastic tray and a 1.5l PET bottle. 
![image](https://github.com/src1138/VMFB/assets/15698079/7a555fc7-618c-4dbf-8762-56bca356aacf)

Mounting: can be mounted on the ground, horizontal or vertical railing, wooden fence, wall, pole 
The dispenser typically dispenses a peanut or two within 3 seconds. Since it is a vibration dispenser, the enclosure should be level and mounted securely to insure relaible dispensing. 

The dispenser drops peanuts into a funnel made from the top of the PET bottle. There is about 12cm between the two, making it difficult for rodents small enough to get into the machine to get to the food. PVC is tough enough to keep larger rodents from gnawing or breaking thier way in.

# FEED

I used peanuts in the shell to attract birds to the area and shelled peanuts in the vending machine. If you live in an area with lots of pigeons, using peanuts in the shell will not attract them as much since they can't eat them (can't get he shell off) and you have a better chance of attracting corvids. Shelled peanuts are easier to dispense reliably - peanuts in the shell are less dense, more irregular in shape, and jam easily. Dry cat and dog food also works.

# BIRD CONDITIONING

Along with learning and having some fun, the goal is to get a birds to bring something, drop it in a hole, and get a reward. Birds need some conditioning for this, so there are a few phases to progress though to help them figure this out.

## Conditioning Stages
0 - Put food in the area you plan to mount the vending machine to start attracting birds
(1-2 weeks)
1 - Food Provided, Timed Dispense, Deposit Provided
(2-3 weeks)
2 - No Food Provided, Timed Dispense, Deposit Provided
(3-4 months)
3 - No Food Provided, No Timed Dispense, Deposit Provided
(6-8 months)
4 - No Food Provided, No Timed Dispense, No Deposit Provided

Time estimates are based on my own experience over the past year or so, but Phase 3 duration is a guess. As of July 2023 I have not yet seen a bird deposit an item I didn't provide. Unfortunately I had to take my machine down in May due to some new HOA regulations prohibiting feeding the birds in my neighborhood. I plan to redeploy it when I find another suitable location.

# PVC ENCLOSURE 

The PVC enclosure contains the battery, electronics and sensors, dispenser, peanuts, and deposited items. The platform is a 35cm plastic tray for a plant pot, attached to the deposit chute with 4 90-degree brackets, four M4 bolts and two hose clamps.

I used bits of electrical or duct tape to make the PVC pipes and joints fit securely tight. This way it is easy to disassemble/modify/repair. It's a good idea to wrap upward-facing joints to prevent water ingress during heavy rains.

You can load peanuts (or whatever) by unscrewing the top cap and pouring them in. I made two baffles from 3mm PVC sheet to reduce the pressure on the vibration dispenser.

You can unload the deposited items by unscrewing one of the caps on the lower half of the vending machine.
