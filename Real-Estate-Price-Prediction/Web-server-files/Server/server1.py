from flask import Flask
import util


app = Flask(__name__)
 
@app.route('/')
def get_location_names():
    response =jsonify({
        'location': util.get_location_names()
    })
    response.headers.add('ACCESS-Control-Allow-Origin','*')
    return response

    return 'Hello, World!'

if __name__ == "__main__" :
    print('Starting Python Flask Server For Home Price Prediciton...')
    app.run()