from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "default return data (no parameters)"

@app.route("/<raw>")
def parameter(raw):

    raw_str = str(raw).lower()
    args = raw_str.split('_')
    return args[0] + " " + str(args)

if __name__ == "__main__":
    app.run()
