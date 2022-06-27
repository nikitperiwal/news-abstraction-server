from transformers import pipeline

models = ["sshleifer/distilbart-cnn-12-6", "t5-base", "t5-small"]
summarizer = pipeline("summarization", model=models[2])


def summarize_text(text_list):
    """
    Creates and returns summaries from a list of text.

    Parameters
    ----------
    text_list  -> The list of texts to summarize.

    Returns
    -------
    abstracts  -> The summarized abstracts from the list.
    """

    output = summarizer(text_list, max_length=90, min_length=60, do_sample=False)
    abstracts = []
    for x in output:
        abstracts.append(x['summary_text'])
    return abstracts


if __name__ == "__main__":
    # TODO check running time for all models

    article="""AHMEDABAD: The Congress has decided to organise protests across all the 182 Assembly segments in Gujarat and the rest of the country on Monday for the rollback of the Centre\'s \' Agnipath \' scheme for recruitment in armed forces, party leader Alka Lamba said on Sunday.\n\nThe other demands of the party included filling up "62 lakh posts lying vacant in the Central and state governments" and the withdrawal of cases against the protesting youths, she said.\n\n"The Congress will hold protests in Gandhian style on June 27 across all the villages, districts, and Assembly constituencies in the country against the \'Agnipath\' scheme. Protests will also be organised across 182 Assembly constituencies in Gujarat," Lamba said.\n\nReferring to the " Jai Jawan , Jai Kisan" slogan, Congress said neither the jawan nor the farmers are happy in the country.\n\n"As many as 62 lakh posts in the Central and state governments are lying vacant. These should be filled up immediately. Out of these 62 lakh posts, 2,55,000 posts are for the Indian Army ," she said.\n\nLamba alleged the BJP-led Centre has slashed the budgetary provisions for the Army by 4 per cent compared to the erstwhile Congress government.\n\n"If the government claims that it has no money for salaries and pensions, then why only the armed forces are made to bear the cut?" she asked.\n\nLamba alleged that the government was intimidating non-violent protesters but Congress stands with them.\n\n"The Congress party will continue to fight in the interest of national security, the country and the youth," she said.\n\nLamba said the Prime Minister should shun his ego and talk to the youths instead of remaining silent on the issue.\n\n\n\nFOLLOW US ON SOCIAL MEDIA Facebook Twitter Instagram KOO APP YOUTUBE"""
    import time

    t = time.time()
    print(summarize_text(article))
    print(time.time()-t)

    t = time.time()
    print(summarize_text(article+" THE END"))
    print(time.time()-t)
