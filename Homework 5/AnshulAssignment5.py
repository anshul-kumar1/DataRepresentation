import math
import json
import numpy as np
from numpy.linalg import norm

# Question

# Helper function for preprocessing the data
def clean_line(inp: str) -> str:
    final = ""
    for char in inp:
        if 97 <= ord(char) <= 122:
            final = final + char
        elif ord(char) == 32:
            final = final + char
        elif 65 <= ord(char) <= 90:
            final = final + char.lower()
    return final

with open('JEOPARDY_QUESTIONS.json', 'r') as file:
    d = json.load(file)

first_10000 = d[:10000]
question_data = []
for elem in first_10000:
    question_data.append(clean_line(elem['question']))

stop_words = ["the", "and", "of", "in", "a", "to", "is", "it", "you", "for", "on", "with", "this", "that", "are", "as", "be"]
dict_of_words = {}

i = 1
for line in question_data:
    temp = line.split()
    for word in temp:
        if word not in dict_of_words and word not in stop_words:
            dict_of_words[word] = i
            i = i + 1

i = 1
one_hot_encoded = []

for question in question_data:
    temp = question.split()
    for i in range(0, len(temp)):
        if temp[i] not in dict_of_words.keys():
            temp[i] = 0
        else:
            temp[i] = 1
    one_hot_encoded.append(temp)


# cosine_sim = []
# for i in range(0, len(one_hot_encoded)):
#     cosine = np.dot(i+1, i) / (norm(i+1, axis=1) * norm(i))
#     cosine_sim.append(cosine)
#
# print(cosine_sim)

import math
import json
import numpy as np
from numpy.linalg import norm

# Question

# Helper function for preprocessing the data
def clean_line(inp: str) -> str:
    final = ""
    for char in inp:
        if 97 <= ord(char) <= 122:
            final = final + char
        elif ord(char) == 32:
            final = final + char
        elif 65 <= ord(char) <= 90:
            final = final + char.lower()
    return final

with open('JEOPARDY_QUESTIONS.json', 'r') as file:
    d = json.load(file)

first_10000 = d[:10000]
question_data = []
for elem in first_10000:
    question_data.append(clean_line(elem['question']))

print(question_data)


corpus = [
    "Renewable energy advancements are reducing our reliance on fossil fuels. Solar, wind, and hydroelectric power offer cleaner alternatives that help combat climate change.",
    "Deforestation is accelerating climate change and biodiversity loss. Protecting forests is vital for maintaining ecological balance and supporting indigenous communities.",
    "Ocean acidification, a result of increased CO2 levels, poses a serious threat to marine biodiversity. Efforts to reduce carbon emissions are essential in mitigating this issue.",
    "Sustainable farming techniques can significantly lower agriculture's environmental footprint. Practices such as precision farming and permaculture promote soil health and biodiversity.",
    "Urbanization challenges include air pollution and waste management. Green architecture and sustainable city planning are crucial for creating livable urban environments.",
    "Water scarcity affects billions globally. Innovative water management strategies, such as rainwater harvesting and desalination, are key to ensuring water availability.",
    "Single-use plastics contribute significantly to global pollution. Policies encouraging the use of biodegradable materials can reduce the environmental impact of plastics.",
    "Electric vehicles (EVs) are becoming more accessible, offering a sustainable alternative to gasoline-powered cars. The expansion of EV infrastructure is critical for this transition.",
    "Global warming impacts weather patterns, leading to extreme weather events. Understanding and mitigating the effects of climate change is essential for disaster preparedness.",
    "Wildlife conservation efforts are crucial for protecting endangered species. Habitat restoration and anti-poaching laws help preserve biodiversity for future generations.",
]



# Preprocessing the data
def preprocess(data: list) -> list:
    final = []
    for line in corpus:
        final.append(clean_line(line))
    return final

# counting the number of times a word occurs in out given data
def freq_count(data: list) -> dict:
    final = {}
    for line in data:
        temp = line.split()
        for word in temp:
            if word not in final:
                final[word] = 1
            else:
                final[word] += 1
    return final

# calculating the inverse document frequency and returning the top 4 words
def calculate_tfidf(data: list) -> list:
    final = []
    processed_data = preprocess(data)
    total_count = 0
    for line in processed_data:
        total_count = total_count + len(line)
    occurrence = freq_count(processed_data)
    for val in occurrence:
        occurrence[val] = (math.log(total_count/occurrence[val]))
    final = sorted(occurrence, reverse=True)[0:4]
    return final

print(calculate_tfidf(corpus))