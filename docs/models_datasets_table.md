## Base Datasets 

| Dataset Name | Location on Ceph | Size of Dataset |  Cleaning Steps performed | Sources of Dataset | Models trained | Model properties | Labels added | Dataset properties |
|:------------:|:----------------:|:---------------:|:-------------------------:|:------------------:|:--------------:|:----------------:|:-----------:|:------------------:|
|statements_sh_bal_cleaned.csv|/mnt/ceph/storage/data-tmp/teaching-current/ms19hove/Datasets/temp_ds/statements_sh_bal_cleaned.csv|~14mio rows|splitted, URLS with little success|twitter dump 01/02/2020, reddit dump may2015, blogs and news from kaggle| ... | ... | ... | 1/3 each source, shuffled |
|statements_static1.csv|/mnt/ceph/storage/data-tmp/teaching-current/ms19hove/Datasets/temp_ds/statements_static1.csv|~14mio rows|splitted, URLS with little success|twitter dump 01/02/2020, reddit dump may2015, blogs and news from kaggle| ... | ... | 0,1 Labels of martins static filter with one stage | 1/3 each source, shuffled |
| trump_administration_statement | /mnt/ceph/storage/data-tmp/teaching-current/jk76qufi/classified/trump_administration_statement.csv | 120597 |Split sentences removed unicode | ... | ...| ... | ... | future labels from FTR static filter
|statements_static2.csv| /mnt/ceph/storage/data-tmp/teaching-current/jk76qufi/datset2/statements_static2.csv| 100Mio (something went wrong) | removed faulty lines and lines < 3 > 25 | statements_sh_bal_cleaned.csv | | | 0,1 future referenzes from static filter 2 | future labels from FTR static filte |
| static_filter_2_classified.csv|/mnt/ceph/storage/data-tmp/teaching-current/jk76qufi/classified/static_filter_2_classified.csv|11.878.640|removed faulty lines and dublicates|statements_sh_bal_cleaned.csv|...|...|future labels from FTR static filte|future labels from FTR static filte|

## Training Datasets
|Dataset Name | 🤗 | Cleaning steps | splits | Source Dataset | labels |
|:------------:|:----------------:|:---------------:|:-------------------------:|:-------------------------:| :-------------------------:|
|jonaskoenig/trump_administration_statement| [🤗](https://huggingface.co/datasets/jonaskoenig/trump_administration_statement) | c1 | train, test, validation | trump_administration_statement | text, ft_tense |
| jonaskoenig/future-time-refernces-static-filter-D1 | [🤗](https://huggingface.co/datasets/jonaskoenig/future-time-refernces-static-filter-D1) | c1 | treain, test, validation | statements_static1.csv | text, ft_tense |
| jonaskoenig/Questions-vs-Statements-Classification |[🤗](https://huggingface.co/datasets/jonaskoenig/Questions-vs-Statements-Classification)| c2 | train, test, validation |[kaggle](https://www.kaggle.com/datasets/shahrukhkhan/questions-vs-statementsclassificationdataset) | text, labels
|jonaskoenig/reddit-blogspot-twitter|[🤗](https://huggingface.co/datasets/jonaskoenig/reddit-blogspot-twitter)| ... | none | statements_sh_bal_cleaned.csv | text, source |
|jonaskoenig/future-time-referenzes-faulty| [🤗](https://huggingface.co/datasets/jonaskoenig/future-time-referenzes-faulty)|c1| train,test,validation| 
|jonaskoenig/future-time-refernces-static-filter-D2|[🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references-D2)|c1|train,test,validation| static_filter_2_classified.csv | text, ft_tense |
|emotion| [🤗](https://huggingface.co/datasets/emotion) | c3 | train, test, validation all combined to one | ... | text, label | statements_static2.csv |text, ft_tense |
|go_emotions| [🤗](https://huggingface.co/datasets/go_emotions) | c3 | raw | ... |text all, labels for emotions| 
|yahoo_answers_topics|[🤗](https://huggingface.co/datasets/yahoo_answers_topics)| c4 | all | ... |texr, topics|

### Legende

c1 : removed faulty rows, removed all unicode (<U+000>) removed every http/https removed "RT" strings, removed all line breaks (\n,\r) and removed more then one whitspace

c2 : renamed column and removed useless column

c3 : all labels where converted to banary label, which can be processed

c4 : question_title and question_content combined to one label and are concated to the best_answer

## Models

|Model Name| 🤗 | Task | Training dataset | BaseModel |
|:------------:|:----------------:|:---------------:|:-------------------------:|:-------------------------:|
|jonaskoenig/xtremedistil-l6-h256-uncased-go-emotion|[🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-go-emotion) | sentiment analysis | emotions, go_emotions | [microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased)|
|jonaskoenig/xtremedistil-l6-h256-uncased-question-vs-statement-classifier|[🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-question-vs-statement-classifier)| removing questions | jonaskoenig/Questions-vs-Statements-Classification | [microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased) |
|jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references-D1| [🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references-D1) | future time referenzes | jonaskoenig/trump_administration_statement, jonaskoenig/future-time-refernces-static-filter-D1 | [microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased) | 
|jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references-D2|[🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references-D2)|future time referenzes |onaskoenig/trump_administration_statement, jonaskoenig/future-time-refernces-static-filter-D2 |[microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased) |
|jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references|[🤗](https://huggingface.co/jonaskoenig/xtremedistil-l6-h256-uncased-future-time-references)| future time referenzes | jonaskoenig/trump_administration_statement, jonaskoenig/future-time-referenzes-faulty | [microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased)|
|jonaskoenig/topic_classification_04| [🤗](https://huggingface.co/jonaskoenig/topic_classification_04) | topic clustering |yahoo_answers_topics |[microsoft/xtremedistil-l6-h256-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased) |

