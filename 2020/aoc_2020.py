from typing import Dict, List
from collections import Counter, defaultdict
import math
import copy
# # Q1: Find the two entries that sum to 2020; what do you get if you multiply them together?
# def two_sum(l:List) -> int:
#     l.sort()
#     i, j = 0, len(l)-1
#     while (i <= j):
#         if l[i] + l[j] == 2020:
#             return l[i]*l[j]
#         elif l[i] + l[j] < 2020:
#             i += 1
#         else:
#             j -= 1
#     return 0

# # Q1: Find the three entries that sum to 2020; what do you get if you multiply them together?
# def two_sum(l, t) -> int:
#     i, j = 0, len(l)-1
#     while (i <= j):
#         if l[i] + l[j] == t:
#             return l[i]*l[j]
#         elif l[i] + l[j] < t:
#             i += 1
#         else:
#             j -= 1
#     return 0

# def three_sum(l) -> int:
#     l.sort()
#     for x in l:
#         p = two_sum(l, 2020-x)
#         if p!=0:
#             return p*x

# Q2: How many passwords are valid according to their policies?
# def correct_password(cs:List, ls:List, arr:List):
#     count = 0
#     for c, l, a in zip(cs, ls, arr):
#         lo, hi = c.split("-")
#         lo, hi = int(lo), int(hi)
#         print (lo, hi, l, a)
#         temp_dict = Counter(a)
#         if temp_dict[l] >= lo and temp_dict[l] <= hi:
#             count +=1
#     return count

# #Q2: How many passwords are valid according to their new policies?
# def correct_password(cs:List, ls:List, arr:List):
#     count = 0
#     for c, l, a in zip(cs, ls, arr):
#         lo, hi = c.split("-")
#         lo, hi = int(lo), int(hi)
#         a = list(a)
#         a.insert(0, "1")
#         print (lo, hi, l, a)
#         print (a[lo], a[hi])
#         if (a[lo] == l) ^ (a[hi] == l):
#             count += 1
#     return count

# # Q3: Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# # how many trees would you encounter?
# def find_path(arr:List) -> int:
#     i, j, count = 0, 0, 0
#     while (i!=len(arr)):
#         if (arr[i][j] == "#"):
#             count += 1
#         i += 1
#         j += 3
#     return count

# # Q3: Starting at the top-left corner of your map and following a slope of right 3 and down 1, 
# # Right 1, down 1. Right 5, down 1. Right 7, down 1. Right 1, down 2.how many trees would you encounter?
# def find_path_general(arr:List, right:int, down:int) -> int:
#     i, j, count = 0, 0, 0
#     while (i<len(arr)):
#         if (arr[i][j] == "#"):
#             count += 1
#         i += down
#         j += right
#     return count

# Q4: Count the number of valid passports - those that have all required fields.
# def validate_dict(arr:List) -> int:
#     fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
#     count = 0
#     for x in arr:
#         st = x.split(" ")
#         curr_fields = [s.split(":")[0] for s in st]
#         if "cid" not in curr_fields:
#             curr_fields.append("cid")
#         if fields == sorted(curr_fields):
#             count += 1
#     return count

# Q4: Count the number of valid passports - those that have all required fields with a
# additional conditions on each fields.
# def validate_dict_cond(arr:List) -> int:
#     fields = sorted(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
#     count = 0
#     for x in arr:
#         st = x.split(" ")
#         curr_fields = []
#         curr_fields_dict = dict.fromkeys(fields)
#         for s in st:
#             k, v = s.split(":")
#             curr_fields_dict[k] = v
#             curr_fields.append(k)
#         if "cid" not in curr_fields:
#             curr_fields.append("cid")
#         if fields == sorted(curr_fields) and all_conditions(curr_fields_dict):
#             count += 1
#     return count

