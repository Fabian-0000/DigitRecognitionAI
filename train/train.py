import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Image settings
IMG_SIZE = 28
IMG_CHANNELS = 1
BATCH_SIZE = 32

# Load dataset from directory
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "train",
    image_size=(IMG_SIZE, IMG_SIZE),
    batch_size=BATCH_SIZE,
    color_mode="grayscale",
    label_mode="int"
)

# Normalize pixel values (0-255 → 0-1)
normalization_layer = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))

# Build CNN model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, IMG_CHANNELS)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 classes (0-9)
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train
history = model.fit(train_ds, epochs=100)

# Save model
model.save("digit_model.keras")