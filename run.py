from rntn import RNTNModel

vec_dims = [20, 30, 40]
lambdas = [1e-4, 1e-3, 1e-2]
batch_sizes = [32, 64, 128]
lrs = [0.1, 0.01, 0.001]

for l in lambdas:
    for batch_size in batch_sizes:
        for lr in lrs:
            for vec_dim in vec_dims:
                model = RNTNModel(vocab_file='resources/vocabulary.csv', wvec_dim=vec_dim, num_classes=5)
                res = model.train(train_file='resources/trees/train.txt', step_size=lr, lamda=l, epsilon=1e-8,
                            num_epoch=10, batch_size=batch_size)
                model.save('{}_{}_{}_{}.pkl'.format(vec_dim, lr, l, batch_size))
                str1 = '{}_{}_{}_{}.txt'.format(vec_dim, lr, l, batch_size)
                with open(str1, 'w') as f:
                    f.write(res)

# model.load('save1.pkl')
#
#
# model.test(test_file='resources/trees/dev.txt')
#
# model.test(test_file='resources/trees/test.txt')
