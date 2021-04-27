import requests

print("Trie CLI (github.com/hershyz/trie) - type 'help' for help")

def help():
    print("--- commands ---")
    print("help: shows all available CLI commands")
    print("add (keyword): adds a keyword to the trie if it does not already exist")
    print("delete (keyword): deletes a keyword from the trie if it exists")
    print("search (keyword): finds out if a keyword is contained within the trie")
    print("display: displays the trie to the console")

def commandLoop():

    raw = input("> ")
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
