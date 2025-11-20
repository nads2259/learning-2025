from flask import Flask, jsonify,request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Creating a temporary API key
api_key = "myapikey"

@app.before_request
def verifyAPIKey():
    
    if request.method == "OPTIONS":
        return None
    
    if request.endpoint in ("home","contact"):
        key = request.headers.get("X-API-KEY")
        
        if (key != api_key):
            return jsonify({"error" : "Unauthorized access!"}),401


@app.route('/', methods=["GET"])
def home():
    return jsonify({
        "brand" : "pacific",
        "page" : "home",
        "content" : "Welcome to the Home Page of pacific!"
    })
    
    
@app.route('/contact',methods = ["GET"])
def contact():
    return jsonify({
        "brand" : "pacific",
        "page" : "contact",
        "content" : "Welcome to the Contact page of pacific! Feel free to contact us!"
    })


# Add a middleware to authenticate user request before delivering data

# Brand name

# Navigation - Home, Contact

# Body - It should deliver with respect to page. hint - different content for Home and different content for contact 

# Year and copyright info



if __name__ == "__main__":
    app.run(debug=True)