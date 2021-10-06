import os
import unittest
from skidl import *


class UnitTestsElectronicDesignAutomationSkidlExamples(unittest.TestCase):
    def test_introduction(self):
        print("test_introduction")

        # Create input & output voltages and ground reference.
        vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

        # Create two resistors.
        r1, r2 = 2 * Part("Device", 'R', TEMPLATE, footprint='Resistor_SMD.pretty:R_0805_2012Metric')
        r1.value = '1K'  # Set upper resistor value.
        r2.value = '500'  # Set lower resistor value.

        # Connect the nets and resistors.
        vin += r1[1]  # Connect the input to the upper resistor.
        gnd += r2[2]  # Connect the lower resistor to ground.
        vout += r1[2], r2[1]  # Output comes from the connection of the two resistors.

        # Or you could do it with a single line of code:
        # vin && r1 && vout && r2 && gnd

        # Output the netlist to a file.
        generate_netlist()

    def test_finding_parts(self):
        print("test_finding_parts")

        with open("finding_parts.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('opamp') \n")
            file.write("search('^lm386$') \n")
            file.write("search('opamp low-noise dip-8') \n")
            file.write("search('opamp (low-noise|dip-8)') \n")
            file.write("search('opamp " + '"' + "high performance" + '"' + ")  \n")
            file.write("show('Amplifier_Audio', 'lm386') \n")
            file.write("show('Amplifier_Audio', 'lm38') \n")
            file.write("search_footprints('QFN-48') \n")

        os.system("python finding_parts.py")

    def test_instantiating_parts(self):
        print("test_instantiating_parts")

        with open('instantiating_parts.py', 'w') as file:
            file.write("from skidl import * \n\n")
            file.write("resistor = Part('Device','R') \n")
            file.write("resistor.value = '1K' \n")
            file.write("print('resistor.value : ' + resistor.value) \n")
            file.write("resistor = Part('Device','R', value='2K') \n")
            file.write("print('resistor.value : ' + resistor.value) \n")
            file.write("print('resistor.value : ' + resistor.value) \n")
            file.write("print('resistor.ref : ' + resistor.ref) \n")
            file.write("resistor.ref = 'R5' \n")
            file.write("print('resistor.ref : ' + resistor.ref) \n")
            file.write("another_res = Part('Device','R') \n")
            file.write("print('another_res.ref : ' + another_res.ref) \n")
            file.write("resistor.ref = 'R1' \n")
            file.write("print('resistor.ref : ' + resistor.ref) \n")

        os.system("python instantiating_parts.py")

    def test_connecting_pins(self):
        print("test_connecting_pins")

        with open('connecting_pins.py', 'w') as file:
            file.write("from skidl import * \n\n")
            file.write("rup = Part('Device', 'R', value='1K', footprint='Resistor_SMD.pretty:R_0805_2012Metric') \n")
            file.write("rlow = Part('Device', 'R', value='500', footprint='Resistor_SMD.pretty:R_0805_2012Metric') \n")
            file.write("print('rup.ref : ' + rup.ref) \n")
            file.write("print('rlow.ref : ' + rlow.ref) \n")
            file.write("print('rup.value : ' + rup.value) \n")
            file.write("print('rup.value : ' + rlow.value) \n")
            file.write("v_in = Net('VIN') \n")
            file.write("print('v_in.name : ' + str(v_in.name)) \n")
            file.write("rup[1] += v_in \n")
            file.write("print('rup[1].net : ' + str(rup[1].net)) \n")
            file.write("gnd = Net('GND') \n")
            file.write("rlow[1] += gnd \n")
            file.write("print('rlow[1].net : ' + str(rlow[1].net)) \n")
            file.write("v_out = Net('VO') \n")
            file.write("v_out += rup[2], rlow[2] \n")
            file.write("print('rup[2].net : ' + str(rup[2].net)) \n")
            file.write("print('rlow[2].net : ' + str(rlow[2].net)) \n")
            file.write("rup[2] += rlow[2] \n")
            file.write("v_out = Net('VO') \n")
            file.write("v_out += rlow[2] \n")
            file.write("print('rup[2].net : ' + str(rup[2].net)) \n")
            file.write("print('rlow[2].net : ' + str(rlow[2].net)) \n")
            file.write("ERC() \n")
            file.write("v_in.do_erc = False \n")
            file.write("gnd.do_erc = False \n")
            file.write("ERC() \n")
            file.write("generate_netlist() \n")
            file.write("generate_xml() \n")

        os.system("python connecting_pins.py")

    def test_searching_transistor_npn(self):
        print("test_searching_transistor_npn")

        with open("searching_transistor_npn.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('transistor (npn)') \n")

        os.system("python searching_transistor_npn.py")

    def test_searching_bridge_rectifier(self):
        print("test_searching_bridge_rectifier")

        with open("test_searching_bridge_rectifier.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('bridge rectifier') \n")

        os.system("python test_searching_bridge_rectifier.py")

    def test_searching_optocoupler(self):
        print("test_searching_optocoupler")

        with open("test_searching_optocoupler.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('optocoupler') \n")

        os.system("python test_searching_optocoupler.py")

    def test_searching_resistor(self):
        print("test_searching_resistor")

        with open("test_searching_resistor.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('resistor') \n")

        os.system("python test_searching_resistor.py")

    def test_searching_terminal_block(self):
        print("test_searching_terminal_block")

        with open("test_searching_terminal_block.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('analog') \n")

        os.system("python test_searching_terminal_block.py")

    def test_searching_footprint(self):
        print("test_searching_footprint")

        with open("test_searching_footprint.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search('footprint') \n")

        os.system("python test_searching_footprint.py")

    def test_searching_footprints_of_one_resistor(self):
        print("test_searching_footprints_of_one_resistor")

        with open("test_searching_footprints_of_one_resistor.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search_footprints('R') \n")

        os.system("python test_searching_footprints_of_one_resistor.py")

    def test_searching_footprints_of_one_transistor(self):
        print("test_searching_footprints_of_one_transistor")

        with open("test_searching_footprints_of_one_transistor.py", "w") as file:
            file.write("from skidl import * \n\n")
            file.write("search_footprints('transistor') \n")

        os.system("python test_searching_footprints_of_one_transistor.py")

    def test_searching_footprints_of_one_optocoupler(self):
        print("test_searching_footprints_of_one_optocoupler")

        with open("test_searching_footprints_of_one_optocoupler.py", "w") as file:
            file.write("from skidl import * \n\n")
            # file.write("search_footprints('optocoupler') \n")
            file.write("search_footprints('Relay_SolidState') \n")

        os.system("python test_searching_footprints_of_one_optocoupler.py")

    def test_searching_footprints_of_one_diode_bridge_rectifier(self):
        print("test_searching_footprints_of_one_diode_bridge_rectifier")

        with open("test_searching_footprints_of_one_diode_bridge_rectifier.py", "w") as file:
            file.write("from skidl import * \n\n")
            # file.write("search_footprints('bridge rectifier') \n")
            # file.write("search_footprints('GUO40-08NO1') \n")
            file.write("search_footprints('Diode_Bridge') \n")

        os.system("python test_searching_footprints_of_one_diode_bridge_rectifier.py")


if __name__ == '__main__':
    unittest.main()
