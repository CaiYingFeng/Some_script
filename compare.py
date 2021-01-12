from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
#load result

gt_db_path ='/media/autolab/disk_4T/cyf/SG_PR/eva/00_gt_db.npy'
pred_db_path = '/media/autolab/disk_4T/cyf/SG_PR/eva/00_DL_db.npy'
gt_db=np.load(gt_db_path)
pred_db=np.load(pred_db_path)


pred_db = np.array(pred_db)
gt_db = np.array(gt_db)
#####ROC
fpr, tpr, roc_thresholds = metrics.roc_curve(gt_db, pred_db)
roc_auc = metrics.auc(fpr, tpr)
print("fpr: ", fpr)
print("tpr: ", tpr)
print("thresholds: ", roc_thresholds)
print("roc_auc: ", roc_auc)
plt.figure(0)
lw = 2
plt.plot(fpr, tpr, color='darkorange',
            lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('DL ROC Curve')
plt.legend(loc="lower right")
plt.show()