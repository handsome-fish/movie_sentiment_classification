from rntn import RNTNModel

model = RNTNModel(vocab_file='dataset/resources/vocabulary.csv', wvec_dim=30, num_classes=5)
model.load('save.pkl')

model.test(test_file='dataset/resources/trees/test.txt')
