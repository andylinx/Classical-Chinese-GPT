import re
word_dic={}
with open('output.txt', 'r') as file:
    for line in file:
        split_points = [match.start() for match in re.finditer(r'\d+', line)]
        split_points.append(len(line))
        start = 0
        pos=1
        word=""
        for point in split_points:
            substring = line[start:point]
            if len(substring)>=1:
                if pos==1:
                    word=substring[-1]
                    pos=0
                    word_dic.setdefault(word, [])
                else:
                    word_dic[word].append(substring)
            start = point
for key, value in word_dic.items():
    print(key + ":")
    for item in value:
        print(item)
    print()