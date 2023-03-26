import pickle
import tensorflow as tf

def pred(input_array):
    # load minmax scaler
    with open('model/minmax_scaler.pkl', 'rb') as f:
        loaded_scaler = pickle.load(f)
    
    # load model
    model = tf.keras.models.load_model("model/boston_nn_model.h5")

    # minmaxscaler
    input_array = loaded_scaler.transform(input_array)

    return model.predict(input_array)[0][0]