# def all_conditions(curr_fields_dict: Dict) -> bool :
#     c = 0
#     ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
#     hcls = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
#     for k, v in curr_fields_dict.items():
#         if k == "byr":
#             if int(v) >= 1920 and int(v) <= 2002:
#                 c += 1
#         elif k == "cid":
#             c += 1
#         elif k == "iyr":
#             if int(v) >= 2010 and int(v) <= 2020:
#                 c += 1   
#         elif k == "eyr":
#             if int(v) >= 2020 and int(v) <= 2030:
#                 c += 1
#         elif k == "hgt":
#             if v[-2:] == "in" and int(v[:-2]) >= 59 and int(v[:-2]) <= 76:
#                 c += 1
#             elif v[-2:] == "cm" and int(v[:-2]) >= 150 and int(v[:-2]) <= 193:
#                 c += 1 
#         elif k == "ecl":
#             if v in ecls:
#                 c += 1
#         elif k == "pid":
#             try:
#                 if len(v) == 9 and int(v):
#                     c += 1  
#             except ValueError:
#                 break
#         elif k == "hcl":
#             if v[0] == "#" and len(v) == 7:
#                 c1 = 0
#                 for x in v[1:]:
#                     if x in hcls:
#                         c1 += 1
#                 if c1 == 6:
#                     c += 1
#                 else:
#                     break
#     return c==8

# Q5: 
# def find_row(arr:List) -> int :
#     lo, hi = 0, 127
#     for i in range(len(arr)):
#         if arr[i] == "F":
#             hi = math.floor((lo+hi)/2)
#         elif arr[i] == "B":
#             lo = math.ceil((lo+hi)/2)
#     return  lo if arr[-1] == "F" else hi

# def find_col(arr:List) -> int :
#     lo, hi = 0, 7
#     for i in range(len(arr)):
#         if arr[i] == "L":
#             hi = math.floor((lo+hi)/2)
#         elif arr[i] == "R":
#             lo = math.ceil((lo+hi)/2)
#     return  lo if arr[-1] == "L" else hi

# Q6: Find unique answers that everyone answered
#     with open("input", "r") as f:
#         total = f.readlines()
#     cand = [i+1 for i, x in enumerate(total) if x=="\n"]
#     arr, j = [""]*len(total), 0
#     arr[0] = total[0].strip()
#     for i in range(1, len(total)):
#         if total[i] == "\n":
#             j += 1
#             arr[j] = total[i+1].strip()
#         elif i in cand:
#             continue
#         else:
#             arr[j] = arr[j] + " " + total[i].strip()
#     arr = [x for x in arr if x!='']
#     res = []
#     for x in arr:
#         if len(x.split(" ")) == 1:
#             res.append(len(x))
#         else:
#             c = 0
#             l = len(x.split(" "))
#             x = list(x)
#             temp_dict = Counter(x)
#             for k,v in temp_dict.items():
#                 if v==l and k!=" ":
#                     c+=1
#             res.append(c)
#     for a, r in zip(arr, res):
#         print (a, r)
#     print(sum(res))

# # Q7: Find how many color contain at least one shiny gold?
# def find_shiny_gold(arr):
#     d = dict()
#     for x in arr:
#         if len(x.split(",")) == 1:
#             st = x.split(" ")
#             k = " ".join(st[0:2])
#             if k not in d:
#                 d[k] = [" ".join(st[5:7])]
#             else:
#                 d[k].append(" ".join(st[5:7]))
#         else:
#             s = x.split(",")
#             k = " ".join(s[0].split(" ")[0:2])
#             for i, y in enumerate(s):
#                 st = y.split(" ")
#                 if i==0:
#                     if k not in d:
#                         d[k] = [" ".join(st[5:7])]
#                     else:
#                         d[k].append(" ".join(st[5:7]))
#                 else:
#                     if k not in d:
#                         d[k] = [" ".join(st[2:4])]
#                     else:
#                         d[k].append(" ".join(st[2:4]))   
#     res = ["shiny gold"]
#     for r in res:
#         for k, v in d.items():
#             if r in v and k not in res:
#                 res.append(k)
#     return len(set(res))-1

