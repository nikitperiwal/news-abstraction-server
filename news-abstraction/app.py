from text_summarizer import summarize_text
from news_classifier import predict_category
import mongo_utils
import schedule
import constants


def execute_subset(news_articles):
    article_ids = [article["_id"] for article in news_articles]
    article_contents = [article["content"] for article in news_articles]

    try:
        # Predicting abstract and categories for the news articles
        predicted_abstracts = summarize_text(article_contents)
        predicted_categories = predict_category(predicted_abstracts)

        for i, article in enumerate(news_articles):
            article["abstract"] = predicted_abstracts[i]
            article["category"] = predicted_categories[i]

        mongo_utils.persist_to_mongo(news_articles, collection_name=constants.PROCESSED_TABLE)
        mongo_utils.remove_from_collection(article_ids, collection_name=constants.CURATED_TABLE)

    except Exception as e:
        print("An exception occurred :", e)


def execute():
    """
    Reads from 'curated_news' table.
    Predicts abstract and categories from the news articles.
    Persists to 'processed_news' table.
    """

    news_articles = list(mongo_utils.read_from_mongo(constants.CURATED_TABLE))
    print(f"No. of news articles read from '{constants.CURATED_TABLE}': {len(news_articles)}")

    i = 0
    batch_size = 10
    while i < len(news_articles):
        print(f"Executing for {i+1}-{i+batch_size}")
        news_subset = news_articles[i: i + batch_size]
        execute_subset(news_subset)
        i += batch_size


def scheduler(interval: int):
    schedule.every(interval).minutes.do(
        execute
    )

    execute()
    while True:
        schedule.run_pending()


if __name__ == "__main__":
    scheduler(constants.SCHEDULE_MINUTES)
