from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report

with open("train_raw_phrases", "r") as f1, open("test_raw_phrases", "r") as f2, \
        open("train_raw_labels", "r") as f3, open("test_raw_labels", "r") as f4:
    X_train_phrases = f1.readlines()
    X_test_phrases = f2.readlines()
    y_train_lines = f3.readlines()
    y_test_lines = f4.readlines()

y_train = []
for train_line in y_train_lines:
    y_train.append(int(train_line))
y_test = []
for test_line in y_test_lines:
    y_test.append(int(test_line))

vec = CountVectorizer()
X_train = vec.fit_transform(X_train_phrases)
X_test = vec.transform(X_test_phrases)

# pca = PCA(100)
# pca.fit_transform(X_train.toarray())
# pca.transform(X_test.toarray())

lsvc = LinearSVC(max_iter=10000)

# 进行模型训练
lsvc.fit(X_train, y_train)
# 预测
y_predict = lsvc.predict(X_test)

# 评估
# 使用模型自带的评估函数进行准确性测评
print('The Accuracy of Linear SVC is', lsvc.score(X_test, y_test))

# 使用classification_report模块进行分析
print(classification_report(y_test,y_predict, target_names=['1', '2', '3', '4', '5']))

with open("svm_result.txt", "w") as re:
    re.write('The Accuracy of Linear SVC is' + str(lsvc.score(X_test, y_test)) + '\n')
    re.write(str(classification_report(y_test,y_predict, target_names=['1', '2', '3', '4', '5'])))