# # # Q7 b: How many individual bags are required inside your single shiny gold bag?
# def count_shiny_gold(arr):
#     d = dict()
#     for x in arr:
#         if len(x.split(",")) == 1:
#             st = x.split(" ")
#             k = " ".join(st[0:2])
#             if k not in d:
#                 d[k] = [" ".join(st[4:7])]
#             else:
#                 d[k].append(" ".join(st[4:7]))
#         else:
#             s = x.split(",")
#             k = " ".join(s[0].split(" ")[0:2])
#             for i, y in enumerate(s):
#                 st = y.split(" ")
#                 if i==0:
#                     if k not in d:
#                         d[k] = [" ".join(st[4:7])]
#                     else:
#                         d[k].append(" ".join(st[4:7]))
#                 else:
#                     if k not in d:
#                         d[k] = [" ".join(st[1:4])]
#                     else:
#                         d[k].append(" ".join(st[1:4]))
#     for k, v in d.items():
#         print (k, v)
#     first = [k for k, v in d.items() if v[0] == "no other bags."]
#     print (first)
#     memo = dict.fromkeys(d.keys(), 0)
#     for f in first:
#         memo[f] = 1
#     # def recurse(k:str, memo):  ## failed attempt at recursion
#     #     print (k, d[k], memo)
#     #     if memo[k]!=0 and k not in first:
#     #         return memo[k]
#     #     if k in first:
#     #         return 0
#     #     for v in d[k]:
#     #         print (k, v, memo, memo[v[2:]])
#     #         if v[2:] in first and memo[v[2:]]!=0:
#     #             memo[k] += int(v[0]) * recurse(v[2:], memo)
#     #         elif memo[v[2:]]!=0 and v[2:] not in first:
#     #             memo[k] += int(v[0]) * recurse(v[2:], memo) + int(v[0])
#     #         else:
#     #             print ("second:", k, v[2:], memo)
#     #             memo[k] += recurse(v[2:], memo)
#     def recurse(k:str, memo):
#         # print (k, d[k], memo)
#         if memo[k]!=0:
#             return memo[k]
#         for v in d[k]:
#             # print (k, v, memo, memo[v[2:]])
#             if v[2:] in first:
#                 memo[k] += int(v[0]) * recurse(v[2:], memo)
#             else:
#                 memo[k] += int(v[0]) * recurse(v[2:], memo) + int(v[0])
#         #     print ("second:", k, v, memo)
#         # print ("third:", memo)
#         return memo[k]
#     res = recurse('shiny gold', memo)
#     # print (memo)
#     return res

## Q7 a: Run your copy of the boot code. 
# Immediately before any instruction is executed a second time, what value is in the accumulator?
# def acc_value(arr:List) -> int:
#     acc, i = 0, 0
#     state = [False]*len(arr)
#     while 1 and i<len(arr):
#         if (not state[i]):
#             inst = arr[i].split(" ")
#             state[i] = True
#             if inst[0] == "nop":
#                 i += 1
#             elif inst[0] == "acc":
#                 acc += int(inst[1])
#                 i += 1
#             elif inst[0] == "jmp":
#                 i += int(inst[1])
#         else:
#             break
#     return acc 

## Q7 a: One of jmp or nop is swapped bcoz of which program doesn't terminate. 
# Correct that and find what value is in the accumulator after program terminates?
# def acc_value(arr:List) -> int:
#     acc, i, flag = 0, 0, False
#     state = [False]*len(arr)
#     while 1 and i<len(arr):
#         if (not state[i]):
#             inst = arr[i].split(" ")
#             state[i] = True
#             if inst[0] == "nop":
#                 i += 1
#             elif inst[0] == "acc":
#                 acc += int(inst[1])
#                 i += 1
#             elif inst[0] == "jmp":
#                 i += int(inst[1])
#         else:
#             flag = True
#             break
#     return acc, flag 

# def acc_value_2(arr:List) -> int:
#     jmp_idx = [i for i, x in enumerate(arr) if "jmp" in x]
#     nop_idx = [i for i, x in enumerate(arr) if "nop" in x]
#     for j in jmp_idx:
#         tmp_arr = copy.deepcopy(arr)
#         tmp_arr[j] = tmp_arr[j].replace("jmp", "nop")
#         a, f = acc_value(tmp_arr)
#         if not f:
#             return a

