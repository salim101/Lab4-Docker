from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/indexfile")
def index():
	return "Index File"

@app.route("/user/<username>")
def show_user_profile(username):
	return " User %s " %username

@app.route("/post/<int:post_id>")
def show_post(post_id):
	return " Post %d " %post_id

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
