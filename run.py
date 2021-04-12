from rntn import RNTNModel


model = RNTNModel(vocab_file='resources/vocabulary.csv', wvec_dim=30, num_classes=5)


model.train(train_file='resources/trees/train.txt', step_size=0.01, lamda=0.001, epsilon=1e-8, num_epoch=10, batch_size=200)


model.save('results/save1.pkl')

model.load('results/save1.pkl')


model.test(test_file='resources/trees/dev.txt')

model.test(test_file='resources/trees/test.txt')
