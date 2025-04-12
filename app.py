# from flask import Flask, render_template, request
# import pandas as pd
# import pickle

# app = Flask(__name__)

# # Load model and columns
# model = pickle.load(open("model (1).pkl", "rb"))
# model_columns = pickle.load(open("model_columns (1).pkl", "rb"))



# @app.route('/predict', methods=["POST"])
# def predict():
#     # Collect form data
#     input_data = {
#         "Food": request.form['food'],
#         "Color": request.form['color'],
#         "Smell": request.form['smell'],
#         "Texture": request.form['texture'],
#         "Foam": request.form['foam'],
#         "Taste": request.form['taste']
#     }

#     df = pd.DataFrame([input_data])
#     df_encoded = pd.get_dummies(df)

#     # Add missing columns
#     for col in model_columns:
#         if col not in df_encoded.columns:
#             df_encoded[col] = 0

#     df_encoded = df_encoded[model_columns]
#     prediction = model.predict(df_encoded)[0]
#     if prediction.lower() == "yes":
#         message = "⚠️ Adulteration Detected! Avoid Consumption."
#     else:
#         message = "✅ Pure Product! Safe to Consume. Keep enjoying quality food 😊"

#     return render_template("result.html", message=message)

   

# if __name__ == "__main__":
#     app.run(debug=True)
# from flask import Flask, render_template, request
# import pandas as pd
# import pickle

# app = Flask(__name__)

# # Load model and columns
# model = pickle.load(open("model (1).pkl", "rb"))
# model_columns = pickle.load(open("model_columns (1).pkl", "rb"))

# @app.route('/')
# def home():
#     return render_template("Home.html")

# @app.route('/predict', methods=["POST"])
# def predict():
#     input_data = {
#         "Food": request.form['food'],
#         "Color": request.form['color'],
#         "Smell": request.form['smell'],
#         "Texture": request.form['texture'],
#         "Foam": request.form['foam'],
#         "Taste": request.form['taste']
#     }

#     df = pd.DataFrame([input_data])
#     df_encoded = pd.get_dummies(df)

#     for col in model_columns:
#         if col not in df_encoded.columns:
#             df_encoded[col] = 0

#     df_encoded = df_encoded[model_columns]
#     prediction = model.predict(df_encoded)[0]

#     # Customize message and styling class
#     if prediction.lower() == "yes":
#         message = "⚠️ Adulteration Detected! Avoid Consumption."
#         result_class = "result-box red"
#     else:
#         message = "✅ Pure Product! Safe to Consume. Keep enjoying quality food 😊"
#         result_class = "result-box green"

#     return render_template("result.html", message=message, result_class=result_class)

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and columns
model = pickle.load(open("model (1).pkl", "rb"))
model_columns = pickle.load(open("model_columns (1).pkl", "rb"))

@app.route('/')
def home():
   
    return render_template("Home.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/review')
def review():
    return render_template("review.html")

@app.route('/input')
def input_page():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    # Collect form data
    input_data = {
        "Food": request.form['food'],
        "Color": request.form['color'],
        "Odour": request.form['smell'],
        "Texture": request.form['texture'],
        "Foam": request.form['foam'],
        "Taste": request.form['taste']
    }

    df = pd.DataFrame([input_data])
    df_encoded = pd.get_dummies(df)

    # Add missing columns
    for col in model_columns:
        if col not in df_encoded.columns:
            df_encoded[col] = 0

    df_encoded = df_encoded[model_columns]
    prediction = model.predict(df_encoded)[0]
    if prediction.lower() == "yes":
        message = "⚠️ Adulteration Detected! Avoid Consumption."
    else:
        message = "✅ Pure Product! Safe to Consume. Keep enjoying quality food 😊"

    return render_template("result.html", message=message)

   

# if __name__ == "__main__":
#     app.run(debug=True)
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
