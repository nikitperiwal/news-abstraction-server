from text_summarizer import summarize_text
import mongo_utils
import schedule

curated_table = "curated_news"
processed_table = "processed_news"


def start_curating():
    """
    Reads from 'curated_news' table.
    Predicts abstract and categories from the news articles.
    Persists to 'processed_news' table.
    """
    news_articles = list(mongo_utils.read_from_mongo(curated_table))
    print(f"No. of news articles read from '{curated_table}': {len(news_articles)}")

    # Predicting abstract and categories for the news articles
    article_ids = list()
    for article in news_articles:
        article_ids.append(article["_id"])
        article["abstract"] = summarize_text(article["content"])
        # article["categories"] = predict_category(article["abstract"])

    print(f"Persisting {len(news_articles)} articles to '{processed_table}'.")
    mongo_utils.persist_to_mongo(news_articles, collection_name=processed_table)

    print(f"Removing the news articles from '{curated_table}'.")
    mongo_utils.remove_from_collection(article_ids, collection_name=curated_table)


def scheduler(interval: int):
    schedule.every(interval).minutes.do(
        start_curating
    )

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    scheduler(5)
