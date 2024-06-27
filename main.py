from newspaper import Article
from newspaper import Config
import nltk
nltk.download('punkt')


def scrape_article(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()  # Perform NLP tasks like keyword extraction and summary generation
    return {
        'title': article.title,
        'authors': article.authors,
        'publication_date': article.publish_date,
        'summary': article.summary,
        'keywords': article.keywords,
        'text': article.text
    }

# Example usage
url = 'https://www.thehindu.com/news/'
article_data = scrape_article(url)
print(article_data)
