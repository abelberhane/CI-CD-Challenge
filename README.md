# CI-CD-Challenge

The 3 main tasks that I will be taking on in this challenge are:

1) Create a simple REST API and package within a simple deployment
framework/pipeline.

2) Commit changes to a git repo and share the repo link.

3) Make sure the repo contains a README file that contains any assumptions you
may have made, and any instructions for getting the resulting environment up and
running.


My biggest challenge would be creating a REST API for the first time since my experience with them has only been consuming them. The next would be creating my first Docker contained app and integrating it into a pipeline. Working with NGINX hands on will be new as well but I am excited for the challenge.


<h1>Assumptions:</h1>
1) Using Github is an acceptable form of git.<br>
2) Another assumption that I have made is that application size does not matter, I was free to test out various imports and allowed my requirements.txt to grow as a result.<br>
3) I also assumed that Python 3.7.9 would be ok.<br>
4) I made the assumption that I should not spend all of my time working on problems like the HEAD request and the log request when I knew there was a lot of learning to do in regards to how to run Docker and what goes into a Docker Compose File let alone NGINX.<br>
5) Initially I made the assumption that I would be able to provide the log for the log parser in an example.log format before processing truly how you would be verifying it.<br>
6) After reviewing the python:buster image, I made the assumption that its apt-get apt-update around line 15-17 would update everything to its latest versions.<br>


<h1>Steps to Run:</h1>
<br>
1. Once you have downloaded the repo, change your directory to be inside of it. <br>
2. Run the following command to bring up the app:
	
	docker-compose up -d 


<h1>Endpoints to check</h1>
1. http://localhost:8080/<br>
2. http://localhost:8080/hello<br>
3. http://localhost:8080/error<br>