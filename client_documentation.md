<h1>Client CLI Documentation</h1>
<h3>Installation and Execution</h3>
<ol>
  <li>Navigate to the <a href="https://github.com/hershyz/trie/releases/tag/client">client release</a> and download the <code>client.zip</code> file.</li>
  <li>Unzip the file. The only item inside the folder will be titled <code>triecli.py</code>.</li>
  <li><code>cd [working directory]</code></li>
  <li><code>python triecli.py</code></li>
</ol>

<h3>Commands</h3>
<pre>
help:          shows all available CLI commands
add            [words]: add words to the trie in one operation (separated by spaces)
delete         [words]: delete words from the trie in one operation (separated by spaces)
search         [words]: return words contained from the argument array (separated by spaces)
display:       displays the trie to the console
autocomplete:  (keyword): returns a list of autocomplete suggestions based on the argument
</pre>

<br>
<br>

<p><strong>NOTE:</strong><br>
  If testing the client on a different webserver (or locally), the address in <code>r = requests.get([address here]/ + url)</code> must be changed (line 33).
</p>
