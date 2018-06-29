from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
import numpy as np
import random

'''
def foo(x, y):
    i = 0
    s = x
    while (i<y):
        i+=1
        s = s + i
    return s
'''

def foo(x,y):
    return x+y

max = 0
x_train = []
y_train = []
random.seed(1)
for i in range(10000):
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    X = [x,y]
    x_train.append(X)
    if (max<foo(x,y)):
        max = foo(x,y)
    y_train.append(foo(x, y))

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = x_train.astype('float') / float(max)
y_train = y_train.astype('float') / float(max)

x_test = []
y_test = []
for i in range(100):
    x = random.randint(0, 999)
    y = random.randint(0, 999)
    X = [x,y]
    x_test.append(X)
    y_test.append(foo(x, y))

x_test, y_test = np.array(x_test), np.array(y_test)
x_test = x_test.astype('float') / float(max)
y_test = y_test.astype('float') / float(max)

x_train = x_train.reshape(10000,2,1)
x_test = x_test.reshape(100,2,1)

model = Sequential()
model.add(LSTM(100, input_shape=(2, 1), return_sequences=True))
model.add(LSTM(50))
#model.add(Dense(20, input_dim=2))
#model.add(Dense(10))
model.add(Dense(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='rmsprop' , metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10, batch_size=32)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=32)

print('loss_and_metrics : ' + str(loss_and_metrics))

for i in range(10):
    x = random.randint(0,999)
    y = random.randint(0,999)
    print(str(x) + "+" + str(y) + "=", end=' ')
    z = np.array([x/max, y/max]).reshape(1,2,1)
    print(int(model.predict(z) * max), end= ' vs ')
    print(foo(x, y))


