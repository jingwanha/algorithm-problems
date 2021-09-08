from collections import defaultdict
import operator

def solution(genres, plays):
    answer = []
    best_album = defaultdict(int)
    genres_freq = defaultdict(list)

    for idx, (g, p) in enumerate(zip(genres, plays)):
        best_album[g] += p
        genres_freq[g].append((idx, p))

    best_album = sorted(best_album.items(), key=operator.itemgetter(1), reverse=True)

    for g_name, _ in best_album:
        for music_number, _ in sorted(genres_freq[g_name], key=operator.itemgetter(1), reverse=True)[:2]:
            answer.append(music_number)

    return answer

if __name__=='__main__':
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]

    res = solution(genres,plays)

    print(res)