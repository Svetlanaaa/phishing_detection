import tensorflow as tf
from sklearn.model_selection import train_test_split
import tensorflowjs as tfjs
import numpy as np


def create_output_data(y):
	data = []
	for i, j in enumerate(y):
		if j < 0:
			data.append([0, 1])
		else:
			data.append([1, 0])
	return np.array(data)


# подготовка данных
data = np.loadtxt("TrainingData.txt", delimiter=",")
x = data[:, :-1]
y = create_output_data(data[:, -1])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# построение модели
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(35, input_dim=16, kernel_initializer='uniform', activation='relu'))
model.add(tf.keras.layers.Dropout(0.3))
model.add(tf.keras.layers.Dense(10, kernel_initializer='uniform', activation='relu'))
model.add(tf.keras.layers.Dropout(0.2))
model.add(tf.keras.layers.Dense(2, kernel_initializer='uniform', activation='sigmoid'))

# сборка модели
lr = 0.095
decay = lr/250
sgd = tf.keras.optimizers.SGD(lr=lr, momentum=0.9, decay=decay, nesterov=True)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

# обучение
history = model.fit(x_train, y_train, validation_data=(x_test, y_test), nb_epoch=100, batch_size=500, shuffle=True, verbose=2)

# сохранение
tfjs.converters.save_keras_model(model, "/home/user/PycharmProjects/phishingDetection")
