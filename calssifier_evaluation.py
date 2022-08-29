# compute evaluation metrics for the classifiers used in this project
# based on data obtained from handlabeling

import pandas as pd
import numpy as np

def compute_metrics(conf):
    tp = conf.iloc[1][1]
    tn = conf.iloc[0][0]
    fp = conf.iloc[0][1]
    fn = conf.iloc[1][0]

    tpr = tp / conf["All"][0]
    tnr = tn / conf["All"][1]
    # accuracy tp + tn / p + n
    
    acc = round((tp + tn) / 600, 3)

    # balanced accuracy (tpr + tnr) / 2

    bal_acc = round((tpr + tnr) / 2, 3)

    # precision tp / tp + fp
    prec = round((tp / (tp + fp)), 3)

    # recall tp / tp + fn
    rec = round(tp / (tp + fn), 3)

    # f-measure
    fm = round(2 * ((prec * rec) / (prec + rec)), 3)

    print(f"accuracy is: {acc}")
    print(f"balanced accuracy is: {bal_acc}")
    print(f"precision is: {prec}")
    print(f"recall is: {rec}")
    print(f"F-Measure is: {fm}")
    print(f"False Positives: {fp} and False Negatives: {fn}")
    print(f"Anteil false classified: { round((fp + fn )/ (fp + fn + tp + tn), 3) } ")

if __name__ == "__main__":
    
    # read data
    df = pd.read_csv("./eval_filter_and_bert.csv")
    df.drop(["Unnamed: 0"], axis=1, inplace=True)
    
    # computing future bert metrics
    conf = pd.crosstab(pd.Series(df["futurehandlabel"], name="True"), pd.Series(df["bertlabel"], name = "Predicted"), margins=True)
    print("metrics of the future BERT are:")
    print()
    compute_metrics(conf)
    print()

    ## analysing the static filter
    conf_stat = pd.crosstab(pd.Series(df["futurehandlabel"], name="True"), pd.Series(df["tense"], name = "Static"), margins=True)
    print("Metrics of the static filter are:")
    print()
    compute_metrics(conf_stat)
    print()

    
    
    # compute emotion and topic classifier metrics
    df_to_em = df.loc[ df["emotionhandlabel"].notnull() ]
    print(f"size of topic and emotion evaluation dataset is: {df_to_em.shape[0]}")
    
    # binary encoding of the true labels
    em_true_counts = df_to_em["emotionhandlabel"] > 0 
    top_true_counts = df_to_em["topichandlabel"] > 0 

    # emotion classifier
    print("Value counts for the EMOTION classifier:")
    print()
    print(df_to_em["emotionhandlabel"].value_counts())
    print()
    em_c = df_to_em["emotionhandlabel"].value_counts()
    print(f"proprtion of missclassified emotions: {round((em_c[0] / em_c.sum()) * 100, 3)}")
    print()

    ## topic classifier
    print("Value counts for the TOPIC classifier:")
    print()
    print(df_to_em["topichandlabel"].value_counts())
    print()
    top_c = df_to_em["topichandlabel"].value_counts()
    print(f"proprtion of missclassified topics: {round((top_c[0] / top_c.sum()) * 100, 3)}")
