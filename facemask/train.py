from keras.preprocessing.image import ImageDataGenerator
from json import decoder
import numpy as np
import keras
import keras.backend as k
from keras.layers import Conv2D, MaxPooling2D, SpatialDropout2D, Flatten, Dropout, Dense
from keras.models import Sequential, load_model
from keras.optimizers import Adam
from keras.preprocessing import image


# BUILDING MODEL TO CLASSIFY BETWEEN MASK AND NO MASK

model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(100, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy',
              metrics=['accuracy'])

train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
    'train',
    target_size=(150, 150),
    batch_size=16,
    class_mode='binary')

test_set = test_datagen.flow_from_directory(
    'test',
    target_size=(150, 150),
    batch_size=16,
    class_mode='binary')

model_saved = model.fit_generator(
    training_set,
    epochs=10,
    validation_data=test_set,

)

model.save('mymodel.h5', model_saved)
