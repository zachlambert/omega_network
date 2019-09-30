from app import app

# GET requests should only return information, making no changes
# POST requests are used for requests which cause changes
# The speech and image endpoints are POST because although their primary
# usage is to process something and return a response, this may in future
# include updating information contained in the brain.

@app.route('/new', methods=['POST'])
def new():
    pass

@app.route('/state', methods=['GET'])
def state(id):
    pass

@app.route('/info', methods=['GET'])
def info(string):
    pass

@app.route('/speech', methods=['POST'])
def speech(string):
    pass

@app.route('/image', method=['POST'])
def image():
    pass
