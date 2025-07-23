import numpy as np
from scipy.signal import find_peaks

def detect_peaks(signal_data, min_height=0.5):
    peaks, _ = find_peaks(signal_data, height=min_height)
    return peaks
