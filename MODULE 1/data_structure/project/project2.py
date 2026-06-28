# Find the second highest (runner-up) score

scores = [2, 3, 6, 6, 5]

unique_scores = list(set(scores))
unique_scores.sort()

runner_up = unique_scores[-2]

print("Runner-up score:", runner_up)