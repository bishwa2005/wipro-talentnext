scores = list(map(int, input("Enter the scores: ").split()))

highest = max(scores)

runner_up = None

for score in scores:
    if score != highest:
        if runner_up is None or score > runner_up:
            runner_up = score

print("Runner-up score:", runner_up)