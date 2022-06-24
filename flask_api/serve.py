# from pyexpat import model
from flask import Flask, request
# import hyper as hp
# import io
# from PIL import Image
# import utils
# import numpy as np
# import json

# Khởi tạo model
global model
model = None

app = Flask(__name__)

# Test
@app.route("/")
@app.route("/home", methods=['GET'])
def _hello_world():
    return "API for Classification"

# # Predict
# @app.route("/predict", methods=['POST'])
# def _predict():
#     data = {"success": False}
#     if request.files.get("image"):
#         # Lấy ảnh
#         img = request.files["image"].read()
#         # Xử lý ảnh
#         img = Image.open(io.BytesIO(img))
#         img = utils._preprocess_image(img, (hp.IMG_WIDTH, hp.IMG_HEIGHT))
#         # Predict
#         result = model.predict(img)[0]
#         print(result)
#         # Lấy 10 giá trị lớn nhất đầu tiên
#         argmax_k = np.argsort(result)[::-1][:10] 
#         classes = [hp.IDX_TO_LABEL[idx] for idx in list(argmax_k)]
#         classes_prob = [result[idx] for idx in list(argmax_k)]
#         # Output
#         data['result'] = dict(zip(classes, classes_prob))
#         data["success"] = True
#     return json.dumps(data, ensure_ascii=False, cls=utils.NumpyEncoder)

if __name__=="__main__":
    # model = utils._load_model()
    print("App run!")
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
    

# create env python = 3.7
# pip install tensorflow=2.6
# flask Pillow
# pip install --upgrade "protobuf<=3.20.1"
# pip install keras==2.6
# tfcpu
# Chuyển sang document