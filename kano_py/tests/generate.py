import os
import random
from kano.model import *

class ConfigFiles:
    def __init__(self, podN=100,nsN=5,policyN=50,podLL=5,nsLL=5,keyL=5,valueL=10,userL=5,selectedLL=3,allowNSLL=3,allowpodLL=3):
        self.podN = podN
        self.nsN = nsN
        self.policyN = policyN
        self.podLL = podLL
        self.nsLL = nsLL
        self.keys = ["key"+str(i) for i in range(keyL)]
        self.values = ["value"+str(i) for i in range(valueL)]
        self.userL = userL
        self.selectedLL = selectedLL
        self.allowNSLL = allowNSLL
        self.allowpodLL = allowpodLL
        self.generatePods()
        self.generateNamespaces()

    def generatePods(self):
        containers = []
        for i in range(self.podN):
            podName = "pod" + str(i)
            # nsName = random.choice(namespaces)
            labels = {}
            for l in range(random.randint(0, self.podLL-1)):
                labels[random.choice(self.keys)] = random.choice(self.values)
            pod = Container(podName, labels)
            containers.append(pod)
        self.containers = containers
        return


    # def generateNamespaces(self):
    #     namespaces = []
    #     for i in range(self.nsN):
    #         nsName = "namespace" + str(i)
    #         labels = {}
    #         for l in range(random.randint(0, self.nsLL-1)):
    #             labels[random.choice(self.keys)] = random.choice(self.values)
    #         ns = Namespace(nsName, labels)
    #         namespaces.append(ns)
    #     self.namespaces = namespaces
    #     return


    def generateConfigFiles(self):
        return


    def getPods(self):
        return self.containers


    # def getNamespaces(self):
    #     return self.namespaces
