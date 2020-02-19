# Apache Spark Streaming of Twitter data

## Objective
Learning how to use tweepy create a connection with twitter and extract the live streaming data from twitter API. Using Spark streaming in PySpark handle the streaming data received and convert to dataframe save as SQL and live display the most popular hashtag topics.

### Prerequisites

1. Apache Spark
2. tweepy
3. pandas
4. matplotlib
5. seaborn
6. [A Twitter Developer Account](https://developer.twitter.com/)
7. Runing on Ubuntu.

## Step 1
Using your Twitter Developer Account create a new App and save/memorizes your access code: 
1. consumer key
2. consumer secret
3. access token
4. access secret.

## Step 2
Write a file named Tweet_Fetch.py file that will connect to Twitter for streaming data and filters the data by tweets keyword.

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
Now, you are able to see the tweets keep showing on your terminal. Execute the code before the line
```
ssc.stop()
```
You are going to see the figure like this
![alt text](https://github.com/rhettxio/Apache-Spark-Streaming-of-twitter-data/blob/master/top10ranktag.png)

## Built With

* [Ubuntu](http://www.dropwizard.io/1.0.2/docs/)
* [Apache Spark](https://maven.apache.org/)

## Authors

* [Anqi Xiong](https://github.com/rhettxio/Apache-Spark-Streaming-of-twitter-data)

## Acknowledgments

* Udemy course: Spark and Python for Big Data with PySpark

