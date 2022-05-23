import glob
from typing import Dict, List

import redis

if __name__ == '__main__':
    r = redis.Redis(host="localhost", port=6379, db=0)
    #
    # path = "C:/Users/imwoodam/Downloads/Highest viewer Twitch streamers, past 3 days - SullyGnome*.csv"
    #
    # streamers: Dict[int, List[str]] = {i + 1: [] for i in range(50)}
    #
    # for filename in glob.glob(path):
    #     with open(filename, 'r', encoding="UTF-8") as f:
    #         for line in f:
    #             rank = line.split(",")[0][1:-1]
    #             streamer = line.split(",")[2][1:-1] if len(line.split(",")[2].split(" ")) == 1 else \
    #                 line.split(",")[2].split(" ")[1][1:-2]
    #
    #             if rank == "":
    #                 continue
    #             key = int(rank) % 50 if int(rank) % 50 != 0 else 50
    #             streamers[key].append(streamer)
    #
    # for i in range(1, 51):
    #     for val in streamers[i]:
    #         r.lpush(i, val.lower())

    for b in r.lrange("7", 0, 40):
        print(b.decode('utf-8'), end=" ")
