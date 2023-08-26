# You can use this program to draw Fourier transform diagrams for a signal.
# In the output for you, two functions will be displayed, which include:
#                  1. the time graph of the signal 
#                  2. its Fourier transformation.


import numpy as np


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
        