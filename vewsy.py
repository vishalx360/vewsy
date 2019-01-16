from newsapi import NewsApiClient
print("vewsy v0.0.1")

# line break
print("")

# Init
newsapi = NewsApiClient(api_key='bbbecd9c85ec4499aacda1d1dc1e7ba2')


# asking for topic
topic = input("Topic ? : ")

# line break
print("")

# print articles function starts


def print_articles(topic):

    all_articles = newsapi.get_everything(q=str(topic))

    for index, article in enumerate(all_articles['articles']):
        print("("+str(index)+")" + " " + article['title'])
# function end


if topic == "":
    topic = "technology"
    print_articles(topic)
else:
    print_articles(topic)
