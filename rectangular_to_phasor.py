import numpy as np

class Complex_Number:

    def __init__(self, real_part=0, img_part=0):
        self.R = real_part
        self.I = img_part

    def Rectangular_to_Phasor(self):
        a = complex(self.R, self.I)
        b = abs(a)
        c =  np.degrees(np.arctan(self.I / self.R))

        return "The phasor form of {} is {:.2f} < {:.2f} degrees".format(a, b, c)

while True:
    try:
        real_part = float(input("Enter the real part: "))
        break
    except:
        print('real part must be an integer or a float ...')

while True:
    try:
        img_part = float(input("Enter the imaginary part: "))
        break
    except:
        print('imaginary part must be an integer or a float ...')

polar_form = Complex_Number(real_part, img_part)
print(polar_form.Rectangular_to_Phasor())