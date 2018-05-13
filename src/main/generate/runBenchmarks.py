import os
import subprocess

""" 
Contains structures for the experiment(s):
    Experiment
        -> Benchmark
            -> Result (contains all measurements required for the different configs(heapSize)   
"""


class Result:

    def __init__(self, heapSize, bench_id):
        # Configs
        self.heapSize = heapSize
        self.bench_id = bench_id

        # Measurement
        self.time = -1
        self.majorC = -1
        self.minorC = -1
        self.majorAvgT = -1
        self.minorAvgT = -1
        self.majorTotalT = -1
        self.minorTotalT = -1


class Benchmark:

    def __init__(self, name):
        self.name = name
        self.appTime = -1
        self.results = []

    def makeResult(self, heapSize, bench_id):
        self.results.append(Result(heapSize, bench_id))

    def addResult(self, result):
        self.results.append(result)

    def setAppTime(self, appTime):
        self.appTime = appTime

    def getAppTime(self):
        return self.appTime

    def getName(self):
        return self.name


class Experiment:

    def __init__(self, experiment, jvm, gcType):
        self.experiment = experiment
        self.jvm = jvm
        self.gcType = gcType

        self.benchmarks = []

    def addBenchmark(self, benchmark):
        self.benchmarks.append(benchmark)

    def getBenchmark(self):
        return benchmark


experiment1 = Experiment("exp1", "jvm1", "gc1")

for bench in range(1, 12):

    benchmark = Benchmark("bench" + str(bench))
    for heapSize in range(1, 11):
        benchmark.makeResult(heapSize * 50, bench)

    experiment1.addBenchmark(benchmark)

for bench in range(0, 11):

    print "Bench: ", experiment1.benchmarks[bench].name

    for result in experiment1.benchmarks[bench].results:
        print "-- result-heap: ", result.heapSize, " with id: ", result.bench_id
