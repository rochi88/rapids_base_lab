import cudf
import numpy as np

import threading
# Using flask to make an api 
# import necessary libraries and functions 
from flask import Flask, jsonify, request 

from libs import log
logger = log.get_logger('root')

# import logging

# logger = logging.getLogger('root')
# logger_restapi = logging.getLogger('restapi')
# logger_rapids = logging.getLogger('rapids')

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

from pymongo import MongoClient

client = MongoClient("mongo:27017")

app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def index(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data}) 
  
# A simple function to calculate the square of a number 
# the number to be squared is sent in the URL when we use GET 
# on the terminal type: curl http://127.0.0.1:5000 / home / 10 
# this returns 100 (square of 10) 
@app.route('/home/<int:num>', methods = ['GET']) 
def disp(num): 

    logger_restapi.info(num**2)
    return jsonify({'data': num**2}) 

@app.route('/mongo/test')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"

def runApp():
    app.run(debug=True, use_reloader=False, port=5000, host='0.0.0.0')

def runMainWorker():
    # Load your time series data using cudf
    # Replace this with your actual data loading method
    # Assume 'data' contains your time series data
    data = np.random.randn(1000, 1)  # Example random data
    gdf = cudf.DataFrame({'value': data.flatten()})

    # Prepare features and target columns for prediction
    look_back = 10  # Number of past values to use as features for prediction
    gdf['target'] = gdf['value'].shift(-1)  # Shift target column by one time step
    for i in range(1, look_back + 1):
        gdf[f'feature_{i}'] = gdf['value'].shift(i)

    # Drop rows with NaN due to shifting for target column
    gdf.dropna(inplace=True)

    # Split the data into features and target variable
    X = gdf.drop(['value', 'target'], axis=1)
    y = gdf['target']
    logger.info(y)

if __name__ == '__main__':
    try:
        logger.debug(f'start first thread')
        t1 = threading.Thread(target=runApp).start()
        logger.debug(f'start second thread')
        t2 = threading.Thread(target=runMainWorker).start()
    except Exception as e:
        logger.error("Unexpected error:" + str(e))




