from collections import defaultdict
from csv import DictReader


def timeStringToMilliseconds(time):
    """
    Doing manually to avoid imports
    """
    hours, minutes, seconds = time.split(":")
    return int(hours) * 3600000 + int(minutes) * 60000 + int(float(seconds) * 1000)


trades = defaultdict(list)
with open('trades.csv', 'r') as f:
    reader = DictReader(f, fieldnames=['time', 'price', 'size', 'exchange'])
    for line in reader:
        trades[line['exchange']].append(timeStringToMilliseconds(line['time']))

answers = {}
for exchange, timestamps in trades.items():
    ans = 0
    indexOfLastInWindow = 0

    for i, timestamp in enumerate(timestamps):
        while indexOfLastInWindow < len(timestamps) and timestamps[indexOfLastInWindow] - timestamp < 1000:
            indexOfLastInWindow += 1
        if indexOfLastInWindow - i > ans:
            ans = indexOfLastInWindow - i

    answers[exchange] = ans

for answer in sorted(answers.items(), key=lambda x: x[0]):
    print(answer[1])
