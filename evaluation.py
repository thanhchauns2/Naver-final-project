import csv
import pickle

labels = ["Probabilistic_Methods", "Neural_Networks", "Genetic_Algorithms", "Rule_Learning", "Reinforcement_Learning", "Case_Based", "Theory"]
def generate():
    sum = {}
    switch = {}
    probabilities = {}
    for i in range(len(labels)):
        sum[labels[i]] = {}
        switch[labels[i]] = {}
        probabilities[labels[i]] = {}
        for j in range(0, 1433):
            sum[labels[i]][j] = 0
            switch[labels[i]][j] = 0
            probabilities[labels[i]][j] = 0
    with open("./train_PTIT.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                for i in range(0, len(row) - 1):
                    if row[i] == '1':
                        sum[row[-1]][i] += 1
                        switch[row[-1]][i] += 1
                    else:
                        sum[row[-1]][i] += 1
                line_count += 1
            if line_count == 1500:
                break
        
    for i in range(len(labels)):
        for j in range(0, 1433):
            probabilities[labels[i]][j] = switch[labels[i]][j] / sum[labels[i]][j]
    

    file = open('evaluate.txt', 'wb')

    pickle.dump(probabilities, file)

    file.close()

generate()