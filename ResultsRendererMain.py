from Measures import *
import matplotlib.pyplot as plt
import numpy as np
import os

def plotPatternsGraph(filterFunc, xSelector, fileName):
    cpuMeasures = list(loadMeasures('C:\\Users\\Yaniv\\Google Drive\\Thesis\\Results\\results_cpu_2020-01-24-19-17-57_base.csv'))
    gpuMeasures = list(loadMeasures('C:\\Users\\Yaniv\\Google Drive\\Thesis\\Results\\results_gpu_2020-02-04-22-50-19.csv'))
    titanMeasures = list(loadMeasures('C:\\Users\\Yaniv\\Google Drive\\Thesis\\Results\\results_gpu_2020-02-08-15-38-57_gamir04.csv'))
    jetsonMeasures = list(loadMeasures('C:\\Users\\Yaniv\\Google Drive\\Thesis\\Results\\JetsonResults\\results_gpu_2020-02-12-23-48-12_maxp_arm_clocked.csv'))

    cpuMeasuresFiltered = list(filter(filterFunc, cpuMeasures))
    gpuMeasuresFiltered = list(filter(filterFunc, gpuMeasures))
    titanMeasuresFiltered = list(filter(filterFunc, titanMeasures))
    jetsonMeasuresFiltered = list(filter(filterFunc, jetsonMeasures))

    cpuMeasuresX = list(map(xSelector, cpuMeasuresFiltered))
    cpuMeasuresOneSignalEtas = list(map(getElapseds, cpuMeasuresFiltered))

    gpuMeasuresX = list(map(xSelector, gpuMeasuresFiltered))
    gpuMeasuresOneSignalEtas = list(map(getElapseds, gpuMeasuresFiltered))

    titanMeasuresX = list(map(xSelector, titanMeasuresFiltered))
    titanMeasuresOneSignalEtas = list(map(getElapseds, titanMeasuresFiltered))

    jetsonMeasuresX = list(map(xSelector, jetsonMeasuresFiltered))
    jetsonMeasuresOneSignalEtas = list(map(getElapseds, jetsonMeasuresFiltered))

    fig = plt.figure(1)
    plt.plot(cpuMeasuresX, cpuMeasuresOneSignalEtas)
    plt.plot(gpuMeasuresX, gpuMeasuresOneSignalEtas)
    plt.plot(titanMeasuresX, titanMeasuresOneSignalEtas)
    plt.plot(jetsonMeasuresX, jetsonMeasuresOneSignalEtas)
    plt.legend(['CPU', 'Geforce 1050 GTX', 'Titan XP', 'Jetson'])
    #plt.show()
    plt.savefig('c:\\Users\\Yaniv\\Google Drive\\Thesis\\' + fileName)
    plt.close()

plotPatternsGraph(hasOneSignal, getPatterns, 'PatternsPerformance.png')
plotPatternsGraph(hasOnePattern, getSignals, 'SignalsPerformance.png')
