# statements-about-the-future
This repo is intended to hold our code for the project with the general topic "statements about the future" in the seminar "Big Data and Language Technologies".

## Overleaf template
The template can be found [here](https://www.overleaf.com/1438418697pvwpsxsfbhsq).

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
