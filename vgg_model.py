from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten, Dropout
from keras.applications.vgg16 import VGG16

def get_model():
    #grab the pretrained VGG16 model
    vgg16 = VGG16(weights='imagenet', include_top=False, input_shape=(200, 200, 3))

    #add all layers except the last dense layer to our model
    model = Sequential()
    for layer in vgg16.layers[:-1]:
        model.add(layer)

    #prevent weights from be trainable
    for layer in model.layers[:-1]:
        layer.trainable = False

    #add a final dense layer that will represent each age group
    model.add(Flatten())
    model.add(Dropout(0.5))
    model.add(Dense(100, activation='softmax'))
    model.summary()

    return model