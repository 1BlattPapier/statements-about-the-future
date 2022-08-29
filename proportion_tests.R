
## read in data
data <- read.csv("./bert_static_testing.csv")

data$bert <- ifelse(data$prop_bert == "True", 1, 0)

data$static <- ifelse(data$prop_static == "True", 1, 0)

df <- data[,4:5]

t <- table(df)

prop_bert = t[2, 1] + t[2, 2]
prop_stat = t[1, 2] + t[2, 2]
all_samples = sum(table(df))

res <- prop.test(c(prop_bert, all_samples), c(prop_stat, all_samples), p = NULL, alternative = "less", correct = TRUE)
res

res_two_sided <- prop.test(c(prop_bert, all_samples), c(prop_stat, all_samples), p = NULL, alternative = "two.sided", correct = TRUE)
res_two_sided