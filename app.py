from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def hello():
   return "Hello world! flask test"

#def testhtml():
 #   return render_template('test2.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')