#!/usr/bin/env python
# coding: utf-8

# In[1]:

# Build a listener class, which is responsible for sending data to a socket and picking up every tweet with a specific tag.

import tweepy
from tweepy import OAuthHandler,Stream


# In[2]:


from tweepy.streaming import StreamListener
import json
import socket


# In[3]:


consumer_key = 'input your consumer_key'
consumer_secret = 'input your consumer_secret'
access_token = 'input your access_token'
access_secret = 'input your access_secret'


# In[4]:


class TweetListener(StreamListener):
    
    def __init__(self,csocket):
        self.clientsocket = csocket
        
    def on_data(self,data):
        
        try:
            msg = json.loads(data) # create a message from json file
            print(msg['text'].encode('utf-8')) # Print the message and UTF-8 coding will eliminate emojis
            self.clientsocket.send(msg['text'].encode('utf-8')) # receiving data from the Twitter stream and send it to socket
            return True
        except BaseException as e:
            print('Error on_data: %s' % str(e))
        return True
    
    def on_error(self,status):
        print(status) # receiving error messages and print
        return True


# In[5]:


def sendData(c_socket): # Send the data to client socket, setting up connection
    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_secret)
    
    twitter_stream = Stream(auth,TweetListener(c_socket)) # Passes the tweets into the client socket
    twitter_stream.filter(track=['coronavirus'])


# In[ ]:


if __name__ == '__main__':
    s = socket.socket()       # Create a socket object
    host = '127.0.0.1'        # Get local machine name
    port = 9999               # Reserve a port for your connection service.
    s.bind((host,port))       # Bind to the port, create tuple
    
    print("Listening on port: %s" % str(port))
    
    s.listen(5)               # Now wait for client connection.
    c,addr = s.accept()       # Establish connection with client.
    
    sendData(c)               # Call sendData method to build a new connection.


# In[ ]:




