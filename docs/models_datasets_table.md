## Base Datasets 

| Dataset Name | Location on Ceph | Size of Dataset |  Cleaning Steps performed | Sources of Dataset | Models trained | Model properties | Labels added | Dataset properties |
|:------------:|:----------------:|:---------------:|:-------------------------:|:------------------:|:--------------:|:----------------:|:-----------:|:------------------:|
|statements_sh_bal_cleaned.csv|/mnt/ceph/storage/data-tmp/teaching-current/ms19hove/Datasets/temp_ds/statements_sh_bal_cleaned.csv|~14mio rows|splitted, URLS with little success|twitter dump 01/02/2020, reddit dump may2015, blogs and news from kaggle| ... | ... | ... | 1/3 each source, shuffled |
|statements_static1.csv|/mnt/ceph/storage/data-tmp/teaching-current/ms19hove/Datasets/temp_ds/statements_static1.csv|~14mio rows|splitted, URLS with little success|twitter dump 01/02/2020, reddit dump may2015, blogs and news from kaggle| ... | ... | 0,1 Labels of martins static filter with one stage | 1/3 each source, shuffled |
| trump_administration_statement | /mnt/ceph/storage/data-tmp/teaching-current/jk76qufi/classified/trump_administration_statement.csv | 120597 |Split sentences removed unicode | ... | ...| ... | ... | future labels from FTR static filter

## Training Datasets
|Dataset Name | 🤗 | Cleaning steps | splits | Source Dataset | labels |
|:------------:|:----------------:|:---------------:|:-------------------------:|:-------------------------:| :-------------------------:|
|jonaskoenig/trump_administration_statement| [🤗](https://huggingface.co/datasets/jonaskoenig/trump_administration_statement) | c1 | train, test, validation | trump_administration_statement | text, ft_tense |
| jonaskoenig/future-time-refernces-static-filter | [🤗](https://huggingface.co/datasets/jonaskoenig/future-time-refernces-static-filter) | c1 | treain, test, validation | statements_static1.csv | text, ft_tense |
| jonaskoenig/Questions-vs-Statements-Classification |[🤗](https://huggingface.co/datasets/jonaskoenig/Questions-vs-Statements-Classification)| c2 | train, test, validation |[kaggle](https://www.kaggle.com/datasets/shahrukhkhan/questions-vs-statementsclassificationdataset) | text, labels


### Legende

c1 : removed faulty rows, removed all unicode (<U+000>) removed every http/https removed "RT" strings, removed all line breaks (\n,\r) and removed more then one whitspace

c2 : renamed column and removed useless column


## Models
