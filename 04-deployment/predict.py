import pickle
import mlflow
from mlflow.tracking import MlflowClient

from flask import Flask, request, jsonify

RUN_ID = '9099cf72ff2d41ec82f98bb5a9f7d95e'
MLFLOW_TRACKING_URI="http://127.0.0.1:5000"

mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)
# mlflow.set_experiment("green-taxi-duration")
# client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)

logged_model = f'runs:/{RUN_ID}/models'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

# path = client.download_artifacts(run_id=RUN_ID, path='dict_vectorizer.bin')
# print(f'downloading the dict vectorizer to {path}')
# with open(path, 'rb') as f_out:
    # dv = pickle.load(f_out)

# with open('lin_reg.bin', 'rb') as f_in:
    # (dv, model2) = pickle.load(f_in)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    preds = model.predict(features)
    # X = dv.transform(features)
    # preds = model.predict(X)
    return preds[0]

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    print("GOT JSON")

    features = prepare_features(ride)
    pred = predict(features)
    
    result = {
        'duration': pred,
        'model_version': RUN_ID
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)