#     for j in nop_idx:
#         tmp_arr = copy.deepcopy(arr)
#         tmp_arr[j] = tmp_arr[j].replace("nop", "jmp")
#         a, f = acc_value(tmp_arr)
#         if not f:
#             return a

## Q8 a: What is the first number that does not have this property?
# def encoding_error(arr:List, k=25):
#     i = 0
#     while 1:
#         flag = False
#         tmp_arr = arr[i:i+k]
#         curr = arr[i+k]
#         for j in range(k):
#             if (curr-tmp_arr[j] in tmp_arr) and (arr[i+j]!=curr-tmp_arr[j]) :
#                 flag = True
#                 break 
#         if not flag:
#             return curr
#         i += 1
## Q8 b: Find contigous set from arr which sum upto above question number. 
## Find sum of lowest and max of that set.
# def error2(arr:List, k=25):
#     res = encoding_error(arr, k)
#     for i in range(len(arr)):
#         s = arr[i]
#         v = []
#         v.append(i)
#         for j in range(i+1, len(arr)):
#             if s+arr[j] == res:
#                 v.append(j)
#                 return v
#             elif s+arr[j] < res:
#                 s += arr[j]
#                 v.append(j)
#             else:
#                 break

# #Q9 a: Find number of 1-difference jolts and 3-diff jolts
# def jolts(arr:List) -> int:
#     arr.sort()
#     res = {0:0, 1:0, 2:0, 3:1}
#     for i in range(len(arr)-1):
#         diff = arr[i+1] - arr[i]
#         if arr[i] <= 3 and i==0:
#             res[arr[i]] += 1
#         if diff <= 3:
#             res[diff] += 1
#     return res[1]*res[3]

#Q9 b: Find all combinations


#Q10 a: Find seats after they stabilize
# def check_sides(arr, i, j, rows, cols, val)-> int:
#     count = 0
#     if j+1 < cols:
#         if arr[i][j+1] == val:
#             count += 1
#     if j-1 >= 0:
#         if arr[i][j-1] == val:
#             count += 1
#     if i+1 < rows:
#         if arr[i+1][j] == val:
#             count += 1
#     if i-1 >= 0:
#         if arr[i-1][j] == val:
#             count += 1
#     return count

# def check_diag(arr, i, j, rows, cols, val)-> int:
#     count = 0
#     if j+1 < cols and i+1 < rows:
#         if arr[i+1][j+1] == val:
#             count += 1
#     if j-1 >= 0 and i+1 < rows:
#         if arr[i+1][j-1] == val:
#             count += 1
#     if j-1 >= 0 and i-1 >= 0:
#         if arr[i-1][j-1] == val:
#             count += 1
#     if i-1 >= 0 and j+1 < cols:
#         if arr[i-1][j+1] == val:
#             count += 1
#     return count

# def pretty_print(arr):
#     s = []
#     for i in range(len(arr)):
#         s.append("".join(arr[i]))
#     for x in s:
#         print (x)    

# def seats(arr) -> int:
#     # pretty_print(arr)
#     rows = len(arr)
#     cols = len(arr[0])
#     c = 0
#     while 1:
#         curr_arr = copy.deepcopy(arr)
#         for i in range(rows):
#             for j in range(cols):
#                 if arr[i][j] == ".":
#                     continue
#                 if arr[i][j] == "L":
#                     c1, c2 = check_sides(arr, i, j, rows, cols, "#"), check_diag(arr, i, j, rows, cols, "#")
#                     if c1+c2 == 0:
#                         curr_arr[i][j] = "#"
#                 if arr[i][j] == "#":
#                     c1, c2 = check_sides(arr, i, j, rows, cols, "#"), check_diag(arr, i, j, rows, cols, "#")
#                     if c1+c2 >= 4:
#                         curr_arr[i][j] = "L"
#         c += 1
#         # print (c)
#         # pretty_print(curr_arr)
#         if curr_arr == arr:
#             break
#         else:
#             arr = copy.deepcopy(curr_arr)
#     # print ("Over:")
#     # pretty_print(arr)
#     count = 0
#     for i in range(rows):
#         for j in range(cols):
#             if arr[i][j] == "#":
#                 count += 1
#     return count

