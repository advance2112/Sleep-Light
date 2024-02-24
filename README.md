#Sleep Light

IFTTT made webhook requests a premium feature for some ungodly reason. So I made my own webhook handling app.

To run, install python, pip, and in pip install requests and flask.
Get a Lifx api token and insert it for <TOKEN>
Point your Sleep as Android to the port and ip address then /sleep
When your alarm goes off, all your lights will fade on a bright white
When your alarm is dismissed, it will instantly turn on the same bright white
