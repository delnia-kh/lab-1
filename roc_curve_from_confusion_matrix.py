import matplotlib.pyplot as plt
import numpy as np

# Define FPR and TPR based on the confusion matrix data
fpr_train = [0, 1/(1 + 286543), 1]  # 0 to FP rate up to 1
tpr_train = [0, 183/(183 + 1), 1]   # 0 to TP rate up to 1

fpr_test = [0, 0/(0 + 2865446), 1]  # 0 because FP=0
tpr_test = [0, 184/(184 + 1), 1]

plt.figure(figsize=(8,6))
plt.plot(fpr_train, tpr_train, marker='o', label='Training ROC curve')
plt.plot(fpr_test, tpr_test, marker='o', label='Testing ROC curve')
plt.plot([0,1], [0,1], 'k--', label='Random Guess')

plt.xlabel('False Positive Rate (FPR)')
plt.ylabel('True Positive Rate (TPR)')
plt.title('ROC Curve from Confusion Matrices')
plt.legend(loc='lower right')
plt.grid(True)
plt.show()
