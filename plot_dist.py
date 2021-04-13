import matplotlib.pyplot as plt


def data_amount(file):
    values = [0] * 5
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            s = line.strip().split('\t')
            if int(s[1]) == 1:
                values[0] += 1
            elif int(s[1]) == 2:
                values[1] += 1
            elif int(s[1]) == 3:
                values[2] += 1
            elif int(s[1]) == 4:
                values[3] += 1
            else:
                values[4] += 1
        return values


def pie_chart(values, title):
    plt.figure(figsize=(4, 4))
    labels = [1, 2, 3, 4, 5]
    explode = [0.01] * 5
    plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%')
    # plt.title('Distribution of Samples in ' + title, loc='center')
    plt.savefig(title)  # 保存图片


# def count_short(filename):
#     values = [0] * 5
#     with open(filename, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             s = line.strip().split('\t')
#             if int(s[1]) == 1:
#                 values[0] += 1
#             elif int(s[1]) == 2:
#                 values[1] += 1
#             elif int(s[1]) == 3:
#                 values[2] += 1
#             elif int(s[1]) == 4:
#                 values[3] += 1
#             else:
#                 values[4] += 1
#         return values

def bar_chart(values):
    plt.figure(figsize=(4, 4))
    labels = [1, 2, 3, 4, 5]
    plt.bar(labels, values, 0.4, color="green")
    plt.xlabel("Label")
    plt.ylabel("Number of Short Sentences")
    # plt.title("bar chart")

    plt.show()
    plt.savefig("train_short_sentences.jpg")


pie_chart(data_amount("train_final.txt"), title="training Set")
pie_chart(data_amount("test_final.txt"), title="test Set")
# pie_chart(data_amount())
bar_chart(data_amount("train_short_sentences.txt"))
