import pickle
import csv

divider = 0.25

def increase(probability, sum = 1):
    return probability + (1 - probability) * (1 - probability) * divider

def decrease(probability, sum = 1):
    return probability - probability * probability * divider


def self_learning():
    probabilities = {}
    with open('evaluate.txt', 'rb') as file:
        data = file.read()
        probabilities = pickle.loads(data)

    cnt = 0

    with open("./train_PTIT.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                labels = {
                    "Probabilistic_Methods": 1,
                    "Neural_Networks": 1,
                    "Genetic_Algorithms": 1,
                    "Rule_Learning": 1,
                    "Reinforcement_Learning": 1,
                    "Case_Based": 1,
                    "Theory": 1
                }
                for i in range(0, len(row) - 1):
                    if row[i] == '1':
                        for j in labels:
                            labels[j] *= (probabilities[j][i])
                labels = dict(sorted(labels.items(), key = lambda item: item[1], reverse = True))
                answer = row[-1]
                expected = list(labels.keys())[0]
                if answer != expected:
                    cnt += 1
                    for i in range(0, len(row) - 1):
                        if row[i] == '1':
                            sum = 0
                            for j in labels:
                                sum += probabilities[j][i]
                            for j in labels:
                                if j != answer:
                                    probabilities[j][i] = decrease(probabilities[j][i], sum)
                            probabilities[answer][i] = increase(probabilities[answer][i], sum)
            # if line_count == 500:
            #     break
    
    file = open('evaluate.txt', 'wb')

    pickle.dump(probabilities, file)

    file.close()

    print("Wrong tests: " + str(cnt))


for i in range(5):
    for j in range(10):
        self_learning()
    divider /= 2
