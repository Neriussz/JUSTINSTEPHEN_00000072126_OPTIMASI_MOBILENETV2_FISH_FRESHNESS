"""
MobileNetV2 Model for Fish Freshness Classification

Author : Justin Stephen
NIM    : 00000072126

Research:
Optimasi MobileNetV2 Menggunakan Strategi Fine-Tuning
untuk Klasifikasi Kesegaran Ikan Berbasis Citra Digital
"""

from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


def build_transfer_learning_model(
    input_shape=(224, 224, 3),
    num_classes=3
):
    """
    Transfer Learning Model
    """

    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=input_shape
    )

    # Freeze backbone
    base_model.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)

    outputs = Dense(
        num_classes,
        activation='softmax'
    )(x)

    model = Model(
        inputs=base_model.input,
        outputs=outputs
    )

    model.compile(
        optimizer=Adam(learning_rate=3e-4),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


def build_fine_tuning_model(
    model,
    unfreeze_layers=30,
    learning_rate=1e-5
):
    """
    Fine-Tuning Stage
    """

    model.trainable = True

    for layer in model.layers[:-unfreeze_layers]:
        layer.trainable = False

    model.compile(
        optimizer=Adam(
            learning_rate=learning_rate
        ),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model


if __name__ == "__main__":

    # Transfer Learning
    model = build_transfer_learning_model()

    print("\nTransfer Learning Model")
    model.summary()

    # Fine-Tuning
    model = build_fine_tuning_model(model)

    print("\nFine-Tuning Model")
    model.summary()
