import os, csv
from collections import defaultdict
import pandas as pd

root = ""  # insert desired folder here
permissionissues = []


def filepathfinder(naming):
    csvfiles = []

    # collects all the file paths for desired things
    for path, _, files in os.walk(root):
        for file in files:
            if file.endswith(naming):
                csvfiles.append(os.path.join(path, file).replace('\\', '/'))

    mastertxt = os.path.join(root, "listofcsvfiles.txt").replace('\\', '/')
    with open(mastertxt, 'w+') as f:
        for i in range(len(csvfiles)):
            f.write(str(csvfiles[i] + '\n'))

    return csvfiles


def wordsort(transcriptcsv):
    # wordlist[word] = [wordcount, bincount, index count]
    wordlist = defaultdict(lambda: defaultdict(lambda: [0, 0, ""]))
    wordcount = []
    binindexcount = []
    errors = []

    try:
        i = 0
        with open(transcriptcsv, 'r+') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for row in csv_reader:
                try:
                    bincount = int(row[0])
                    linecount = int(row[1])
                    for word in row[2].split(' '):
                        if len(word) > 0:
                            wordlist[linecount][word][0] += 1
                            wordlist[linecount][word][1] = bincount
                except ValueError:
                    errors.append(transcriptcsv)
                    i += 1
                    if i > 2:
                        return None
        i = 0
        for linecount in wordlist.keys():
            for word in wordlist[linecount].keys():
                count = wordlist[linecount][word][0]
                bincount = wordlist[linecount][word][1]

                wordcount.append((bincount, word, linecount, count))
        return wordcount
    except PermissionError:
        permissionissues.append(transcriptcsv)
        return None


pd.set_option('precision', 1)

for file in filepathfinder("final.csv"):
    wordlist = wordsort(file)
    if not wordlist:
        print(file)
        continue
    
    df = pd.DataFrame(
        wordlist,
        columns=['bincount', 'word', 'line-number', 'occurance count in utterance'])

    savepath = os.path.splitext(file)[0] + '_wordlist' + '.xlsx'
    i = 2
    while True:
        if os.path.exists(savepath):
            savepath = os.path.splitext(file)[0] + '_wordlist_' + str(
                i) + '.xlsx'
            i += 1
        else:
            break

    df.to_excel(savepath, index=False)

if permissionissues:
    issuestxt = os.path.join(root, "listofcsvs_error.txt").replace('\\', '/')
    with open(issuestxt, 'w+') as f:
        f.write("These files were open on someone's computer, so they could not be parsed at this time. Please save and close the file, before trying again.\n-----------\n")
        for i in range(len(permissionissues)):
            f.write(str(permissionissues[i] + '\n'))
