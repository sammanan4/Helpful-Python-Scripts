'''
Jorge is a physicist who has published many research papers and wants to know how much impact they have had in the academic community. 
To measure impact, he has developed a metric, H-index, to score each of his papers based on the number of times it has been cited by other papers. 
Specifically, the H-index score of a researcher is the largest integer H such that the researcher has H papers with at least H citations each.

Jorge has written N
papers in his lifetime. The i-th paper has Ci citations. 
Each paper was written sequentially in the order provided, and the number of citations that each paper has will never change. 
Please help Jorge determine his H-index score after each paper he wrote.

Input:
The first line of the input gives the number of test cases, T. 
T test cases follow. Each test case begins with a line containing N, the number of papers Jorge wrote. 
The second line contains N integers. The i-th integer is Ci, the number of citations that the i-th paper has.


Output:
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a space-separated list of N integers. 
The i-th integer is Jorge's H-index score after writing his i-th paper. 

Sample Input:
2
3
5 1 2
6
1 3 3 2 2 15

Sample Output:
Case #1: 1 1 2
Case #2: 1 1 2 2 2 3


Status: TLE
'''

t = int(input())
for j in range(1, t+1):
    _ = input()
    n = list(map(int, input().split(" ")))
    total = 1
    d = {n[0]: 1}
    print(f"Case #{j}: {total}", end=" ")
    for k in n[1:]:
        d[k] = d.get(k, 0) + 1
        if k > total and sum([v for g,v in d.items() if g > total]) > total:
            total+=1
        print(f"{total}", end=" ")
    print("")
