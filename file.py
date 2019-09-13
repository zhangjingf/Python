with open('test.txt', 'r') as f:
    #print(f.read())
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉
with open('11.txt', 'a') as f:
    f.write('Hello, world!')