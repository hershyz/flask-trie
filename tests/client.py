import requests

print("Trie CLI (github.com/hershyz/trie) - type 'help' for help")

def help():
    print("--- commands ---")
    print("help:          shows all available CLI commands")
    print("add            [words]: add words to the trie in one operation")
    print("delete         [words]: delete words from the trie in one operation")
    print("search         [words]: return words contained and not contained in the trie from the argument array")
    print("display:       displays the trie to the console")
    print("autocomplete:  (keyword): returns a list of autocomplete suggestions based on the argument")

def commandLoop():

    raw = input("> ")

    if len(raw) < 1:
        commandLoop()

    args = raw.split(" ")
    
    if args[0] == "help":
        help()

    else:
        url = ""
        for i in range(len(args)):
            url += args[i]
            if i < len(args) - 1:
                url += "_"

        r = requests.get("http://127.0.0.1:5000/" + url)
        print(r.text)

    commandLoop()

commandLoop()
