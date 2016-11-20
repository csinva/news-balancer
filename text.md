## Inspiration
America is more divided than ever. In today's world incorrect news sources and politically biased articles stand in the way of a clear understanding of contemporary issues. In fact, the absence of differing viewpoints in today's media has led to echochambers in which peoples prejudices and beliefs are repeatedly confirmed. This leads to a lack of understanding between different groups that can breed discrimination and intolerance.

## What it does
News Balancer takes a story and provides articles on that story with credibility and varying political bias. The homepage will randomly generate a story from its archives, but a user can type in a query to get stories relating to their query along with their credibility / political bias.

## How I built it
1. News Balancer uses scikit learn to find similar articles based on a machine learning algorithm known as Multinomial Naive Bayes Classification. It was trained on a recently released dataset (News Data Aggregator, UCI 2016). 
2. The biases and credibility of publications within this dataset were evaluated using well-known websites (ex. allsides.com).
3. A Django application was built to visualize the biases in the studied articles, and also to extend it to new queries.

# Personal accomplishments
Our group struggled both with inexperience in using machine learning packages, understanding a new dataset, and especially with development using Django. It is a miracle to us that we were able to piece this together in the amount of time we did.

## What's next for News Balancer
News Balancer would best work as an extension for news sites that people already go to. Thus News Balancer should take the form of a Chrome extension that could in real-time, check the credibility and bias of sources on news websites. This is especially important for 