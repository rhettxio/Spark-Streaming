# Apache Spark Streaming of Twitter data - Fetching hashtags for Coronavirus

## Objective
Learning how to use tweepy create a connection with twitter and extract the live streaming data from twitter API. Using Spark streaming in PySpark handle the streaming data received and convert to dataframe save as SQL and live display the most popular hashtag topics.

### Prerequisites

1. Apache Spark
2. tweepy
3. pandas
4. matplotlib
5. seaborn
6. [A Twitter Developer Account](https://developer.twitter.com/)
7. Runing on Ubuntu

## Step 1
Using your Twitter Developer Account create a new App and save/memorizes your access code: 
1. consumer key
2. consumer secret
3. access token
4. access secret.

## Step 2
Write a file named Tweet_Fetch.py file that will connect to Twitter for streaming data and filters the data by tweets keyword. Notice that please enter your own access code saved in the step 1.
```
consumer_key = 'input your consumer_key'
consumer_secret = 'input your consumer_secret'
access_token = 'input your access_token'
access_secret = 'input your access_secret'
```

## Step 3
Build a pipeline in Spark retrieve the streaming data from Tweet_Fetch.py, process the data by extracing the hashtag of the tweets, ranking the top 10 topics and converting the data into dataframe and display it every 10 seconds.

## How you run the program
At the beginning, you can run the first part of the file Spark\_Tweet\_Streaming\_Project.ipynb until the line
```
RDDtuple.foreachRDD(process)
```
After that, open your teminal and run Tweet_Fetch.py under the certain directory
```
python3 Tweet_Fetch.py
```
You should able to see
```
Listening on port: 9999
```
Then go back to file Spark\_Tweet\_Streaming\_Project.ipynb and run the line
```
ssc.start()
```
Now, you are able to see the tweets keep showing on your terminal. Keep runing the following code
You are going to see the figure like this

***

![alt text](https://github.com/rhettxio/Apache-Spark-Streaming-of-twitter-data/blob/master/top10ranktag.png)

***

It will keep updating in every 10 seconds period (feel free to define any other period).
It will stop by runing the last line of code
```
ssc.stop()
```

## Built With

* [Ubuntu](https://ubuntu.com/)
* [Apache Spark](https://maven.apache.org/)

## Authors

* [Anqi Xiong](https://github.com/rhettxio/Apache-Spark-Streaming-of-twitter-data)

## Acknowledgments

* Udemy course: Spark and Python for Big Data with PySpark

