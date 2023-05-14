from flask import Flask, request, render_template, session
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', file_uploaded=False)


def analyze_file_1(filename):
    with open('naive_bayes_model.pkl', 'rb') as f:
        model = pickle.load(f)
    # Make predictions using the loaded model
    input_data = [filename]  # Input data for prediction
    predictions = model.predict(input_data)
    # Perform further processing or use the predictions as desired
    return predictions


@app.route('/', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return render_template('index.html', file_uploaded=False)

    uploaded_file = request.files['file']
    if uploaded_file.filename == '':
        return render_template('index.html', file_uploaded=False)

    uploaded_file.save(uploaded_file.filename)
    algorithm = request.form.get('algorithm', 1)

    result = None  # default value

    if algorithm == '1':
        result = analyze_file_1(uploaded_file.filename)

    if result is not None:
        result = result

    return render_template('index.html', result=result, file_uploaded=True)


if __name__ == '__main__':
    app.run(debug=True)
