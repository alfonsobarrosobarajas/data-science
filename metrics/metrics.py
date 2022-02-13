from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
y_true = [1, 1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 1, 0, 0]
TN, FP, FN, TP = confusion_matrix(y_true, y_pred).ravel()


Accuracy = (TP + TN) / (TP + TN + FP + FN)


accuracy_score(y_true, y_pred)


accuracy_score(y_true, y_pred)
recall = TP / (TP + FN)
precision = TP / (TP + FP)


F1 = 2 * ((recall * precision)/(recall + precision))

f1_score(y_true, y_pred)

y_true = [1, 1, 1, 0, 1, 0]
y_pred = [1, 1, 0, 1, 1, 0]
fpr, tpr, thresholds = roc_curve(y_true, y_pred)
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         label='ROC curve')
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
