# VMFB
Simple, inexpensive bird feeder that dispenses peanuts in exchange for dropping stuff in a hole. A vending machine for clever birds.

An inexpensive, simple bird feeder that dispenses a nut for stuff and can be built from analog components and discarded or scrap objects. Rodent proof, runs on 5-6V, one moving part (vibration motor). No 3D printing or laser cutting required, just some basic hand tools. Lots of improvement and customization possibilities. Lots of possibilities for the enclosure.

- powered by 5-6V
- comes on when the PIR sees a warm body, stays on until it's gone
- detects when something is dropped in a hole, anything that fits and reflects IR will work
- dispenses a shelled peanut or similar-sized treat (maybe two or three)
- dispenser design is rodent-proof
- cheap to make (electronic components, connectors, wires, motor cost ~25 EUR)
- small enough to be portable with various mounting options
- easy customize and improve upon

This PCB is for all the electronics required. The circuit is fairly straightforward:

- PIR sensor - this turns on the IR LEDs for the photodiode sensors when triggered.
- 555 monostable vibrator to keep the circuit on for ~45 secs after the PIR is triggered. There is a diode leading from pin 6/7 to the trigger. This allows the PIR to reset the timer during a cycle, keeping the thing continuously on while a bird is in front of the PIR.
- LM358 dual op amp for the IR proximity sensors made from IR leds and phototransistors
- another 555 for a monostable vibrator - when the drop sensor sees something it turns the vibration motor on, when the dispense sensor sees something it turns it back off. If the dispense sensor doesn't see a peanut within 24 seconds it turns the dispenser off.
- a 555 astable vibrator - to use as an optional timed dispense (5-60min) to get birds used to it as a food source
- another 555 astable vibrator - to use as an optional intermittent (8-25sec) current sink (for 0.7 to 2.25sec) to keep some powerbanks on when the IR LEDs are off
- small DC motor (the one I used is marked 2 volts) with an unbalanced load on the axle
- some resistors, capacitors, a few transistors and diodes and signal LEDs to indicate what's going on
