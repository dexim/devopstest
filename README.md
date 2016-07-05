# DevOps Test
DevOps - Vagrant test 

Task:
Create a github or bitbucket git repository where you should include the following:

1- A simple app/webapp/script (you can choose your favourite language go/python/ruby/perl/bash/haskell/clojure/java, etc)  that listen on port 8080,
   and replay with a message like: "Hi there!!" or something along the lines to a GET / request and also log the request to /tmp/even.log
   if the source IP addresses (the one where the request come from) 4th octet is even and to /tmp/odd.log if its odd.

   So assuming your app/script is called "hello" and your ip is 10.22.1.2:
   After starting you app: ./hello
   if we use curl to do a get:
   curl http://10.22.1.2:8080  (assuming I'm doing the curl from the same machine where the app is running)
   we get a "hi there!!" back and a log entry must be created on /tmp/even.log, similar if the client is doing curl from an odd ip.

2 - vagrant file  that allows us to `vagrant up` and provision a linux box (you can choose whatever distro you like, ubuntu, centos.. etc)
  with nginx installed and configured as a proxy to the app you written on the previous task. You can choose any configuration management you like, but the deploy and configuration of nginx and your app must be done with a CM tool (chef, salt, puppet, ansible, cfengine..etc)
  The behaviour for your app must be the same even with nginx as proxy.
  NOTE: if you are not sure how to make vagrant use one of the CM tools supported check: https://www.vagrantup.com/docs/provisioning/

3 - This task is not mandatory but it would be a bonus point, if you can do the same as on step 2 but instead of vagrant and cm tools, use docker and docker-compose to accomplish the same.

To successfully accomplish this assignment we should get from you:
   - The url of a git repository, which will contain, the app you written and the vagrant file at least.
   - Of course if you also are willing to do the 3rd task it will include the Dockerfile and docker-compose.yml.
   - And instructions on how we should run what you did.
-----------------------------
Instructions:


