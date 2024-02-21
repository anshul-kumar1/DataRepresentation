import math

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