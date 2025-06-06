import matplotlib.pyplot as plt
import numpy as np

# Logarithmic thresholds values
thresholds = np.array([
    1e-19, 1e-18, 1e-17, 1e-16, 1e-15, 1e-14, 1e-13, 1e-12, 1e-11,
    1e-10, 1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1, 1e0
])

# Hypothetical accuracy values close to your data
accuracy = np.array([
    0.995, 0.996, 0.997, 0.998, 0.9985, 0.999, 0.9993, 0.9995, 0.9996,
    0.9997, 0.9998, 0.9999, 0.9999, 0.99995, 0.99985, 0.9997, 0.995, 0.95, 0.7, 0.65
])

# Hypothetical MCC values close to your data
mcc = np.array([
    0.98, 0.985, 0.987, 0.989, 0.99, 0.992, 0.993, 0.994, 0.995,
    0.996, 0.997, 0.998, 0.999, 0.9995, 0.995, 0.98, 0.9, 0.6, 0.1, 0.05
])

plt.figure(figsize=(10,6))
plt.plot(thresholds, accuracy, marker='o', label='Accuracy')
plt.plot(thresholds, mcc, marker='o', label='MCC')

plt.xscale('log')
plt.xlabel('Threshold (E-value)')
plt.ylabel('Score')
plt.title('Accuracy and MCC over Different Thresholds')
plt.axvline(x=1e-6, color='red', linestyle='--', label='Chosen Threshold = 1e-6')

plt.legend()
plt.grid(True)
plt.show()
