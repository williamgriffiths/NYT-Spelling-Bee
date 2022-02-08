def remove_dupes(file1):
    lines_seen = set()

    with open(file1,"r") as f:
        with open("allwords2.txt", "r+") as g:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i not in lines_seen:
                    g.write(i)
                    lines_seen.add(i)
            g.truncate()