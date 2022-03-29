import csv
import pickle

probabilities = {}
cnt = 0
answers = []

with open('./evaluate.txt', 'rb') as file:
    data = file.read()
    probabilities = pickle.loads(data)

with open("./test_data.csv", "r") as csv_file:
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
            expected = list(labels.keys())[0]
            answer = row[-1]
            if answer != expected:
                print("Wrong at token " + str(line_count + 1) + ". Expected: " + expected + " Got: " + answer)
                cnt += 1
            answers.append(expected)
            line_count += 1

with open("./test_data_after_training.txt", 'w') as file:
    for i in range(len(answers)):
        file.write(answers[i] + '\n')

print("Wrong tests: " + str(cnt))
        