# def ispresent(arr, x, y, rows, cols, val, r=False, inc=True):
#     if r:
#         if inc:
#             while (x<rows):
#                 if arr[x][y] == val:
#                     return True
#                 x += 1
#             return False
#         else:
#             while (x>=0):
#                 if arr[x][y] == val:
#                     return True
#                 x -= 1
#             return False
#     else:
#         if inc:
#             while (y<cols):
#                 if arr[x][y] == val:
#                     return True
#                 y += 1
#             return False
#         else:
#             while (y>=0):
#                 if arr[x][y] == val:
#                     return True
#                 y -= 1
#             return False

# def check_sides2(arr, i, j, rows, cols, val)-> int:
#     count = 0
#     if j+1 < cols:
#         if ispresent(arr, i, j+1, rows, cols, val, r=False, inc=True):
#             count += 1
#     if j-1 >= 0:
#         if ispresent(arr, i, j-1, rows, cols, val, r=False, inc=False):
#             count += 1
#     if i+1 < rows:
#         if ispresent(arr, i+1, j, rows, cols, val, r=True, inc=True):
#             count += 1
#     if i-1 >= 0:
#         if ispresent(arr, i-1, j, rows, cols, val, r=True, inc=False):
#             count += 1
#     return count

# def ispresent2(arr, x, y, val, rows, cols, incx=True, incy=True):
#     if incx and incy:
#         while (x<rows and y<cols):
#             if arr[x][y] == val:
#                 return True
#             x += 1
#             y += 1
#         return False
#     elif (not incx) and (not incy):
#         while (x>=0 and y>=0):
#             if arr[x][y] == val:
#                 return True
#             x -= 1
#             y -= 1
#         return False
#     elif (not incx) and incy:
#         while (x>=0 and y<cols):
#             if arr[x][y] == val:
#                 return True
#             x -= 1
#             y += 1
#         return False
#     elif incx and (not incy):
#         while (x<rows and y>=0):
#             if arr[x][y] == val:
#                 return True
#             x += 1
#             y -= 1
#         return False

# def check_diag2(arr, i, j, rows, cols, val)-> int:
#     count = 0
#     if j+1 < cols and i+1 < rows:
#         if ispresent2(arr, i+1, j+1, val, rows, cols, True, True):
#             count += 1
#     if j-1 >= 0 and i+1 < rows:
#         if ispresent2(arr, i+1, j-1, val, rows, cols, True, False):
#             count += 1
#     if j-1 >= 0 and i-1 >= 0:
#         if ispresent2(arr, i-1, j-1, val, rows, cols, False, False):
#             count += 1
#     if i-1 >= 0 and j+1 < cols:
#         if ispresent2(arr, i-1, j+1, val, rows, cols, False, True):
#             count += 1
#     return count

# def seats2(arr) -> int:
#     # pretty_print(arr)
#     rows = len(arr)
#     cols = len(arr[0])
#     c = 0
#     while 1:
#         curr_arr = copy.deepcopy(arr)
#         for i in range(rows):
#             for j in range(cols):
#                 if arr[i][j] == ".":
#                     continue
#                 # ??What?? empty seats that see no occupied seats become occupied <-- Error here
#                 if arr[i][j] == "L":
#                     c1, c2 = check_sides(arr, i, j, rows, cols, "#"), check_diag(arr, i, j, rows, cols, "#")
#                     if c1+c2 == 0:
#                         curr_arr[i][j] = "#"
#                 if arr[i][j] == "#":
#                     c1, c2 = check_sides2(arr, i, j, rows, cols, "#"), check_diag2(arr, i, j, rows, cols, "#")
#                     if c1+c2 >= 5:
#                         curr_arr[i][j] = "L"
#         c += 1
#         print (c)
#         pretty_print(curr_arr)
#         if curr_arr == arr or c>=3:
#             break
#         else:
#             arr = copy.deepcopy(curr_arr)
#     # print ("Over:")
#     # pretty_print(arr)
#     count = 0
#     for i in range(rows):
#         for j in range(cols):
#             if arr[i][j] == "#":
#                 count += 1
#     return count

