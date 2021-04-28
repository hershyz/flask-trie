<h1>Server Documentation</h1>
<h3>Hosting</h3>
<p>
  The application is hosted through <a href="https://www.pythonanywhere.com/">PythonAnywhere</a>, but requirements/procfiles are included in the source for easy deployment to AWS, GCP, Azure, Heroku, etc. I was initially hosting the appliction on Heroku, but found that its free tier was simply not powerful enough to keep up with the tests I was running from the client CLI. This delay was actually causing incorrect results to be displayed to the client, so I switched the hosting to a PythonAnywhere webserver. Flask makes it easy to test server code locally using GET and POST requests, so I simply changed the address of which these requests were directed to when the app was deployed.
</p>
<h3>The Client CLI</h3>
<p>
  The client CLI uses a single GET request to send a command to the server and display the results of the command. Arguments are passed through the URL of the request, which are then parsed and verified by the server. From a systems design standpoint, we want argument verification to be done on the server side to prevent errors due to faulty args sent from a modified client. The beauty of this system is that new commands/functionality can be added to the server without modification to the client. The <a href="https://github.com/hershyz/trie/tree/main/tests">tests</a> folder in this repository contains files for local server testing. You are more than welcome to test the server locally in addition to testing through the webserver.
</p>
