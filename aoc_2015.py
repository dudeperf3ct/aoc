from typing import Dict, List
from collections import Counter
import re, json
# ## Q1 a: An opening parenthesis, (, means he should go up one floor, and 
# # a closing parenthesis, ), means he should go down one floor. To what floor do the instructions take Santa?
# ## Q1 b: find the position of the first character that causes him to enter the basement (floor -1).
# def find_floor(l:List) -> int:
#     c = 0
#     for i in range(len(l)):
#         if l[i] == "(":
#             c += 1
#         elif l[i] == ")":
#             c -= 1
#         if c == -1:
#             return i

# #Q2 a: All numbers in the elves' list are in feet. 
# # How many total square feet of wrapping paper should they order?
# def find_area(x:str) -> int :
#     arr = x.split("x")
#     arr = [int(x) for x in arr]
#     arr.sort()
#     l, h, w = arr
#     return 2*((l*h) + (h*w) + (l*w)) + (l*h)
# ## Slight variant of above
# def find_area_2(x:str) -> int :
#     arr = x.split("x")
#     arr = [int(x) for x in arr]
#     arr.sort()
#     l, h, w = arr
#     return (l*h*w) + 2*(l+h)

# # Q3: Moves are always exactly one house to the north (^), south (v), east (>), or west (<). 
# # After each move, he delivers another present to the house at his new location. 
# # How many houses receive at least one present?
# def move_santa(arr:str) -> int:
#     res = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
#     i, j, count = 0, 0, 0
#     res[0][0] = 1
#     for k in range(len(arr)):
#         if arr[k] == ">":
#             j += 1
#         elif arr[k] == "<":
#             j -= 1
#         elif arr[k] == "v":
#             i += 1
#         elif arr[k] == "^":
#             i -= 1
#         res[i][j] += 1
#     for i in range(len(arr)):
#          for j in range(len(arr)):
#               if res[i][j]>=1:
#                   count += 1
#     return count

# # Q3: Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# # then take turns. how many houses receive at least one present?
# ## inefficient O(n^2)
# def move_santa_2(arr:str) -> int:
#     count, res = 0, [[0 for _ in range(len(arr))] for _ in range(len(arr))]
#     for p in range(2):
#         i, j, count = 0, 0, 0
#         res[0][0] = 1
#         for k in range(p, len(arr), 2):
#             if arr[k] == ">":
#                 j += 1
#             elif arr[k] == "<":
#                 j -= 1
#             elif arr[k] == "v":
#                 i += 1
#             elif arr[k] == "^":
#                 i -= 1
#             res[i][j] += 1
#     for i in range(len(arr)):
#          for j in range(len(arr)):
#               if res[i][j]>=1:
#                   count += 1
#     return count

# # Q4: find MD5 hashes which, in hexadecimal, start with at least five zeroes. 
# # The input to the MD5 hash is some secret key followed by a number in decimal. 
# # To mine AdventCoins, you must find Santa the lowest positive number
# import hashlib
# def find_hash(code:str) -> str:
#     i = 0
#     while 1:
#         i += 1
#         hash = hashlib.md5((code + str(i)).encode()).hexdigest()
#         # # find one with 5 zeros
#         # if hash.startswith('0'*5):
#         #     return i
#         # find one with 6 zeros
#         if hash.startswith('0'*6):
#             return i

# Q5: find number of nice string which have following conditions
# It contains at least three vowels (aeiou only)
# It contains at least one letter that appears twice in a row
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

# def find_index(st:str, x:str) -> int:
#     c = x[0]
#     for i, s in enumerate(st):
#         if s == c and st[i:i+len(x)] == x:
#             return i

# def nice_strings(st:str) -> bool :
#     cond1, cond2, cond3 = False, False, True
#     vowels, c = ["a", "e", "i", "o", "u"], 0
#     not_contains = ["ab", "cd", "pq", "xy"]
#     for x in not_contains:
#         if x in st:
#             ind = find_index(st, x)
                ## dangerous to modify given string but we are safe here
#             st = st[:ind] + st[ind+len(x):]
#             cond3 = False
#             break
#     if not cond3:
#         return False
#     for i in range(len(st)-1):
#         if st[i] in vowels:
#             c += 1
#         if st[i] == st[i+1]:
#             cond2 = True
#         if c>=3:
#             cond1 = True
#     if st[-1] in vowels:
#         c += 1
#     if c>=3:
#         cond1 = True
#     return cond1 and (cond1 == cond2 == cond3)

