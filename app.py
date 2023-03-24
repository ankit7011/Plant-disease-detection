from flask import Flask, redirect, url_for, request, render_template
import pickle
from werkzeug.utils import secure_filename
import os
from joblib import load

UPLOAD_FOLDER = 'D:\Coding\Jupyter_Python\Plant disease detection'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



def ValuePredictor(input):
    # to_predict = np.array(to_predict_list).reshape(1, 12)
    # loaded_model = pickle.load(open("model.bin", "rb"))
    # result = loaded_model.predict(input)
    # return result[0]
    # import joblib
    text = ["Virat Kohli, AB de Villiers set to auction their 'Green Day' kits from 2016 IPL match to raise funds"]
    pipeline = load("text_classification.joblib")


# f_pickle = open("trained_model.pkl", 'rb')
# # model = pickle.dumps(f_pickle)
# model = pickle.load(open('trained_model.pkl', 'rb'))
if __name__ == "__main__":
    print("welcome to plant")
    ValuePredictor("")


@app.route('/')
def show_predict_stock_form():
    return render_template('plant.html')

@app.route('/success/<name>')
def success(diseaseName):
	return 'welcome %s' % diseaseName

@app.route('/submitImage', methods=['POST', 'GET'])
def submit_image():
    ValuePredictor("")
    # with open('./model.bin', 'rb') as f_in:
    #     model = pickle.load(f_in)
    # with open('trained_model.pkl', 'rb') as f:
    # 	model = pickle.load(f)
    if request.method == 'POST':
        print( request.form['plantName'])
        print(request.files['plantImage'])

        if 'plantImage' not in request.files:
            return 'there is no plantImage in form!'
        plantImage = request.files['plantImage']
        path = os.path.join(app.config['UPLOAD_FOLDER'], plantImage.filename)
        plantImage.save(path)
        data=model(path)
        return data

    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''
   
if __name__ == '__main__':
	app.run(debug=True)
