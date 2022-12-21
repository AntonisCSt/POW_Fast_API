from fastapi import FastAPI
import uvicorn
import pickle
import numpy as np

# load the model from disk
filename = filename = './model/bcancer_model_v1.pkl'
loaded_model = pickle.load(open(filename, 'rb'))

app = FastAPI(debug=True)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/predict")
async def predict(input_data: dict):
    """
    make breast cancer prediction with random forst essemble model
    """
    results = np.array(list(input_data.values())).reshape(1, -1)[0]
    return results



if __name__ == '__main__':
    uvicorn.run(app)