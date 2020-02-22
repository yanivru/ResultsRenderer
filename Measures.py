import os

def getAllCsvFiles(path):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

    return files

class Measure:
    signals = 0
    patterns = 0
    elapsed = 0

def hasOneSignal(measure):
    return measure.signals == 1

def hasOnePattern(measure):
    return measure.patterns == 1

def getPatterns(measure):
    return measure.patterns

def getSignals(measure):
    return measure.signals

def getElapseds(measure):
    return measure.elapsed

def loadMeasures(filePath):
    file1 = open(filePath, 'rb')

    csv = file1.readlines()

    measures = []

    i = iter(csv)
    next(i)
    for x in i:
        values = x.decode("utf-8").split(",", -1)
        measure = Measure()
        measure.signals = float(values[0])
        measure.patterns = float(values[1])
        measure.elapsed = float(values[2])

        measures.append(measure)

    return measures