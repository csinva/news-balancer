from newspaper import build
import pickle

test = build(u'http://moneymorning.com/2014/03/10/todays-stock-market-news-earnings-calendar-15/')
article = test.articles[0]
print(article)
print(article.images)
print(article.imgs)
# print('loading wsj...')
# wsj = build('http://wsj.com')
# pickle.dump(wsj, open("wsj.pkl", "wb"))
# print('wsj.articles', wsj.articles)

# print('loading nyt...')
# nyt = build(u'http://nytimes.com')
# pickle.dump(nyt, open("nyt.pkl", "wb"))
# print('nyt.articles', nyt.articles)

# print('loading cnn...')
# cnn = build('http://cnn.com')
# pickle.dump(cnn, open("cnn.pkl", "wb"))
# print('cnn.articles', cnn.articles)
