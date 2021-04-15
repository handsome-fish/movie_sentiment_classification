def format_sentences(file1, file2, trainfile, validfile, testfile):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, \
            open(trainfile, 'w') as train, open(validfile, 'w') as valid, open(testfile, 'w') as test:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        for i in range(1, len(lines1)):
            t1 = lines1[i].replace("-LRB-", "(")
            t2 = t1.replace("-RRB-", ")")
            k = lines2[i].strip().split(",")
            t = t2.strip().split('\t')
            if k[1] == '1':
                train.writelines(t[1])
                train.writelines("\n")
            elif k[1] == '2':
                test.writelines(t[1])
                test.writelines("\n")
            elif k[1] == '3':
                valid.writelines(t[1])
                valid.writelines("\n")


def tag_sentiment(infile, infile0, infile1, infile2):
    # ("sentiment_labels.txt", "dictionary.txt", "train.txt","train_final.txt")
    with open(infile, 'r') as info, open(infile0, 'r') as info0, open(infile1, 'r') as info1, \
            open(infile2, 'w') as info2:
        lines = info.readlines()
        lines0 = info0.readlines()
        lines1 = info1.readlines()

        text2id = {}
        for i in range(0, len(lines0)):
            s = lines0[i].strip().split("|")
            text2id[s[0]] = s[1]

        id2sentiment = {}
        for i in range(0, len(lines)):
            s = lines[i].strip().split("|")
            id2sentiment[s[0]] = s[1]

        for line in lines1:
            if line.strip() not in text2id:
                print(line.strip())
                # 由于特殊字符不匹配造成
                continue
            else:
                text_id = text2id[line.strip()]
            sentiment_score = id2sentiment[text_id]
            sentiment_label = 1
            if 0 <= float(sentiment_score) <= 0.2:
                sentiment_label = 1
            elif 0.2 < float(sentiment_score) <= 0.4:
                sentiment_label = 2
            elif 0.4 < float(sentiment_score) <= 0.6:
                sentiment_label = 3
            elif 0.6 < float(sentiment_score) <= 0.8:
                sentiment_label = 4
            elif 0.8 < float(sentiment_score) <= 1:
                sentiment_label = 5

            info2.write(line.strip() + "\t" + str(sentiment_label) + "\t" + "\n")


def short_sentences(filename):
    with open(filename, "r") as f1:
        with open("train_short_sentences.txt", "w") as f2:
            lines = f1.readlines()
            for line in lines:
                s = line.strip().split('\t')
                if len(s[0]) <= 10:
                    f2.write(s[0].strip() + '\t' + s[1] + '\t' + str(len(s[0])) + '\n')


def generate_phrases(file1, file2, file3, file4, file5, file6):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3, \
            open(file4, 'w') as f4, open(file5, "w") as f5, open(file6, "w") as f6:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        lines3 = f3.read(999999)

        text2id = {}
        for i in range(0, len(lines2)):
            s = lines2[i].strip().split("|")
            text2id[s[0]] = s[1]

        id2sentiment = {}
        for i in range(0, len(lines1)):
            s = lines1[i].strip().split("|")
            id2sentiment[s[0]] = s[1]

        # sentences = "|".join(lines3)

        for text in text2id:
            if text not in lines3:
                # print(text.strip())
                # 由于特殊字符不匹配造成
                continue
            else:
                text_id = text2id[text]
            sentiment_score = id2sentiment[text_id]
            sentiment_label = 1
            if 0 <= float(sentiment_score) <= 0.2:
                sentiment_label = 1
            elif 0.2 < float(sentiment_score) <= 0.4:
                sentiment_label = 2
            elif 0.4 < float(sentiment_score) <= 0.6:
                sentiment_label = 3
            elif 0.6 < float(sentiment_score) <= 0.8:
                sentiment_label = 4
            elif 0.8 < float(sentiment_score) <= 1:
                sentiment_label = 5

            f4.write(text + "\t" + str(sentiment_label) + "\n")
            f5.write(text + '\n')
            f6.write(str(sentiment_label) + '\n')


format_sentences("dataset/stanfordSentimentTreebank/datasetSentences.txt",
                 "dataset/stanfordSentimentTreebank/datasetSplit.txt", "train.txt", "valid.txt", "test.txt")

tag_sentiment("dataset/stanfordSentimentTreebank/sentiment_labels.txt",
              "dataset/stanfordSentimentTreebank/dictionary.txt", "train.txt", "train_final.txt")
tag_sentiment("dataset/stanfordSentimentTreebank/sentiment_labels.txt",
              "dataset/stanfordSentimentTreebank/dictionary.txt", "test.txt", "test_final.txt")
tag_sentiment("dataset/stanfordSentimentTreebank/sentiment_labels.txt",
              "dataset/stanfordSentimentTreebank/dictionary.txt", "valid.txt", "valid_final.txt")

short_sentences("train_final.txt")


generate_phrases("dataset/stanfordSentimentTreebank/sentiment_labels.txt",
                 "dataset/stanfordSentimentTreebank/dictionary.txt", "train.txt",
                 "train_phrase_label.txt", "train_raw_phrases", "train_raw_labels")
generate_phrases("dataset/stanfordSentimentTreebank/sentiment_labels.txt",
                 "dataset/stanfordSentimentTreebank/dictionary.txt", "test.txt",
                 "test_phrase_label.txt", "test_raw_phrases", "test_raw_labels")
