from flask import Flask
import trie as tr

app = Flask(__name__)

trie = tr.Trie()

@app.route("/")
def home():
    return "default return data (no parameters)"

@app.route("/<raw>")
def parameter(raw):

    raw_str = str(raw).lower()
    args = raw_str.split('_')
    
    if args[0] == "add":
        added = []
        error = []
        i = 1
        while i < len(args):
            success = trie.add_word(args[i])
            if success:
                added.append(args[i])
            else:
                error.append(args[i])
            i += 1
        return "added: " + str(added) + ", could not add: " + str(error)
    
    if args[0] == "display":
        print(trie.get_words)
        return str(trie.get_words())

    if args[0] == "search":
        found = []
        not_found = []
        i = 1
        while i < len(args):
            exists = trie.search(args[i])
            if exists:
                found.append(args[i])
            else:
                not_found.append(args[i])
            i+=1
        return "found: " + str(found) + ", not found: " + str(not_found)

    if args[0] == "autocomplete":
        if len(args) < 2:
            return "no argument given"
        return str(trie.autocomplete(args[1]))
    else:
        return "invalid command: '" + args[0] + "', check spelling and try again"

if __name__ == "__main__":
    app.run()