# Q13 a: How much time till you catch the earliest bus?
# def catch_bus(arr):
#     depart = int(arr[0])
#     times = [int(n) for n in arr[1].split(",") if n!="x"]
#     res = [x-(depart%x) for x in times]   
#     return times[res.index(min(res))] * min(res)

# b: Find sequential earliest times
# def compute_lcm(a):
#     lcm = a[0]
#     for i in a[1:]:
#         lcm = lcm * i // math.gcd(lcm, i)
#     return lcm

# def catch_bus_1(arr):
#     times = {i : int(n) for i,n in enumerate(arr[1].split(",")) if n!="x"}
#     # ##brute-force
#     # i = 100000000000000
#     # while 1:
#     #     count = 0
#     #     for k, v in times.items():
#     #         if (i+k) % v == 0:
#     #             count += 1
#     #         else:
#     #             break
#     #     if count == len(times):
#     #         return i
#     #     i += times[0]
#     res = [times[0]]
#     i = 0
#     while 1:
#         i += compute_lcm(res)
#         for k, v in times.items():
#             if (i+k) % v == 0:
#                 if v not in res:
#                     res.append(v)
#         if len(res) == len(times):
#             return i

# # Q 14 a and b. Mask operations
# def match_str(b, mask):
#     p = []
#     for i in range(36):
#         if mask[i] == "X":
#             p.append(b[i])
#         else:
#             p.append(mask[i])
#     return "".join(p)

# def match_str1(b, mask):
#     get_bin = lambda x1, n: format(x1, 'b').zfill(n)
#     n = Counter(mask)['X']
#     res = []
#     r = []
#     for i in range(36):
#         if mask[i] == "0":
#             r.append(b[i])
#         else:
#             r.append(mask[i])
#     r = "".join(r)
#     for i in range(1<<n): 
#         temp = get_bin(i, n)
#         t, j = "", 0
#         for x in r:
#             if x == "X":
#                 t += temp[j]
#                 j += 1
#             else:
#                 t += x
#         res.append(t)
#     return res

# def eval_mask(arr):
#     val = defaultdict()
#     get_bin = lambda x1, n: format(x1, 'b').zfill(n)
#     for x in arr:
#         if "mask" in x:
#             _, mask = x.split(" = ")
#         else:
#             v, d = x.split(" = ")
#             _, v = v.split("[")
#             v = int(v[:-1])
#             b = get_bin(int(v), 36)
#             res = match_str1(b, mask)
#             # b = get_bin(int(d), 36)
#             for r in res:
#                 val[r] = int(d)
#     return sum(v for v in val.values())

# # Q15 a. Elves take turn in game
# def find_number(arr):
#     i = len(arr)+1
#     res = {arr[i] : i+1 for i,n in enumerate(arr)}
#     curr = 0
#     # while i!=2020:  ##part a
#     while i!=30000000:  ##part b
#         if curr in res:
#             prev = curr
#             curr = i-res[curr]
#             res[prev] = i
#         else:
#             res[curr] = i
#             curr = 0
#         i += 1
#     return curr

# Q 16 a. Find valid tickets
# def tickets(arr):
#     lo, hi, num, val = [], [], [], []
#     for x in arr:
#         if len(x) == 0:
#             break
#         l, h = x.split(" or ")
#         _, l = l.split(": ")
#         lo.append(int(l.split("-")[0]))
#         hi.append(int(l.split("-")[1]))
#         lo.append(int(h.split("-")[0]))
#         hi.append(int(h.split("-")[1]))
#     i = 0
#     for x in arr:
#         if "nearby ticket" in x:
#             break
#         i += 1
#     for j in range(i+1, len(arr)):
#         num.extend(arr[j].split(","))
#     num = [int(n) for n in num]
#     for l, h in zip(lo, hi):
#         for i, n in enumerate(num):
#             if n>=l and n<=h:
#                 val.append(n)
#     rem = [x for x in num if x not in val]
#     return sum(rem)

