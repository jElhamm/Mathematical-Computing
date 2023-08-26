# You can use this program to draw Fourier transform diagrams for a signal.
# In the output for you, two functions will be displayed, which include:
#                  1. the time graph of the signal 
#                  2. its Fourier transformation.


import numpy as np
import matplotlib.pyplot as plt

class FourierTransform:
    def __init__(self, inputSignal, sampling_frequency):
        if isinstance(inputSignal, list):
            self.signal = np.array(inputSignal)
        elif isinstance(inputSignal, np.ndarray):
            self.signal = inputSignal
        else:
            raise ValueError("Invalid input signal. It should be a list or a numpy array.")

        self.sampling_frequency = sampling_frequency

    def apply_transform(self):
        # Apply the Fourier transform to the input signal
        self.fourier_transform = np.fft.fft(self.signal)
        self.frequency_bins = np.fft.fftfreq(len(self.signal), 1/self.sampling_frequency)

    # plot the input signal
    def plot_signal(self):
        time_axis = np.arange(0, len(self.signal)) * (1/self.sampling_frequency)         # Create a time axis based on the sampling frequency
        plt.subplot(2, 1, 1)
        plt.plot(time_axis, self.signal)
        plt.title('Input Signal')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')

    # plot the Fourier transform 
    def plot_transform(self):
        plt.subplot(2, 1, 2)
        plt.stem(self.frequency_bins, np.abs(self.fourier_transform))
        plt.title('Fourier Transform')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')

    def plot(self):
        self.apply_transform()
        plt.figure(figsize=(10, 8))
        self.plot_signal()
        self.plot_transform()
        plt.tight_layout()
        plt.show() 


# This part of the code is written as an example to show the output of the code.
# According to your needs, you can change or delete this part.

def  banner():
    print("""
        
#####################################################################################
#                              ***   Welcome   ***                                  #
#                                                                                   #             
#     You can use this program to draw Fourier transform diagrams for a signal.     #
#      In the output for you, two functions will be displayed, which include:       #
#                       1. the time graph of the signal                             #
#                       2. its Fourier transformation.                              #
#                                                                                   #    
#####################################################################################
    """)           
    
def main():
    inputSignal = input("==> Enter the input signal as a comma-separated list of numbers: ").split(",")
    sampling_frequency = float(input("==> Enter the sampling frequency: "))
    inputSignal = [float(num) for num in inputSignal]
    fft = FourierTransform(inputSignal, sampling_frequency)
    fft.plot()
    print("\n*************************************************")
    print("*        (: The graphs are displayed. :)        *")
    print("*************************************************\n")

if __name__ == "__main__":
    main()

# An example of how to use the program is shown.  