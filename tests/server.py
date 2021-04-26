from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "default return data (no parameters)"

@app.route("/<raw>")
def parameter(raw):

    raw_string = str(raw)
    args = raw_string.split('_')
    result = ""
    
    for i in range(len(args)):
        result += args[i]
        if i < len(args) - 1:
            result += ", "
    
    print(args)
    return ("raw parameters: " + result)

if __name__ == "__main__":
    app.run()
