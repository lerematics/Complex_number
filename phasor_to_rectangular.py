import numpy as np

class Complex_Number:

    def __init__(self, abs_value=0, phase_angle=0):
        self.A = abs_value
        self.P = phase_angle

    def Phasor_to_Rectangular(self):
        real_part = self.A * (np.cos(np.radians(self.P)))
        img_part = self.A * (np.sin(np.radians(self.P)))

        return "The rectangular form of {} < {} degrees is [{:.2f} + {:.2f}j]".format(self.A, self.P, real_part, img_part)

while True:
    try:
        abs_value = float(input("Enter the absolute value: "))
        break
    except:
        print('absolute value must be an integer or a float ...')
    
while True:
    try:
        phase_angle = float(input("Enter the phase angle: "))
        break
    except:
        print('phase angle must be an integer or a float ...')

rectangular_form = Complex_Number(abs_value, phase_angle)
print(rectangular_form.Phasor_to_Rectangular())