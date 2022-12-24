def parse(filename):
    d={}
    with open(filename) as f:
        for line in f:
            src, dest, weigh = line.split(',')
            if src in d:
                d[src][dest] = int(weigh)
            else:
                d[src] = {dest : int(weigh)}
    return d 

print(parse('graph.csv'))

