import os
import argparse
import matplotlib.pyplot as plt
from datetime import datetime

from src.signal_capture import capture_uart
from src.peak_detector import detect_peaks
from utils.logger import save_to_csv

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=str, required=True, help='UART port (e.g., /dev/ttyUSB0)')
    parser.add_argument('--threshold', type=float, default=0.5, help='Signal threshold to trigger capture')
    args = parser.parse_args()

    signal_data = capture_uart(port=args.port, threshold=args.threshold)
    peaks = detect_peaks(signal_data, min_height=args.threshold)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    csv_path = f"data/signal_{timestamp}.csv"
    plot_path = f"plots/spectrum_{timestamp}.png"

    save_to_csv(signal_data, csv_path)

    plt.figure(figsize=(12, 6))
    plt.plot(signal_data, label="Signal")
    plt.plot(peaks, [signal_data[p] for p in peaks], "rx", label="Peaks")
    plt.title("Captured RF Signal with Peaks")
    plt.xlabel("Sample Index")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(plot_path)
    print(f"[INFO] Signal saved to {csv_path}")
    print(f"[INFO] Plot saved to {plot_path}")

if __name__ == "__main__":
    main()
