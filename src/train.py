import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras

print(f"Using tensorflow version: {tf.__version__}")

# Get the datasets
data = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = data.load_data()

# The class names for each of fashion category
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# Clean the data of the train, and test sets
train_images = train_images / 255.0

test_images = test_images / 255.0

# Visualize the clothing category.
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# Create the keras model.
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation="softmax")
])

# Compile the model
model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])

# Fit and train the model.
model.fit(train_images, train_labels, epochs=15)

# Test the model
test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print(f"Test Accuracy: {test_acc}\nTest loss: {test_loss}")

# Save the model
model.save("model.h5")
