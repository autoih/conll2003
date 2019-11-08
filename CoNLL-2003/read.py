
filepath = 'eng_train.txt'
with open(filepath) as fp:
    
    content = fp.read().splitlines()
    for cnt, line in enumerate(content):
        print(type(line))

#        print(line[0])
#        print(line[-1])
        print("Line {}: {}".format(cnt, line))
        if cnt ==10:
            break

