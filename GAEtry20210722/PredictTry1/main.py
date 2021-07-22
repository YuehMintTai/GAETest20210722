# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_flex_quickstart]
import logging
from flask import Flask
from flask import  render_template,request
import pandas as pd
import tensorflow as tf
app=Flask(__name__,template_folder='templates')

app = Flask(__name__)
@app.route('/')
def index():
  title='資料表單'
  return render_template('index.html',title=title)
@app.route('/predict',methods=['POST'])
def predict():
  title='預測結果'
  YDQ=request.form.get('YDQ')
  APGAR=request.form.get('APGAR')
  AGE=request.form.get('AGE')
  SEX=request.form.get('SEX')
  #model4=tf.keras.models.load_model('.\Model3')
  #newCase={'網路成癮分數YDQ':[int(YDQ)],'家庭滿意度apgar':[int(APGAR)],'年齡':[int(AGE)],'sex_男':[int(SEX)]}
  #newCase=pd.DataFrame(newCase)
  #PREDICT=(round(model4.predict(newCase)[0][0]*100,3))
  PREDICT=123
  return render_template('predict.html',title=title,YDQ=YDQ,APGAR=APGAR,AGE=AGE,SEX=SEX,PREDICT=PREDICT)

@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8000, debug=True)
# [END gae_flex_quickstart]