# Q5 b: find number of nice string which have following conditions
# It contains a pair of any two letters that appears at least twice in the string without overlapping
# It contains at least one letter which repeats with exactly one letter between them
# my answer = 53 (wrong) completed
# def nice_strings_2(st:str) -> bool:
#     cond1, cond2 = False, False
#     # initially i wrote len(st)-3 [answer=53] with len(st)-2 [answer=55]
#     for i in range(len(st)-2):  #error here ... answer=53 using this code
#         x = st[i:i+3]
#         if x == x[::-1]:
#             cond2 = True
#             break
#     # for i in range(len(st)-2):   #correct answer=55
#     #     if st[i] == st[i+2]:
#     #         cond2 = True
#     #         break
#     if not cond2:
#         return cond2
#     for i in range(len(st)-2):
#         x = st[i:i+2]
#         if (x in st[:i]) or (x in st[i+2:]):
#             cond1 = True
#             break
#     return cond1

# # Q6 a: Given instructions, find how many lights are lit?
# def lights(arr:List) -> int:
#     res = [[False for _ in range(1000)] for _ in range(1000)]
#     for x in arr:
#         x = x.split(" ")
#         # toggle
#         if len(x)==4:
#             (x1, y1), (x2, y2) = x[1].split(","), x[3].split(",")
#             op = x[0]
#         # turn on or off
#         else:
#             (x1, y1), (x2, y2) = x[2].split(","), x[4].split(",")
#             op = x[1]
#         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#         for i in range(x1, x2+1):
#             for j in range(y1, y2+1):
#                 if (op == "on" and not(res[i][j])) or (op == "off" and res[i][j]):
#                     res[i][j] = not(res[i][j])
#                 elif op == "toggle":
#                     res[i][j] = not(res[i][j])
#     count = 0
#     for i in range(1000):
#         count += sum(res[i])
#     return count

# # Q6 b: Given instructions and brightness, find how total brightness of all lights?
# def lights(arr:List) -> int:
#     res = [[0 for _ in range(1000)] for _ in range(1000)]
#     for x in arr:
#         x = x.split(" ")
#         # toggle
#         if len(x)==4:
#             (x1, y1), (x2, y2) = x[1].split(","), x[3].split(",")
#             op = x[0]
#         # turn on or off
#         else:
#             (x1, y1), (x2, y2) = x[2].split(","), x[4].split(",")
#             op = x[1]
#         x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
#         for i in range(x1, x2+1):
#             for j in range(y1, y2+1):
#                 if op == "on":
#                     res[i][j] += 1
#                 elif op == "off":
#                     res[i][j] = max(0, res[i][j]-1)
#                 elif op == "toggle":
#                     res[i][j] += 2
#     count = 0
#     for i in range(1000):
#         count += sum(res[i])
#     return count


#Q7: a and b Subsittute bitwise operators
# def bit_manipulation(arr):
#     d = dict()
#     for x in arr:
#         v, k = x.split(" -> ")
#         if len(v.split(" ")) == 1:
#             d[k] = int(v)
#         else:
#             d[k] = v.split(" ")
#     while 1:
#         for k,v in d.items():
#             if k == "lx":
#                 if isinstance(v, int):
#                     return v
#             if isinstance(v, list):
#                 if "AND" in v or "OR" in v or "LSHIFT" in v or "RSHIFT" in v:
#                     try: 
#                         if isinstance(int(v[0]), int):
#                             x = int(v[0])
#                     except ValueError:
#                         x = d[v[0]]
#                     try: 
#                         if isinstance(int(v[-1]), int):
#                             y = int(v[-1])
#                     except ValueError:
#                         y = d[v[-1]]
#                     if "AND" in v and isinstance(x, int) and isinstance(y, int):
#                         d[k] = x & y
#                     if "OR" in v and isinstance(x, int) and isinstance(y, int):
#                         d[k] = x | y
#                     if "LSHIFT" in v and isinstance(x, int) and isinstance(y, int):
#                         d[k] = x << y
#                     if "RSHIFT" in v and isinstance(x, int) and isinstance(y, int):
#                         d[k] = x >> y
#                 if "NOT" in v:
#                     try: 
#                         if isinstance(int(v[1]), int):
#                             x = int(v[1])
#                     except ValueError:
#                         x = d[v[1]]
#                     if isinstance(x, int):
#                         d[k] = x ^ 65535

#Q8 a. Escape literal count string character and length
# def counts(arr):
#     c, l = 0, 0
#     for x in arr:
#         l += len(eval(x))
#         c += len(x)
#     return c-l
# b.
# def counts(arr):
#     c = 0
#     for x in arr:
#         c += x.count('\\') + x.count('"') + 2
#     return c

