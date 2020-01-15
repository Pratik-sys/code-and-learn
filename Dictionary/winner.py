# Given an array of names of candidates in an election. A candidate name in array represents a vote casted to the candidate. Print the name of candidates received Max vote. If there is tie, print lexicographically smaller name.
# Check lexographically smaller/greater on wiki.

"""
Input :  votes[] = {"john", "johnny", "jackie", 
                    "johnny", "john", "jackie", 
                    "jamie", "jamie", "john",
                    "johnny", "jamie", "johnny", 
                    "john"};
Output : 'john'

We have four Candidates with name as 
'John', 'Johnny', 'jamie', 'jackie'. 
The candidates John and Johny get maximum votes.
Since John is alphabetically smaller, we print it.
"""
from collections import Counter


def winner(voters):
    vote_name = Counter(voters)
    name_vote = {}
    for value in vote_name.values():
        name_vote[value] = []
    for key, value in vote_name.items():
        name_vote[value].append(key)
    winner_value = sorted(name_vote, reverse=True)[0]
    winner_name = sorted(name_vote[winner_value])[0]
    print(f' The winner is {winner_name}')


winner(
    [
        "john",
        "johnny",
        "jackie",
        "johnny",
        "john",
        "jackie",
        "jamie",
        "jamie",
        "john",
        "johnny",
        "jamie",
        "johnny",
        "john",
    ]
)

