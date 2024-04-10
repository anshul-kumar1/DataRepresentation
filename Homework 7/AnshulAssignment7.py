import librosa
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import ifft2, fftshift, ifftshift
from scipy.stats import stats
import heapq
import math


# Question 1
# a
def play_audio(file_name: str):
    audio, sr = librosa.load(file_name, sr=None)
    sd.play(audio, sr)
    sd.wait()

# playing the audio files
print(play_audio('audio_files/Instrumental.wav'))
print(play_audio('audio_files/No_Music.wav'))

# b
def plot_frequency_domain(data, sr, st):
    m = len(data)
    n = 2 ** int(np.ceil(np.log2(m)))
    y = np.fft.fft(data, n)
    f = np.fft.fftfreq(n, d=1 / sr)
    amplitude = np.abs(y) / n
    plt.plot(f[:n // 2], amplitude[:n // 2])
    plt.title('Frequency Domain Representation -' + st)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()

def data_and_sr(file_name: str):
    data, sr = librosa.load(file_name, sr=None)
    return data, sr

data_instrumental, sr_instrumental = data_and_sr('audio_files/Instrumental.wav')
data_no_music, sr_no_music = data_and_sr('audio_files/No_Music.wav')

print(plot_frequency_domain(data_instrumental, sr_instrumental, "Instrumental file"))
print(plot_frequency_domain(data_no_music, sr_no_music, "No Music file"))

# c
s1, sr1 = librosa.load('audio_files/Instrumental.wav', sr=None)
s2, sr2 = librosa.load('audio_files/No_Music.wav', sr=None)
max_length = max(len(s1), len(s2))

# Used to pad the signals to the same length
s1_padded = np.pad(s1, (0, max_length - len(s1)), mode='constant')
s2_padded = np.pad(s2, (0, max_length - len(s2)), mode='constant')

# Compute the FFT for each signal
fft1 = np.fft.fft(s1_padded)
fft2 = np.fft.fft(s2_padded)

combined_magnitude = np.abs(fft1) + np.abs(fft2)
combined_frequencies = fft1 + fft2
frequency = np.linspace(0, sr1, len(combined_magnitude))

plt.figure(figsize=(12, 6))
plt.plot(frequency[:len(combined_magnitude) // 2], combined_magnitude[:len(combined_magnitude) // 2])
plt.title('Combined Frequency Domain Representation')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()

# d
time_domain_signal = np.fft.ifft(combined_frequencies).real

# e
sr = max(sr_instrumental, sr_no_music)
sd.play(time_domain_signal, sr)
sd.wait()

# f
window_size = 1024
hop_length = 512
D = librosa.stft(s2, n_fft=window_size, hop_length=hop_length)
S_db = librosa.amplitude_to_db(abs(D), ref=np.max)

# g
plt.figure(figsize=(15, 6))
librosa.display.specshow(S_db, sr=sr2, hop_length=hop_length, x_axis='time', y_axis='log')
plt.colorbar(format="%+2.f")
plt.title('STFT Magnitude of "No_Music.wav"')
plt.show()


#####

graph_airports = {
    'HNL': [('LAX', 2555)],
    'LAX': [('SFO', 337), ('HNL', 2555), ('ORD', 1743), ('DFW', 1233)],
    'SFO': [('LAX', 337), ('ORD', 1843)],
    'ORD': [('SFO', 1843), ('LAX', 1743), ('DFW', 802), ('LGA', 150), ('PVD', 849)],
    'DFW': [('LAX', 1233), ('ORD', 802), ('LGA', 1387), ('MIA', 1120)],
    'LGA': [('DFW', 1387), ('ORD', 150), ('MIA', 1099), ('PVD', 142)],
    'PVD': [('LGA', 142), ('MIA', 1205)],
    'MIA': [('LGA', 1099), ('PVD', 1205)]

}
def shortest_path_dijkstra(graph, origin):
    distance_dict = dict()
    root = dict()
    visited = set()

    for i in graph:
        distance_dict[i] = math.inf
        root[i] = None
    distance_dict[origin] = 0
    count = 0

    while visited != (set(graph.keys())) and count <= len(graph.keys()):
        count += 1
        current_airport = None
        min_ = math.inf
        for air in distance_dict:
            if air not in visited:
                dist_air = distance_dict[air]
                if dist_air < min_:
                    min_ = dist_air
                    current_airport = air

        # maintaining the visited set
        visited.add(current_airport)

        for j in graph[current_airport]:
            next_ap = j[0]
            distance = j[1]
            if next_ap not in visited:
                new_dist = distance_dict[current_airport] + distance
                if new_dist < distance_dict[next_ap]:
                    distance_dict[next_ap] = new_dist
                    root[next_ap] = current_airport

    return distance_dict


print(shortest_path_dijkstra(graph_airports, 'ORD'))

# Question 3

# Prims Algorithm
def prims_algorithm(graph):
    begin = list(graph.keys())[0]
    visited = set()
    visited.add(begin)
    route = []
    total = 0
    while len(visited) < len(graph):
        holder = list()
        for current_airport in visited:
            edges = graph[current_airport]
            for j in edges:
                next_air = j[0]
                dist_air = j[1]
                if next_air not in visited:
                    if not holder:
                        holder = (current_airport, next_air, dist_air)
                    elif dist_air < holder[2]:
                        holder = (current_airport, next_air, dist_air)
                    else:
                        pass
        if holder:
            route_add = str(holder[0]), str(holder[2])
            route.append(route_add)
            visited.add(holder[1])
            total += holder[2]
    return route, total

def origin(airport, graph):
    if graph[airport] != airport:
        graph[airport] = origin(graph[airport], graph)
    return graph[airport]

def kruskal(graph):
    airport_dict = dict()
    for airport in graph:
        airport_dict[airport] = airport
    route = []
    total = 0
    holder = []

    list_of_airports = list(graph.items())
    for airport in list_of_airports:
        for x in airport[1]:
            curr_air = x[0]
            dist = x[1]
            holder.append((dist, airport[0], curr_air))
    sort_by_dist = sorted(holder)

    for elem in sort_by_dist:
        dist = elem[0]
        c = elem[1]
        p = elem[2]
        child_origin = origin(c, airport_dict)
        par_origin = origin(p, airport_dict)
        if child_origin != par_origin:
            route.append((c, p, dist))
            total += dist
            airport_dict[child_origin] = par_origin
    return route, total


def checker(graph):
    if prims_algorithm(graph)[1] == kruskal(graph)[1]:
        print("Prims:", prims_algorithm(graph_airports))
        print("Kruskals:", kruskal(graph_airports))
        return "The minimum spanning tree is the same for both algorithms"
    else:
        return "Error Encountered"

print(checker(graph_airports))