# #Q9 a and b. Travelling salesman problem
# def shortest_distance(arr):
#     cities = dict()
#     i, su = 0, []
#     for x in arr:
#         l, r = x.split(" to ")
#         r, _ = r.split(" = ")
#         if l not in cities:
#             cities[l] = i
#             i += 1
#         if r not in cities:
#             cities[r] = i
#             i += 1
#     print(cities)
#     matrix = [[float('-inf') for _ in range(len(cities))] for _ in range(len(cities))]
#     for k in cities.keys():
#         for x in arr:
#             l, r = x.split(" to ")
#             r, val = r.split(" = ")
#             val = int(val)
#             matrix[cities[l]][cities[r]] = val
#             matrix[cities[r]][cities[l]] = val
#         ind, s = (0, 0), 0
#         visited = [False for _ in range(len(cities))]
#         next_min = max(matrix[cities[k]])
#         min_ind = matrix[cities[k]].index(max(matrix[cities[k]]))
#         ind = (cities[k], min_ind)
#         visited[ind[0]] = True
#         visited[ind[1]] = True
#         s = next_min
#         # print("Start:", ind[0], s)
#         while sum(visited)!=len(cities):
#             next_min = max(matrix[ind[1]])
#             visited[ind[1]] = True
#             min_ind = matrix[ind[1]].index(max(matrix[ind[1]]))
#             # print("Not final Next:", ind[1], next_min, min_ind, matrix[ind[1]])
#             while visited[min_ind]:
#                 matrix[ind[1]][min_ind] = matrix[ind[1]][ind[1]]
#                 next_min = max(matrix[ind[1]])
#                 min_ind = matrix[ind[1]].index(max(matrix[ind[1]]))
#                 # print("new min:", next_min, min_ind, matrix[ind[1]])
#             # print("Final Next:", min_ind)
#             visited[min_ind] = True
#             s += next_min
#             ind = (ind[1], min_ind)
#         # print(k, s)
#         su.append(s)
#     # return min(su) ##part a change max to min and to float('inf')
#     return max(su)   ##part b change min to max and to float('-inf')

# # Q10 a and b. Look and say
# def look_and_say(arr):
#     s = arr[0]
#     count = 0
#     # while (count < 40):  ##part a
#     while (count < 50):    ##part b
#         c = 1
#         curr = ""
#         for i in range(len(s)):
#             if i!=len(s)-1 and s[i] == s[i+1]:
#                 c += 1
#             else:
#                 curr += str(c) + s[i]
#                 c = 1
#         s = curr
#         count += 1
#     return len(s)

# #Q11 a an b. valid password ---> submitted answers without code
# ## how to correct first and third requirement??
# def check1(s):
#     for i in range(len(s)-2):
#         if ord(s[i+1]) == ord(s[i])+1 and ord(s[i+2]) == ord(s[i])+2:
#             return True
#     return False    

# def check2(s):
#     if ("i" in s) or ("o" in s) or ("l" in s):
#         return True
#     return False

# def make2(s):
#     l = len(s)
#     for i, x in enumerate(s):
#         if x in ["i", "o", "l"]:
#             s = s[:i] + chr(ord(x)+1) + "a"*(l-i-1)
#             return s

# def check3(s):
#     seen = []
#     for i in range(len(s)-1):
#         if s[i] == s[i+1] and s[i] not in seen:
#             seen.append(s[i])
#         if len(seen) == 2:
#             return True
#     return False

# def valid_password(s="ghijklmn"):
#     while 1:
#         if not check1(s):
#             s = make1(s)
#         if not check2(s):
#             s = make2(s)
#         if not check3(s):
#             s = make3(s)
#         if check1(s) and check2(s) and check3(s):
#             return s

## Q12 a. ## stole from reddit
# with open("input", "r") as f:
#         string = f.read()
#print("Sum of all numbers 1:", sum(map(int, re.findall("-?[0-9]+", string))))
# #part b
# def hook(obj):
#   if "red" in obj.values(): 
#       return {}
#   else: 
#       return obj
# stuff = str(json.loads(string, object_hook=hook))
# print("Sum of all numbers 2:", sum(map(int, re.findall("-?[0-9]+", stuff))))

# # Q13 a. Find maximum happines sitting in circle
# def sitting_circular(arr):
#     s, i = 0, 0
#     d = dict()
#     for x in arr:
#         x = x.split(" ")
#         p1, p2 = x[0], x[-1].replace(".", "")
#         if p1 not in d:
#             d[p1] = i
#             i += 1
#         if p2 not in d:
#             d[p2] = i
#             i += 1
#     print(d)
#     matrix = [[-1000 for _ in range(len(d))] for _ in range(len(d))]
#     for x in arr:
#         x = x.split(" ")
#         p1, p2, n = x[0], x[-1].replace(".", ""), int(x[3])
#         if x[2] == "lose":
#             n = -n
#         matrix[d[p1]][d[p2]] = n
#     print(matrix)
#     return s

if __name__ == "__main__":
    with open("input", "r") as f:
        total = f.readlines()
    arr = []
    for x in total:
        arr.append(x.strip())