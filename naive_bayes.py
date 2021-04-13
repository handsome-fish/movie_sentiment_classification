
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
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

# 初始化NB模型
mnb = MultinomialNB()

# 利用训练数据对模型参数进行估计
mnb.fit(X_train, y_train)
# 对测试样本进行类别预测
y_predict = mnb.predict(X_test)

# 评估
print('The accuracy of Naive Bayes Classifier is', mnb.score(X_test, y_test))
print(classification_report(y_test, y_predict, target_names=['1', '2', '3', '4', '5']))