def tickets1(arr):
    d, n_tickets, y_tickets = dict(), [], []
    for x in arr:
        if len(x) == 0:
            break
        l, h = x.split(" or ")
        c, l = l.split(": ")
        d[c] = [[int(l.split("-")[0]), int(l.split("-")[1])], [int(h.split("-")[0]), int(h.split("-")[1])]]
    i = 0
    for x in arr:
        if "your ticket" in x:
            break
        i += 1
    y_tickets = arr[i+1].split(",")
    y_tickets = [int(p) for p in y_tickets]
    i = 0
    for x in arr:
        if "nearby ticket" in x:
            break
        i += 1
    for j in range(i+1, len(arr)):
        p = arr[j].split(",")
        n_tickets.append([int(j) for j in p])
    print(d, y_tickets, n_tickets)
    for i, y in enumerate(y_tickets):
        n_tickets[i].extend([y])
    classes = []
    for i in range(len(n_tickets)):
        temp = n_tickets[i]
        for k, v in d.items():
            t = []
            for r in v:
                for p in temp:
                    if p>=r[0] and p<=r[1]:
                        t.append(p)
            if sorted(t) == sorted(temp):
                classes.append(k)
                break
    print(classes)
    ids = [i for i, c in enumerate(classes) if "departure" in c]
    c = 1
    for i in ids[:6]:
        c *= y_tickets[i]
    return c


#Q18 a. Order of operators left to right priority
# def eval_operations(arr):
#     s = 0
#     ops = ['*', '+', '-', '/']
#     for x in arr:
#         eq = list(x)
#         eq = [p for p in eq if p!=" "]
#         st, prev = [], []
#         print(eq)
#         p = 0
#         curr = ""
#         while p!=len(eq):
#             st.append(eq[p])
#             if eq[p] == '(':
#                 prev.append(len(st)-1)
#             if eq[p] == ')':
#                 st.pop()
#                 curr = "".join(st[prev.pop()+1:p])
#                 print("now:", curr)
#                 while 1:
#                     c = st.pop()
#                     if c == "(":
#                         break
#                 ind = [i for i, k in enumerate(curr) if k in ops]
#                 if len(ind) > 1:
#                     t = str(eval(curr[:ind[1]]))
#                     print(t)
#                     for i in range(1, len(ind)-1):
#                         print(i, t, curr[ind[i]:ind[i+1]])
#                         t += curr[ind[i]:ind[i+1]]
#                         t = str(eval(t))
#                     t += curr[ind[-1]:]
#                     t = str(eval(t))
#                 else:
#                     print(curr)
#                     t = str(eval(curr))
#                 st.append(t)
#             print(p, curr, st, prev)
#             p += 1
#         if len(st) > 3:
#             print(st)
#             st = "".join(st)
#             ind = [i for i, k in enumerate(st) if k in ops]
#             t = str(eval(st[:ind[1]]))
#             print(ind, t)
#             for i in range(1, len(ind)-1):
#                 print(t)
#                 t += st[ind[i]:ind[i+1]]
#                 t = str(eval(t))
#             t += st[ind[-1]:]
#             t = str(eval(t))
#             s += int(t)            
#         else:
#             s += eval("".join(st))
#         print(x, s)
#     return s

# b. Do addition first before multiplication


