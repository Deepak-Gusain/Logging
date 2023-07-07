# Spark_Logging
Splunk and fluentd integration for logging

Steps for end to end logging solution:-

Problem:- 
Let say you have a spark application running on databricks, As you know we should write code in try block to handle any exception scenario. We must capture all logs to analyse our application.

Solution:-
Write logs using logging / py4j to a files (in our case to GCP bucket), from another job read these files and send it to splunk using "emit" function. Please refer python file.

a) you need to execute below command (Below are for linux):-
   --> apt-get update --fix-missing
   --> apt install ruby-full build-essential -y
   --> gem install fluentd fluent-plugin-splunk-hec
   
b) After that you have to create "final.conf" file this will be used by fluentd    to connect and flush logs to splunk. Please refer final.conf file.
   use below command to run fluentd
   
   -->  screen -d -m fluentd -c final.conf

c) We were using splunk logs for our application debugging and tracing.

d) for any cluster issues or in depth debugging you have to use databricks cluster logs   and spark UI logs.

e) We were running jobs using airflow (we are  also running multiple instance of same jobs for different location using airflow dag).

f) In Splunk you have to create HTTP Event collector and generate new token. This will be used in final.conf file. Remember port must be same in file and splunk gui. 

g) You have to create index and mention it in "final.conf" file. You have to mention that index then only you will be able to search these logs in splunk using "index present in final.conf" file. Otherwise use index="*" (if no index is created) 
