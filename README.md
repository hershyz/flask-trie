<h1>hershyz/trie</h1>
<p>
  Backend autocomplete algorithm using Flask + Trie Nodes 🔍<br>
  [Slingshot Take-Home Challenge]
</p>

<h3>Overview</h3>
<p>
  The code in this repository contains a global state <a href="https://github.com/hershyz/trie/tree/main/server">server</a>, and a <a href="https://github.com/hershyz/trie/tree/main/client">client CLI</a> to access the server.<br>
  The server uses a trie object (a tree of linked character nodes) to store keywords in a set.<br>
  The client CLI uses HTTP GET requests to send commands to the server and retrieve information from the server.<br>
  The application is hosted through <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>, but requirements/procfiles are included in the source for easy deployment to AWS, GCP, Azure, Heroku, etc.
</p>

<h3>Requirements</h3>
<pre>
Server:   <a href="https://github.com/pallets/flask">Flask</a>
Client:   none
Additionally, procfile and deployment requirements can be found <a href="https://github.com/hershyz/trie/tree/main/server">here</a>.
</pre>

<h3>Additional Docs</h3>
<ul>
  <li><a href="https://github.com/hershyz/trie/blob/main/server_documentation.md">How the Server Works (Hosting and Client Interactions)</a></li>
  <li><a href="https://github.com/hershyz/trie/blob/main/client_documentation.md">Client CLI (Installation and Commands)</a></li>
</ul>

<br>

<p>
  <strong>Some Final Thoughts</strong><br>
  Prior to starting this project, my only knowledge of backend development consisted of a few YouTube videos that I had watched on Flask. I did not know how to deploy a web application, let alone devise a system to fulfill client requests comprehensively. In addition, the recursive structure of linked character nodes was not easy for me to visualize. I found myself stepping through testcases on a whiteboard more than actually coding. In retrospect (given more time), I would have written this in Nodejs because of its efficiency with real-time applications. But at the end of the day, Flask was still a very solid choice for the backend.<br>
  <br>
  Here are some of the most notable things I learned:<br>
  <ul>
    <li>How HTTP GET and POST requests work</li>
    <li>Deploying web applications using Git repositories</li>
    <li>Code working locally ≠ the behavior of the same code when deployed</li>
    <li>To my surprise, Python is an extremely viable tool for object oriented tasks</li>
  </ul>
  <br>
  <i>PS: The <code>tests</code> folder in this repo was used for updates as I was testing the server locally. If for some reason the server is not working, please DM me on Discord or send me an email.</i>
</p>