# Q19 a. Use rules and find ones that match rule 0 --> NOT COMPLETED
# '''  Works for small test case correct answer and input case incorrect answer
# def update_value(d, s, seen):
#     temp = ""
#     s = s.split("-")
#     for j in range(len(s)):
#         if len(s[j]) == 0:
#             continue
#         if s[j] in seen and isinstance(d[s[j]], str) and isinstance(temp, str):
#             temp += d[s[j]]
#         elif s[j] in seen and isinstance(d[s[j]], list) and isinstance(temp, str):
#             t = []
#             for y in d[s[j]]:
#                 t.append(temp+y)
#             temp = t
#         elif s[j] in seen and isinstance(d[s[j]], list) and isinstance(temp, list):
#             temp1 = []
#             for t in temp:
#                 for y in d[s[j]]:
#                     temp1.append(t+y)
#             temp = temp1
#         elif s[j] not in seen and isinstance(temp, str):
#             c = Counter(s[j])
#             if not ('b' == "".join(sorted(c.keys())) or 'a' == "".join(sorted(c.keys())) or 'ab' == "".join(sorted(c.keys()))):
#                 temp += "-" + s[j] + "-"
#             else:
#                 temp += s[j]
#         elif s[j] not in seen and isinstance(temp, list):
#             t = []
#             for y in temp:
#                 c = Counter(s[j])
#                 if not ('b' == "".join(sorted(c.keys())) or 'a' == "".join(sorted(c.keys())) or 'ab' == "".join(sorted(c.keys()))):
#                     t.append(y+ "-" + s[j] + "-")
#                 else:
#                     t.append(y+s[j])
#             temp = t       
#     # print("New value:", s, temp)
#     return temp

# def update_seen(d, seen):
#     # print("Previous seen:", seen)
#     temp = []
#     for k, v in d.items():
#         if k in seen:
#             continue
#         else:
#             count = 0
#             for x in v:
#                 c = Counter(x)
#                 if ('b' == "".join(sorted(c.keys())) or 'a' == "".join(sorted(c.keys())) or 'ab' == "".join(sorted(c.keys()))):
#                     count += 1
#             if count == len(v):
#                 temp.append(k)
#     # print("Found new seen:", temp)
#     return temp

# def valid_strings(arr):
#     d = dict()
#     for x in arr:
#         k, v = x.split(":")
#         if len(v.split("|")) == 1:
#             d[k] = "-".join(v.strip().replace('"', "").split(" "))
#         else:
#             d[k] = [("-").join(y.strip().split(" ")) for y in v.split("|")]
#     d = dict(sorted(d.items(), key=lambda x:len(x[1])))
#     seen = []
#     for k, v in d.items():
#         c = Counter(v)
#         if ('b' == "".join(sorted(c.keys())) or 'a' == "".join(sorted(c.keys())) or 'ab' == "".join(sorted(c.keys()))):
#             seen.append(k)
#     # print(d, seen)
#     c1 = 0
#     while 1:
#         for k, v in d.items():
#             if k in seen:
#                 continue
#             else:
#                 if isinstance(v, list):
#                     for i, x in enumerate(v):
#                         for s in seen:
#                             if s in x.split("-"):
#                                 d[k][i] = update_value(d, x, seen)
#                     seen.extend(update_seen(d, seen))
#                     # print("Update seen:", k, seen)
#                     # print("Update value:", k, d[k])
#                 elif isinstance(v, str):
#                     d[k] = update_value(d, v, seen)
#                     seen.extend(update_seen(d, seen))
#                     # print("Update seen:", k, seen)
#                     # print("Update value:", k, d[k])
#                 flatten = lambda x1: [y1 for l1 in x1 for y1 in flatten(l1)] if type(x1) is list else [x1]
#                 if any(isinstance(z, list) for z in d[k]):
#                     # print("Flatten:", k, d[k])
#                     d[k] = flatten(d[k])
#             # print(k, d)
#         c1 += 1
#         if '0' in seen:
#             break
#     return d['0']
#     ## additional code insert in main ##
#     v = valid_strings(arr)
#     with open("input1", "r") as f:
#         total = f.readlines()
#     arr = []
#     for x in total:
#         arr.append(x.strip())
#     c = 0
#     for x in arr:
#         if x in v:
#             c += 1
#     print(c)
# '''


if __name__ == "__main__":
    with open("input", "r") as f:
        total = f.readlines()
    arr = []
    for x in total:
        arr.append(x.strip())
    print(tickets1(arr))