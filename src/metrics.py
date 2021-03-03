import tensorflow.keras.backend as tkb


def _true_positives(y_true, y_pred):
    return tkb.sum(tkb.round(tkb.clip(y_true * y_pred, 0, 1)))


def _predicted_positives(y_pred):
    return tkb.sum(tkb.round(tkb.clip(y_pred, 0, 1)))


def _possible_positives(y_true):
    return tkb.sum(tkb.round(tkb.clip(y_true, 0, 1)))


def precision(y_true, y_pred):
    return _true_positives(y_true, y_pred) / (_predicted_positives(y_pred) + tkb.epsilon())


def recall(y_true, y_pred):
    return _true_positives(y_true, y_pred) / (_possible_positives(y_true) + tkb.epsilon())


def f1(y_true, y_pred):
    f1_val = 2 * (precision(y_true, y_pred) * recall(y_true, y_pred)) \
             / (precision(y_true, y_pred) + recall(y_true, y_pred) + tkb.epsilon())
    return f1_val
