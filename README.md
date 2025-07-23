# Test Automation Framework for RF Signal Capture

This project implements a complete test automation framework using Python to capture analog signal data from embedded systems over UART and validate signal integrity by detecting amplitude thresholds and spectral peaks near 180 kHz. The framework is designed to replace manual probing or oscilloscope-based debugging with a repeatable, script-driven validation process.

---

## Aim

To develop a signal capture and validation system that:
- Automatically triggers waveform capture over UART from embedded hardware when a signal crosses a defined amplitude threshold.
- Detects signal peaks and classifies frequency behavior using Python-based analysis.
- Logs all results to CSV and generates annotated waveform plots.
- Validates signals in the 180 kHz range for systems using low-frequency capacitive communication.

This system was used during validation of a virtual capacitance communication system between two embedded boards.

---

## Tech Stack

- **Python 3.9+**
- **PySerial**: For UART data capture from microcontrollers
- **NumPy & SciPy**: For data processing and peak detection
- **Matplotlib**: For waveform and peak visualization
- **CSV module**: For structured signal logging and traceability

---

## Skills Demonstrated

- Serial communication and UART buffering using `pyserial`
- Threshold-triggered waveform capture
- Real-time signal analysis and peak identification
- Data logging and output visualization
- Modular CLI-based test automation scripting
- Replacement of oscilloscope validation with headless code

This framework significantly reduced hardware debug time and enabled consistent, automated validation across multiple test runs.

---

## Project Workflow

1. The microcontroller transmits waveform values over UART.
2. The Python script listens to the UART port.
3. When signal amplitude exceeds a defined threshold (e.g., 0.5), it begins capturing a fixed number of samples.
4. The captured data is:
   - Saved to a CSV file
   - Processed using `scipy.signal.find_peaks`
   - Annotated on a waveform plot using `matplotlib`
5. Console output summarizes detected peak indices, amplitudes, and duration.

This pipeline was validated on 180 kHz sine waves transmitted through virtual air capacitance using GPIO DAC output, with the receiver reading noise-affected analog waveforms.

---
