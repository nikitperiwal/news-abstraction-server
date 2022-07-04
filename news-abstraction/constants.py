from secret_keys import mongo_username, mongo_password

# Defining the constants to be used throughout the app

NEWS_CATEGORIES = ['BUSINESS', 'DINING', 'ENTERTAINMENT', 'FASHION', 'PARENTING', 'POLITICS',
                   'SPORTS', 'TRAVEL', 'HEALTH', 'WORLD']

# Scheduler
SCHEDULE_MINUTES = 5

# MongoDB Constants
MONGO_URL = f"mongodb+srv://{mongo_username}:{mongo_password}@shortly.autde.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB_NAME = "news_db"
CURATED_TABLE = "curated_news"
PROCESSED_TABLE = "processed_news"

# News Category Model Parameters
CATEGORY_BASE_BERT = "distilbert-base-uncased"
CATEGORY_MODEL_WEIGHT_PATH = "models/News_Classifier_Weights/Weights"
NEWS_MAX_LENGTH = 75
NEWS_NUM_OUTPUT = len(NEWS_CATEGORIES)

# Text Abstraction Model Parameters
ABSTRACTION_MODEL = "facebook/bart-large-cnn"   # t5-base, t5-small
ABSTRACT_MAX_LENGTH = 75
ABSTRACT_MIN_LENGTH = 60
