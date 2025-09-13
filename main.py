Last login: Sun Sep 14 01:29:25 on ttys000
(base) dhirajrajiitj@Dhirajs-MacBook-Air ~ % cd Downloads 
(base) dhirajrajiitj@Dhirajs-MacBook-Air Downloads % cd Ml_ops 
(base) dhirajrajiitj@Dhirajs-MacBook-Air Ml_ops % ls
DigitClassification	ml_ops_day3		testing_day3
DigitClassification1	new_digit
(base) dhirajrajiitj@Dhirajs-MacBook-Air Ml_ops % cd ml_ops_day3 
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % ls
best_model.joblib			requirements.txt
comparison.py				rf_model.joblib
decision_tree_confusion_matrix.png	sample_training_digits.png
dt_model.joblib				svm_confusion_matrix.png
plot_digits_classification.py		svm_model.joblib
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano testing1.py
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % python testing1.py 
Classification report for SVM:
              precision    recall  f1-score   support

           0       1.00      0.99      0.99        88
           1       0.99      0.97      0.98        91
           2       0.99      0.99      0.99        86
           3       0.98      0.87      0.92        91
           4       0.99      0.96      0.97        92
           5       0.95      0.97      0.96        91
           6       0.99      0.99      0.99        91
           7       0.96      0.99      0.97        89
           8       0.94      1.00      0.97        88
           9       0.93      0.98      0.95        92

    accuracy                           0.97       899
   macro avg       0.97      0.97      0.97       899
weighted avg       0.97      0.97      0.97       899


Classification report for Decision Tree:
              precision    recall  f1-score   support

           0       0.92      0.90      0.91        88
           1       0.85      0.60      0.71        91
           2       0.88      0.70      0.78        86
           3       0.69      0.74      0.71        91
           4       0.91      0.79      0.85        92
           5       0.59      0.74      0.65        91
           6       0.81      0.95      0.87        91
           7       0.89      0.75      0.82        89
           8       0.59      0.69      0.64        88
           9       0.65      0.74      0.69        92

    accuracy                           0.76       899
   macro avg       0.78      0.76      0.76       899
weighted avg       0.78      0.76      0.76       899


✅ Models saved as svm_model.joblib and dt_model.joblib
✅ Models loaded successfully!
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano .gitignore
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % ls
best_model.joblib			rf_model.joblib
comparison.py				sample_training_digits.png
decision_tree_confusion_matrix.png	svm_confusion_matrix.png
dt_model.joblib				svm_model.joblib
plot_digits_classification.py		testing1.py
requirements.txt
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % rm rf_model.joblib 
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % ls
best_model.joblib			requirements.txt
comparison.py				sample_training_digits.png
decision_tree_confusion_matrix.png	svm_confusion_matrix.png
dt_model.joblib				svm_model.joblib
plot_digits_classification.py		testing1.py
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % rm comparison.py 
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % ls
best_model.joblib			sample_training_digits.png
decision_tree_confusion_matrix.png	svm_confusion_matrix.png
dt_model.joblib				svm_model.joblib
plot_digits_classification.py		testing1.py
requirements.txt
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano .gitignore
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git add .      
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git status
On branch actionbranch
Your branch is up to date with 'origin/actionbranch'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	new file:   .gitignore
	new file:   best_model.joblib
	new file:   decision_tree_confusion_matrix.png
	modified:   plot_digits_classification.py
	new file:   sample_training_digits.png
	new file:   svm_confusion_matrix.png

(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git commit -m "created .gitignore"
[actionbranch d6c9d9d] created .gitignore
 Committer: Dhiraj Raj <dhirajrajiitj@Dhirajs-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6 files changed, 14 insertions(+), 3 deletions(-)
 create mode 100644 .gitignore
 create mode 100644 best_model.joblib
 create mode 100644 decision_tree_confusion_matrix.png
 create mode 100644 sample_training_digits.png
 create mode 100644 svm_confusion_matrix.png
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git push
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (7/7), done.
Writing objects: 100% (8/8), 129.16 KiB | 413.00 KiB/s, done.
Total 8 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To github.com:DhirajRajIitJodhpur/ml_ops_day3.git
   3d6f7bf..d6c9d9d  actionbranch -> actionbranch
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano testing1.py 
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano .gitignore
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git add .
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % git status
On branch actionbranch
Your branch is up to date with 'origin/actionbranch'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   .gitignore
	new file:   testing1.py

(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % ls
best_model.joblib			sample_training_digits.png
decision_tree_confusion_matrix.png	svm_confusion_matrix.png
dt_model.joblib				svm_model.joblib
plot_digits_classification.py		testing1.py
requirements.txt
(base) dhirajrajiitj@Dhirajs-MacBook-Air ml_ops_day3 % nano testing1.py 

  UW PICO 5.09                       File: testing1.py                          

"""
================================
Recognizing hand-written digits
Using SVM and Decision Tree
================================
"""

# Standard imports
import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm, tree
from sklearn.model_selection import train_test_split
from joblib import dump, load

###############################################################################
# Digits dataset
digits = datasets.load_digits()

# Visualize first 4 training images
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))

^G Get Help  ^O WriteOut  ^R Read File ^Y Prev Pg   ^K Cut Text  ^C Cur Pos   
^X Exit      ^J Justify   ^W Where is  ^V Next Pg   ^U UnCut Text^T To Spell  

