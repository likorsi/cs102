# a version of word frequency example from mapreduce tutorial

def mapper(doc):
    # input reader and map function are combined
    import os
    print(os.getcwd())
    words = []
    with open(os.path.join('/Users/Лидия/cs102/h10/tmp', doc)) as fd:
        for line in fd:
            words.extend((word.lower(), 1) for word in line.split() \
                         if len(word) > 3)
    return words

def reducer(words):
    # we should generate sorted lists which are then merged,
    # but to keep things simple, we use dicts
    word_count = {}
    for word, count in words:
        if word not in word_count:
            word_count[word] = 0
        word_count[word] += count
    # print('reducer: %s to %s' % (len(words), len(word_count)))
    return word_count

if __name__ == '__main__':
    import dispy, logging
    import os
    #map_cluster = dispy.SharedJobCluster(mapper,nodes=['*'], scheduler_node="192.168.43.181")
    map_cluster = dispy.JobCluster(mapper)
    reduce_cluster = dispy.JobCluster(reducer)
    map_jobs = []
    for f in ['doc1', 'doc2', 'doc3', 'doc4', 'doc5']:
        job = map_cluster.submit(f)
        map_jobs.append(job)
    reduce_jobs = []
    for map_job in map_jobs:
        words = map_job()
        if not words:
            print(map_job.exception)
            continue
        # simple partition
        n = 0
        while n < len(words):
            m = min(len(words) - n, 1000)
            reduce_job = reduce_cluster.submit(words[n:n+m])
            reduce_jobs.append(reduce_job)
            n += m
    # reduce
    word_count = {}
    for reduce_job in reduce_jobs:
        words = reduce_job()
        if not words:
            print(reduce_job.exception)
            continue
        for word, count in words.items():
            if word not in word_count:
                word_count[word] = 0
            word_count[word] += count
    # sort words by frequency and print
    for word in sorted(word_count, key=lambda x: word_count[x], reverse=True):
        count = word_count[word]
        print(word, count)
    reduce_cluster.print_status()
