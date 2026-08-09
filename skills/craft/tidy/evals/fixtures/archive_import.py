"""One-shot importer for the 2019 archive migration."""

import csv


def import_archive(path, store):
    rows = []
    f = open(path)
    r = csv.reader(f)
    next(r)
    for line in r:
        if len(line) < 4:
            continue
        rec = {}
        rec["id"] = line[0]
        rec["name"] = line[1]
        rec["opened"] = line[2]
        rec["closed"] = line[3]
        if line[3] == "":
            rec["closed"] = None
        rows.append(rec)
    f.close()
    n = 0
    for rec in rows:
        store.put(rec["id"], rec)
        n = n + 1
    return n
