# skidl : https://xess.com/skidl/docs/_site/
# kicad : https://www.kicad.org/
import unittest
from skidl import *
import warnings


class Unit_Tests_EDA_Brevet_US_5_149_407_Water_Electrolyzer(unittest.TestCase):
    def test_electronic_design_automation_with_skidl_option_1(self):
        print("test_electronic_design_automation_with_skidl_option_1")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # Circuit
        circuit = Circuit()

        # Ground : G1
        G1 = Net('GND', circuit=circuit)

        # Bridge rectifier or diode bridge : BR1
        BR1 = Part("Diode_Bridge", 'KBU8G', footprint='Diode_THT:Diode_Bridge_Vishay_KBU', circuit=circuit)

        # TerminalBlock for the input of bridge rectifier BR1 : TB_I_BR1
        # TerminalBlock for the output of bridge rectifier BR1 : TB_O_BR1
        TB_BR1 = Part("Connector",
                      "Screw_Terminal_01x02",
                      footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal",
                      circuit=circuit)

        # Link the pin 2 of BR1 to TB_I_BR1
        BR1[2] += TB_BR1[1]

        # Link the pin 3 of BR1 to TB_O_BR1
        BR1[3] += TB_BR1[2]

        # Link the pin 4 of BR1 to GND
        BR1[4] += G1

        # Resistor : R1
        R1 = Part("Device",
                  "R",
                  value="100K",
                  footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal',
                  circuit=circuit)

        # Link the pin 1 of BR1 to the pin 1 of R1
        BR1[1] += R1[1]

        # Optocoupler : OC1
        OC1 = Part('Isolator', 'LTV-352T', footprint='Package_SO:SO-4_4.4x3.6mm_P2.54mm', circuit=circuit)

        # Link the pin 2 of R1 to the pin  of OC1
        R1[2] += OC1[4]

        # TerminalBlock for the input of optocoupler OC1 : TB_I_OC1
        # TerminalBlock for the output of optocoupler OC1 : TB_O_OC1
        TB_OC1 = Part("Connector",
                      "Screw_Terminal_01x02",
                      footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal",
                      circuit=circuit)

        # Link the pin 1 of OC1 to the pin 1 of TB_OC1
        OC1[1] += TB_OC1[1]

        # Link the pin 2 of OC1 to the pin 2 of TB_OC1
        OC1[2] += TB_OC1[2]

        # Transistor NPN : T1
        T1 = Part("Device", 'Q_NPN_CBE', footprint='Package_TO_SOT_THT:TO-264-3_Vertical', circuit=circuit)

        # Link the pin 1 of R1 to the pin C of T1
        R1[1] += T1['C']

        # Link the pin 3 of OC1 to the pin B of T1
        OC1[3] += T1['B']

        # TerminalBlock for the input of ground G1 : TB_I_G1
        # TerminalBlock for the emitter of transistor T1 : TB_E_T1
        TB_I_G1_E_T1 = Part("Connector",
                            "Screw_Terminal_01x02",
                            footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-2-5.08_1x02_P5.08mm_Horizontal",
                            circuit=circuit)

        # Link G1 to the pin 1 of TB_I_G1_E_T1
        TB_I_G1_E_T1[1] += G1

        # Link O_E_T1 to the pin 2 of TB_I_G1_E_T1
        T1['E'] += TB_I_G1_E_T1['Pin_2']

        # Check the circuit for errors.
        circuit.ERC()

        # Generate the netlist from the circuit object.
        circuit.generate_netlist()

        # Generate the xml from the circuit object.
        circuit.generate_xml()

        # Generate the DOT graph from the circuit object.
        # circuit.generate_graph()

        # Generate the SVG graph from the circuit object.
        # circuit.generate_svg()

    def test_electronic_design_automation_with_skidl_option_2(self):
        print("test_electronic_design_automation_with_skidl_option_2")

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        # Circuit
        circuit = Circuit()

        # Ground : G1
        G1 = Net('GND', circuit=circuit)

        # Bridge rectifier or diode bridge : BR1
        BR1 = Part("Diode_Bridge", 'KBU8G', footprint='Diode_THT:Diode_Bridge_Vishay_KBU', circuit=circuit)

        # Resistor : R1
        R1 = Part("Device",
                  "R",
                  value="100K",
                  footprint='Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal',
                  circuit=circuit)

        # Optocoupler : OC1
        OC1 = Part('Isolator', 'LTV-352T', footprint='Package_SO:SO-4_4.4x3.6mm_P2.54mm', circuit=circuit)

        # Transistor NPN : T1
        T1 = Part("Device", 'Q_NPN_CBE', footprint='Package_TO_SOT_THT:TO-264-3_Vertical', circuit=circuit)

        # TerminalBlock for the input of bridge rectifier BR1 : TB_I_BR1
        # TerminalBlock for the output of bridge rectifier BR1 : TB_O_BR1
        # TerminalBlock for the input of optocoupler OC1 : TB_I_OC1
        # TerminalBlock for the output of optocoupler OC1 : TB_O_OC1
        # TerminalBlock for the input of ground G1 : TB_I_G1
        # TerminalBlock for the emitter of transistor T1 : TB_E_T1
        TB = Part("Connector",
                  "Screw_Terminal_01x06",
                  footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_MKDS-1,5-6-5.08_1x06_P5.08mm_Horizontal",
                  circuit=circuit)

        # Link to the GND to the pin 1 of TB
        TB[1] += G1

        # Link to the pin 2 of TB to the pin 2 of BR1
        TB[2] += BR1[2]

        # Link to the pin 3 of TB to the pin 3 of BR1
        TB[3] += BR1[3]

        # Link to the pin 4 of TB to the pin 1 of OC1
        TB[4] += OC1[1]

        # Link to the pin 5 of TB to the pin 2 of OC1
        TB[5] += OC1[2]

        # Link to the pin 6 of TB to the pin E of T1
        TB[6] += T1['E']

        # Link the pin 4 of BR1 to the GND
        BR1[4] += G1

        # Link the pin 1 of R1 to the pin 1 of BR1
        R1[1] += BR1[1]

        # Link the pin 1 of R1 to the pin C of T1
        R1[1] += T1['C']

        # Link the pin 2 of R1 to the pin of 4 OC1
        R1[2] += OC1[4]

        # Link the pin 3 of OC1 to the pin B of T1
        OC1[3] += T1['B']

        # Check the circuit for errors.
        circuit.ERC()

        # Generate the netlist from the circuit object.
        circuit.generate_netlist()

        # Generate the xml from the circuit object.
        circuit.generate_xml()

        # Generate the DOT graph from the circuit object.
        # circuit.generate_graph()

        # Generate the SVG graph from the circuit object.
        # circuit.generate_svg()


if __name__ == '__main__':
    unittest.main()
