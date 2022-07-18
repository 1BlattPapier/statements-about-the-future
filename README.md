# statements-about-the-future
This repo is intended to hold our code for the project with the general topic "statements about the future" in the seminar "Big Data and Language Technologies".

## Documentation:

- [Datasets and Models](docs/models_datasets_table.md)

## Documents
- [The project expose can be found here.](https://www.overleaf.com/1438418697pvwpsxsfbhsq)
- [The project presention can be found here.](https://www.overleaf.com/5785149735scbmdytpypzp)
   - [Zero-Shot Learning in Modern NLP](https://joeddav.github.io/blog/2020/05/29/ZSL.html)

## AWS Credentials
BUCKET_NAMES =  ["corpus-iwo-internet-archive-wide00001"]

AWS_ACCESS_KEY_ID = ***REMOVED***

AWS_SECRET = ***REMOVED***

ENDPOINT_URL = ***REMOVED***

später als BUCKET_NAMES auch corpus-iwo-internet-archive-wide00010 und corpus-commoncrawl-main-2022-05 als BUCKET_NAMES

Datein sind WARC-Dateien. Die genaue Struktur könnt ihr euch mit s3cmd ls anzeigen lassen (https://s3tools.org/usage).

## Starting a Docker-Conatiner at the GPU Server
1. Login to ```ssh <username>@141.54.132.206```
2. execute ```screen```
3. execute: 
   ```
   srun --mem=32g enroot import --output firsttest.sqsh docker://ghcr.io/niklasdeckers/web-archive-keras:master
   ```
6. TODO

## Brainstorming about topic
- Daten über längeren Zeitraum
- Klimawandel
   - Riesen Ding
- Leicht klassifizierbar
- Unterthemen mit REGEX oder so? Sollte leicht zuzuordnen zu sein
- Sentiment analysis?
- Unsupervised clustering?
- Statements about the future in Zeitklassen
- In Jahren?
   - Zieljahre?
      - Aussagejahre
      - Unsicherheiten mit reinnehmen!
   - KI trainieren zu Aussagen
      - Klassifizieren
      - Aussagen zu Jahren treffen
   - Evaluierung?
## Concrete topic idea
1. General classification of statements about the future
2. 


### Questions
- How binding is the expose?
   - How concrete should our ideas/technologies be?
- Should we definitely use all data or are we allowed to restrict the data domain (platforms/websites/topics)?
- Our vague idea: we want to classify/split the data in different "time classes". Tell about our current discussion. What seems practical? Inspiration?
- What should be our end result?
   - Should we have a proper validation method?
   - Website where an arbitrary input is classified with a time?
   - Visualisation of topic clusters?
      - Subreddit future topic variation over time (maybe in reference to other official channels)
      - Topics discussed long term or short term - how long-term are topics discussed?

## Discussion on project expose
### Timetable
1. 24.06.2022: Usable data pipeline
   - Common Crawl
   - Evtl. Reddit dump
   - Beschränkung auf Englisch (so weit wie möglich)
   - Wahrscheinlich nicht web archive, weil Daten eher unpassend für uns
2. 26.06.2022: First basic statements about the future classifier
   - Most likely rule based, otherwise general trained model or tense classifier
   - [Need to evaluate](https://github.com/cbjrobertson/ftr_classifier)
   - Prompt engineering
   - [The_grammar_of_future_time_reference](https://www.researchgate.net/publication/243786675_The_grammar_of_future_time_reference_in_European_languages)
   - [Predictions](https://www.goodreads.com/quotes/tag?utf8=✓&id=predictions)
3. Manual evaluation
   - Probably above most complicated part
   - Might have to concentrate on good classification
   - Maybe prompt engineering
   - Use data to train model
4. 04.07.2022: Progress report presentation
5. 17.07.2022: Topic clustering
6. 31.07.2022: Interactive visualization by time and topics
   - Probably [t-SNE](https://towardsdatascience.com/visualising-high-dimensional-datasets-using-pca-and-t-sne-in-python-8ef87e7915b)
7.  29.08.2022, 22:00: Bug fixes, hot fixes, dirty rework

### Discussions
- Agreements
   - We almost have to do unsupervised clustering?
   - Data
      - Reddit (Reddit dump)
      - Myspace
         - We need to evaluate how much is in our internet archive data?
      - Blogs
         - Most likely blogspot
- What topic?
   - What statements about the future?
   - Tool for
   - Subtopic analysis clustering?
   - Extended sentinent/opinion clustering?
- What (data) domain?
   - Reddit
   - Twitter
   - Internet archive
   - Blogs

### Data
- https://huggingface.co/datasets/mschi/twitter_stream_pile/resolve/main/twitter_stream_2020_02_01.tar

- https://www.kaggle.com/datasets/kaggle/reddit-comments-may-2015

- https://www.kaggle.com/datasets/patjob/articlescrape

- https://files.pushshift.io/reddit/comments/daily/

#### Emotion Classification:
- https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-go-emotion
- https://huggingface.co/bergum/xtremedistil-l6-h384-go-emotion
- https://github.com/google-research/google-research/tree/master/goemotions/data/full_dataset

### Topic-Classification
- https://huggingface.co/facebook/bart-large-mnli

### Question or statement
- https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-question-vs-statement-classifier



## Expose Meeting
GPT-3 or not?
- Too expensive

Topic extraction
- Should check early on
- Could be a problem
- Deployable
- Github/papers with code probably better

Word "represantation" screams like embedding


Could be a problem: distributed by pyspark
- Can ask him when we run into problems

Dataset built with filters 
- is okay
- Should care about train test leakage
- Should test how bert performs
- Write both in paper
- Note statistics early on
- Care about train test split
Send problems via mail again

Metrics
- What metrics do we use to valuate
- Labeling by hand
- Significance of amount of handlables 
- Sources - test different sources

# Questions
- What is the structure of common crawl (because of sampling)
   - Time tags?
- Paper? what focus
   - What metrics
   - Significance tests?
   - Sources - test different sources
- What short sentences do we exclude?
   - Care about different formats from blogs, twitter, etc.
   - 25 words upper limit of sentences
- (Cleaning/Splitting/...)
   - Not sure how we split
   - NLTK
   - Special character are a problem - also for static classification - false negatives
# Out of scope Pipeline
- Elavuation filter
- Website
# Pipeline
- Single sentences
- Small batch size
- Pipeline should be streamed - json
- Sampling in pipeline
# Order of pipeline
0. Sampling
1. Cleaning
   - UTF-8 tokens
   - Everything except typical sentence things and letters
   - URLs
   - Splitting
2. Language
3. FTR classification
4. Sentinent classification
5. Topic classification
6. Database
# TODO
- Table for pipeline what where, etc. (Table)
- Raw template (Jonas)
- Project template (Jonas)
- Ask regarding paper (Martin)
