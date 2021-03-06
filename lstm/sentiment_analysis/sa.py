import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Method for text processing
def process_txt(data_list):

    data_processed = []
    for item in data_list:

        # Remove one char tokens
        text = re.sub(r'\b\w{1,1}\b', '', item[0])

        # Remove special chars
        special_chars = [',', '.', '"', ':', ')', '(', '-', '!', '?', '|', ';', "'", '$', '&', '/', '[', ']', '>', '%',
                         '=',
                         '#', '*', '+', '\\', '@', '_  ']
        for sp in special_chars:
            if sp in text:
                text = text.replace(sp, ' ')

        # Remove digits
        text = re.sub("\d", " ", text)

        # To lower case
        text = text.lower()

        # Tokenize text
        tokens = word_tokenize(str(text))

        # Remove english stop words
        filtered = [word for word in tokens if word not in stopwords.words('english')]

        # Rejoin tokens
        text = " ".join(filtered)

        data_processed.append(text)
    return data_processed


# Load data from csv files
train = pd.read_csv("train.csv", encoding = "ISO-8859-1")
test = pd.read_csv("test.csv", encoding = "ISO-8859-1")

# Get train data and labels
train_data = train.iloc[:, 5:6].values
train_labels = train.iloc[:, 0:1].values

# get test data and labels
test_data = test.iloc[:, 5:6].values
test_labels = test.iloc[:, 0:1].values

# Text preprocessing
test_data_processed = process_txt(test_data)
train_data_processed = process_txt(train_data)

print(test_data_processed)



