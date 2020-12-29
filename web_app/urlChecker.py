import urllib.request
import re
import pandas as pd

def URL_code(url):

    code = 99999

    try:
        connection = urllib.request.urlopen(url)
        code = connection.getcode()
        connection.close()
    except urllib.request.HTTPError as e:
        code = e.getcode()
    except Exception as e:
        q = 1

    print(code)

    # if(code >= 400 and code != 403):
    #     return True
    #
    # return False

    return(code)

    # regex = re.compile("page not found", re.I)
    # m = regex.match(html)
    # print(html)
    # print(m)


print('reading data...')
news = pd.read_csv("../data_news_aggregator/news_data_uci.csv")

urls = [u for u in news['URL']]

#news['QQQ'] = urls


codes = []
for u in urls:
    codes.append(URL_code(u))

news['URL_CODE'] = codes

news.to_csv("../data_news_aggregator/news_data_with_codes.csv")