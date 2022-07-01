from transformers import pipeline
import constants

summarizer = pipeline("summarization", model=constants.ABSTRACTION_MODEL)


def summarize_text(text_list):
    """
    Creates and returns summaries from a list of text.

    Parameters
    ----------
    text_list: The list of texts to summarize.

    Returns
    -------
    abstracts: The summarized abstracts from the list.
    """

    output = summarizer(
        text_list,
        max_length=constants.ABSTRACT_MAX_LENGTH,
        min_length=constants.ABSTRACT_MIN_LENGTH,
        do_sample=False
    )
    abstracts = []
    for x in output:
        abstracts.append(x['summary_text'])
    return abstracts
