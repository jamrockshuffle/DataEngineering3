import boto3
import glob
import os
import json
import csv
import flatten_json
import pathlib

def main():
    for i in glob.glob("data/**/*.json", recursive=True):
        f = open(i, "r")
        data = json.loads(f.read())
        flat_data = flatten_json.flatten(data, "_")

        if not os.path.exists("data/csv"):
            os.mkdir("data/csv")

        fl = open('data/csv/'+pathlib.Path(i).stem+'.csv', 'a')

        with open('data/csv/'+pathlib.Path(i).stem+'.csv', 'w', newline='') as x:
            w = csv.DictWriter(x, flat_data.keys())
            w.writeheader()
            w.writerow(flat_data)
    pass


if __name__ == "__main__":
    main()
