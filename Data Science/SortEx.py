# function sort top three scores
def top_three(scores):
    top_scores = []
    
    scores.sort()
    list_size = len(scores)
    top_scores = [scores[list_size-1], scores[list_size-2], scores[list_size-3]]
    
    return top_scores

# main code
score = [10, 12, 39, 57, 76, 13, 73]
result = top_three(score)

print(result)