from ghost_env import INFURA_KEY, VAULT_ADDRESS
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import warnings
warnings.filterwarnings('ignore', category=UserWarning, module='keras')

import tensorflow as tf
import numpy as np

class TensorFlowModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        # Now 9 features: open, high, low, close, volume, sentiment, risk_grade, sma_14, rsi_14
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(shape=(9,)),   # <- updated for 9 features!
            tf.keras.layers.Dense(24, activation='relu'),
            tf.keras.layers.Dense(12, activation='relu'),
            tf.keras.layers.Dense(3, activation='softmax')  # buy/hold/sell
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def predict(self, features):
        """
        features: array-like of shape (9,) [open, high, low, close, volume, sentiment, risk_grade, sma_14, rsi_14]
        Returns: 'buy', 'hold', or 'sell'
        """
        features = np.array(features).reshape(1, -1)
        prediction = self.model.predict(features, verbose=0)
        label = np.argmax(prediction)
        return ['buy', 'hold', 'sell'][label]

    def train(self, X, y, epochs=15, batch_size=8):
        self.model.fit(X, y, epochs=epochs, batch_size=batch_size)

    def save_weights(self, path="tf_model_weights.h5"):
        self.model.save_weights(path)

    def load_weights(self, path="tf_model_weights.h5"):
        self.model.load_weights(path)

def log_event():ef mutate(*args, **kwargs): print('[ghost_empire] dummy mutate called')
def drop_files_to_bridge():