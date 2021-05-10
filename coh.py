#!/usr/bin/env python
# visit http://tool.lu/pyc/ for more information
import numpy as np
from abaqus import *
from abaqusConstants import *
from itertools import *

class cohesive_insert:
    skip = 100000000
    nodes_states = { }
    elements_num = 0
    converttomeshpart = 0
    interface_nodes_label_dir = { }
    interface_nodes_label_lis = []
    
    def __init__(self, Part, Sets):
        self.part = Part
        self.sets = Sets.split(',')
        vpName = session.currentViewportName
        self.model = session.sessionState[vpName]['modelName']
        self.max_nodes_length = len(str(len(mdb.models[self.model].parts[self.part].nodes)))
        self.nodeskip = 10 ** self.max_nodes_length

    
    def convertToMeshpart(self):
        p = mdb.models[self.model].parts[self.part]
        
        try:
            p.PartFromMesh(name = self.part + '-mesh', copySets = True)
        except:
            print 'error'

        mdb.models[self.model].parts.changeKey(fromName = self.part, toName = self.part + '-original')
        mdb.models[self.model].parts.changeKey(fromName = self.part + '-mesh', toName = self.part)
        p = mdb.models[self.model].parts[self.part]
        cohesive_insert.elements_num = len(p.elements)

    
    def copyNodes_2D_Inner_edge(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectSets = sets.split(';')[1:]
            objectEdgeNodesLabelSet_dir = { }
            for objectsetName in objectSets:
                objectEdgeNodesLabelSet_dir[objectsetName] = []
            
            missionNodesLabelSet = []
            for i in p.sets[setName].nodes:
                missionNodesLabelSet.append(i.label)
                i_copy_times = 0
                for j in i.getElements():
                    if j in p.sets[setName].elements:
                        i_copy_times += 1
                        continue
                if i_copy_times == len(i.getElements()):
                    i_copy_times = i_copy_times - 1
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'edge',
                        'usecode': 0 }
                else:
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'inner',
                        'usecode': 1 }
                    for objectsetName in objectSets:
                        if i in p.sets[objectsetName].nodes and i.label not in objectEdgeNodesLabelSet_dir[objectsetName]:
                            objectEdgeNodesLabelSet_dir[objectsetName].append(i.label)
                            continue
                for k in range(1, i_copy_times + 1):
                    p.Node(i.coordinates, None, k * self.nodeskip + i.label)
                
            
            p.SetFromNodeLabels(name = 'Nset-' + setName, nodeLabels = tuple(missionNodesLabelSet))
            for objectsetName in objectSets:
                p.SetFromNodeLabels(name = 'Nset-interface-' + setName + '-' + objectsetName, nodeLabels = tuple(objectEdgeNodesLabelSet_dir[objectsetName]))
            
        

    
    def copyNodes_2D_Inner(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectSets = sets.split(';')[1:]
            objectEdgeNodesLabelSet_dir = { }
            for objectsetName in objectSets:
                objectEdgeNodesLabelSet_dir[objectsetName] = []
            
            missionNodesLabelSet = []
            for i in p.sets[setName].nodes:
                missionNodesLabelSet.append(i.label)
                i_copy_times = 0
                for j in i.getElements():
                    if j in p.sets[setName].elements:
                        i_copy_times += 1
                        continue
                if i_copy_times == len(i.getElements()):
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'edge',
                        'usecode': 0 }
                else:
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'inner',
                        'usecode': 1 }
                    for objectsetName in objectSets:
                        if i in p.sets[objectsetName].nodes and i.label not in objectEdgeNodesLabelSet_dir[objectsetName]:
                            objectEdgeNodesLabelSet_dir[objectsetName].append(i.label)
                            continue
                for k in range(1, i_copy_times + 1):
                    p.Node(i.coordinates, None, k * self.nodeskip + i.label)
                
            
            p.SetFromNodeLabels(name = 'Nset-' + setName, nodeLabels = tuple(missionNodesLabelSet))
            for objectsetName in objectSets:
                p.SetFromNodeLabels(name = 'Nset-interface-' + setName + '-' + objectsetName, nodeLabels = tuple(objectEdgeNodesLabelSet_dir[objectsetName]))
            
        

    
    def copyNodes_3D_Inner_edge(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectSets = sets.split(';')[1:]
            objectEdgeNodesLabelSet_dir = { }
            for objectsetName in objectSets:
                objectEdgeNodesLabelSet_dir[objectsetName] = []
            
            missionNodesLabelSet = []
            for i in p.sets[setName].nodes:
                missionNodesLabelSet.append(i.label)
                i_copy_times = 0
                for j in i.getElements():
                    if j in p.sets[setName].elements:
                        i_copy_times += 1
                        continue
                if i_copy_times == len(i.getElements()):
                    i_copy_times = i_copy_times - 1
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'edge',
                        'usecode': 0 }
                else:
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'inner',
                        'usecode': 1 }
                    for objectsetName in objectSets:
                        if i in p.sets[objectsetName].nodes and i.label not in objectEdgeNodesLabelSet_dir[objectsetName]:
                            objectEdgeNodesLabelSet_dir[objectsetName].append(i.label)
                            continue
                for k in range(1, i_copy_times + 1):
                    p.Node(i.coordinates, None, k * self.nodeskip + i.label)
                
            
            p.SetFromNodeLabels(name = 'Nset-' + setName, nodeLabels = tuple(missionNodesLabelSet))
            for objectsetName in objectSets:
                p.SetFromNodeLabels(name = 'Nset-interface-' + setName + '-' + objectsetName, nodeLabels = tuple(objectEdgeNodesLabelSet_dir[objectsetName]))
            
        

    
    def copyNodes_3D_Inner(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectSets = sets.split(';')[1:]
            objectEdgeNodesLabelSet_dir = { }
            for objectsetName in objectSets:
                objectEdgeNodesLabelSet_dir[objectsetName] = []
            
            missionNodesLabelSet = []
            for i in p.sets[setName].nodes:
                missionNodesLabelSet.append(i.label)
                i_copy_times = 0
                for j in i.getElements():
                    if j in p.sets[setName].elements:
                        i_copy_times += 1
                        continue
                if i_copy_times == len(i.getElements()):
                    i_copy_times = i_copy_times - 1
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'edge',
                        'usecode': 0 }
                else:
                    cohesive_insert.nodes_states[i.label] = {
                        'location': 'inner',
                        'usecode': 1 }
                    for objectsetName in objectSets:
                        if i in p.sets[objectsetName].nodes and i.label not in objectEdgeNodesLabelSet_dir[objectsetName]:
                            objectEdgeNodesLabelSet_dir[objectsetName].append(i.label)
                            continue
                for k in range(1, i_copy_times + 1):
                    p.Node(i.coordinates, None, k * self.nodeskip + i.label)
                
            
            p.SetFromNodeLabels(name = 'Nset-' + setName, nodeLabels = tuple(missionNodesLabelSet))
            for objectsetName in objectSets:
                p.SetFromNodeLabels(name = 'Nset-interface-' + setName + '-' + objectsetName, nodeLabels = tuple(objectEdgeNodesLabelSet_dir[objectsetName]))
            
        

    
    def copyNodes_2D_Interface(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            nodesset1 = set([ i.label for i in p.sets[setName1].nodes ])
            nodesset2 = set([ i.label for i in p.sets[setName2].nodes ])
            interface_nodes_set = nodesset1 & nodesset2
            for i in interface_nodes_set:
                node = p.nodes.getFromLabel(i)
                p.Node(node.coordinates, None, node.label + self.nodeskip)
            
            interface_nodes_label = tuple(interface_nodes_set)
            p.SetFromNodeLabels(name = 'Nset-interface-' + setName1 + '-' + setName2, nodeLabels = interface_nodes_label)
            cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2] = interface_nodes_label
        

    
    def copyNodes_3D_Interface(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            nodesset1 = set([ i.label for i in p.sets[setName1].nodes ])
            nodesset2 = set([ i.label for i in p.sets[setName2].nodes ])
            interface_nodes_set = nodesset1 & nodesset2
            for i in interface_nodes_set:
                node = p.nodes.getFromLabel(i)
                p.Node(node.coordinates, None, node.label + self.nodeskip)
            
            interface_nodes_label = tuple(interface_nodes_set)
            p.SetFromNodeLabels(name = 'Nset-interface-' + setName1 + '-' + setName2, nodeLabels = interface_nodes_label)
            cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2] = interface_nodes_label
        

    
    def copyNodes_2D_Multiple(self):
        p = mdb.models[self.model].parts[self.part]
        unionsetName = 'Unionset'
        setNames = self.sets[0].split(';')
        nodeslabelset_dir = { }
        for i in setNames:
            nodeslabelset_dir[i] = set([ node.label for node in p.sets[i].nodes ])
        
        sets = [ p.sets[i] for i in setNames ]
        p.SetByBoolean(name = unionsetName, sets = tuple(sets))
        sets_combinations = list(combinations(setNames, 2))
        for i in p.sets[unionsetName].nodes:
            i_copy_times = 0
            for j in i.getElements():
                if j in p.sets[unionsetName].elements:
                    i_copy_times += 1
                    continue
            if i_copy_times == len(i.getElements()):
                i_copy_times = i_copy_times - 1
                cohesive_insert.nodes_states[i.label] = {
                    'location': 'edge',
                    'usecode': 0 }
            else:
                cohesive_insert.nodes_states[i.label] = {
                    'location': 'inner',
                    'usecode': 1 }
            for k in range(1, i_copy_times + 1):
                p.Node(i.coordinates, None, k * self.nodeskip + i.label)
            
        
        for combination in sets_combinations:
            interface_nodes_set = set(nodeslabelset_dir[combination[0]]) & set(nodeslabelset_dir[combination[1]])
            p.SetFromNodeLabels(name = 'Nset-interface-' + combination[0] + '-' + combination[1], nodeLabels = tuple(interface_nodes_set))
        

    
    def copyNodes_3D_Multiple(self):
        p = mdb.models[self.model].parts[self.part]
        unionsetName = 'Unionset'
        setNames = self.sets[0].split(';')
        nodeslabelset_dir = { }
        for i in setNames:
            nodeslabelset_dir[i] = set([ node.label for node in p.sets[i].nodes ])
        
        sets = [ p.sets[i] for i in setNames ]
        p.SetByBoolean(name = unionsetName, sets = tuple(sets))
        sets_combinations = list(combinations(setNames, 2))
        for i in p.sets[unionsetName].nodes:
            i_copy_times = 0
            for j in i.getElements():
                if j in p.sets[unionsetName].elements:
                    i_copy_times += 1
                    continue
            if i_copy_times == len(i.getElements()):
                i_copy_times = i_copy_times - 1
                cohesive_insert.nodes_states[i.label] = {
                    'location': 'edge',
                    'usecode': 0 }
            else:
                cohesive_insert.nodes_states[i.label] = {
                    'location': 'inner',
                    'usecode': 1 }
            for k in range(1, i_copy_times + 1):
                p.Node(i.coordinates, None, k * self.nodeskip + i.label)
            
        
        for combination in sets_combinations:
            interface_nodes_set = set(nodeslabelset_dir[combination[0]]) & set(nodeslabelset_dir[combination[1]])
            p.SetFromNodeLabels(name = 'Nset-interface-' + combination[0] + '-' + combination[1], nodeLabels = tuple(interface_nodes_set))
        

    
    def updateElements_2D_Inner_edge_TRI3(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                updatenodes = []
                for j in i.connectivity:
                    updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                    cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = TRI3, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                    (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                    (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label)]
                for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                    if j in p.sets[setName].elements:
                        n = [
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label)]
                    else:
                        n = [
                            (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                            (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                            (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label)]
                    for k in m:
                        for l in n:
                            set_k = set(np.array(k) % self.nodeskip)
                            set_l = set(np.array(l) % self.nodeskip)
                            if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                                cohesive_insert.elements_num += 1
                                if set_k.issubset(Integral_cohesiveEdgeNodesSet):
                                    for objectsetName in objectsets:
                                        if set_k.issubset(cohesiveEdgeNodesSet_dir[objectsetName]):
                                            cohesiveEdgeElementLabel_dir[objectsetName].append(cohesive_insert.elements_num)
                                            continue
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                                else:
                                    cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                            
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            for objectsetName in objectsets:
                p.SetFromElementLabels(name = 'Elset-' + objectsetName + '_edge_cohesive', elementLabels = tuple(cohesiveEdgeElementLabel_dir[objectsetName]))
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
        

    
    def updateElements_2D_Inner_TRI3(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                elementnodesset = set([ node.label for node in i.getNodes() ])
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) < 2:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                        cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                    
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) == 2:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        if p.nodes[j].label not in Integral_cohesiveEdgeNodesSet:
                            updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                            cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                            continue
                        updatenodes.append(p.nodes[j])
                    
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = TRI3, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                    (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                    (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label)]
                for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                    if j in p.sets[setName].elements:
                        n = [
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label)]
                    else:
                        n = [
                            (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                            (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                            (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label)]
                    for k in m:
                        for l in n:
                            set_k = set(np.array(k) % self.nodeskip)
                            set_l = set(np.array(l) % self.nodeskip)
                            if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                                cohesive_insert.elements_num += 1
                                if set_k.issubset(Integral_cohesiveEdgeNodesSet):
                                    pass
                                else:
                                    cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                            
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
        

    
    def updateElements_3D_Inner_edge_TET4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                updatenodes = []
                for j in i.connectivity:
                    updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                    cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = TET4, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                for objectsetName in objectsets:
                                    if set_yu_k.issubset(cohesiveEdgeNodesSet_dir[objectsetName]):
                                        cohesiveEdgeElementLabel_dir[objectsetName].append(cohesive_insert.elements_num)
                                        continue
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_k)
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_yu_k)
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            for objectsetName in objectsets:
                p.SetFromElementLabels(name = 'Elset-' + objectsetName + '_edge_cohesive', elementLabels = tuple(cohesiveEdgeElementLabel_dir[objectsetName]))
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
        

    
    def updateElements_3D_Inner_TET4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                elementnodesset = set([ node.label for node in i.getNodes() ])
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) < 3:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                        cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                    
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) == 3:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        if p.nodes[j].label not in Integral_cohesiveEdgeNodesSet:
                            updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                            cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                            continue
                        updatenodes.append(p.nodes[j])
                    
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = TET4, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                pass
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_yu_k)
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
        

    
    def updateElements_3D_Inner_WEDGE(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                elementnodesset = set([ node.label for node in i.getNodes() ])
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) < 3:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                        cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                    
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) >= 3:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        if p.nodes[j].label not in Integral_cohesiveEdgeNodesSet:
                            updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                            cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                            continue
                        updatenodes.append(p.nodes[j])
                    
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = WEDGE6, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                    (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                pass
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                if len(set_yu_k) == 3:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                if len(set_yu_k) == 4:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
        

    
    def updateElements_3D_Inner_edge_WEDGE(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                updatenodes = []
                for j in i.connectivity:
                    updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                    cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = WEDGE6, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                    (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                for objectsetName in objectsets:
                                    if set_yu_k.issubset(cohesiveEdgeNodesSet_dir[objectsetName]):
                                        cohesiveEdgeElementLabel_dir[objectsetName].append(cohesive_insert.elements_num)
                                        continue
                                if len(set_yu_k) == 3:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                if len(set_yu_k) == 4:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                if len(set_yu_k) == 3:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                if len(set_yu_k) == 4:
                                    p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_yu_k)
                                
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            for objectsetName in objectsets:
                p.SetFromElementLabels(name = 'Elset-' + objectsetName + '_edge_cohesive', elementLabels = tuple(cohesiveEdgeElementLabel_dir[objectsetName]))
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
        

    
    def updateElements_2D_Inner_edge_QUAD4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                updatenodes = []
                for j in i.connectivity:
                    updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                    cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = QUAD4, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                    (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                    (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label),
                    (i.getElemEdges()[3].getNodes()[0].label, i.getElemEdges()[3].getNodes()[1].label)]
                for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                    if j in p.sets[setName].elements:
                        n = [
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[1].label)]
                    else:
                        n = [
                            (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                            (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                            (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label),
                            (j.getElemEdges()[3].getNodes()[0].label, j.getElemEdges()[3].getNodes()[1].label)]
                    for k in m:
                        for l in n:
                            set_k = set(np.array(k) % self.nodeskip)
                            set_l = set(np.array(l) % self.nodeskip)
                            if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                                cohesive_insert.elements_num += 1
                                if set_k.issubset(Integral_cohesiveEdgeNodesSet):
                                    for objectsetName in objectsets:
                                        if set_k.issubset(cohesiveEdgeNodesSet_dir[objectsetName]):
                                            cohesiveEdgeElementLabel_dir[objectsetName].append(cohesive_insert.elements_num)
                                            continue
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                                else:
                                    cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                            
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            for objectsetName in objectsets:
                p.SetFromElementLabels(name = 'Elset-' + objectsetName + '_edge_cohesive', elementLabels = tuple(cohesiveEdgeElementLabel_dir[objectsetName]))
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
        

    
    def updateElements_2D_Inner_QUAD4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                elementnodesset = set([ node.label for node in i.getNodes() ])
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) < 2:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                        cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                    
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) == 2:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        if p.nodes[j].label not in Integral_cohesiveEdgeNodesSet:
                            updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                            cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                            continue
                        updatenodes.append(p.nodes[j])
                    
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = QUAD4, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                    (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                    (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label),
                    (i.getElemEdges()[3].getNodes()[0].label, i.getElemEdges()[3].getNodes()[1].label)]
                for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                    if j in p.sets[setName].elements:
                        n = [
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label),
                            (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[1].label)]
                    else:
                        n = [
                            (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                            (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                            (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label),
                            (j.getElemEdges()[3].getNodes()[0].label, j.getElemEdges()[3].getNodes()[1].label)]
                    for k in m:
                        for l in n:
                            set_k = set(np.array(k) % self.nodeskip)
                            set_l = set(np.array(l) % self.nodeskip)
                            if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                                cohesive_insert.elements_num += 1
                                if set_k.issubset(Integral_cohesiveEdgeNodesSet):
                                    pass
                                else:
                                    cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                    p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                                    cohesiveNodesSetsList.append(set_k)
                            
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
        

    
    def updateElements_3D_Inner_edge_HEX8(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                updatenodes = []
                for j in i.connectivity:
                    updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                    cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = HEX8, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label, i.getElemFaces()[0].getNodes()[3].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label, i.getElemFaces()[1].getNodes()[3].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                    (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label),
                    (i.getElemFaces()[5].getNodes()[0].label, i.getElemFaces()[5].getNodes()[1].label, i.getElemFaces()[5].getNodes()[2].label, i.getElemFaces()[5].getNodes()[3].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                for objectsetName in objectsets:
                                    if set_yu_k.issubset(cohesiveEdgeNodesSet_dir[objectsetName]):
                                        cohesiveEdgeElementLabel_dir[objectsetName].append(cohesive_insert.elements_num)
                                        continue
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_yu_k)
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_yu_k)
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            for objectsetName in objectsets:
                p.SetFromElementLabels(name = 'Elset-' + objectsetName + '_edge_cohesive', elementLabels = tuple(cohesiveEdgeElementLabel_dir[objectsetName]))
            
        

    
    def updateElements_3D_Inner_HEX8(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            setName = sets.split(';')[0]
            objectsets = sets.split(';')[1:]
            cohesiveNodesSetsList = []
            cohesiveEdgeNodesSet_dir = { }
            cohesiveEdgeElementLabel_dir = { }
            Integral_cohesiveEdgeNodesSet = set()
            
            try:
                for objectsetName in objectsets:
                    cohesiveEdgeElementLabel_dir[objectsetName] = []
                    cohesiveEdgeNodesSet_dir[objectsetName] = set([ i.label for i in p.sets['Nset-interface-' + setName + '-' + objectsetName].nodes ])
                    Integral_cohesiveEdgeNodesSet = Integral_cohesiveEdgeNodesSet | cohesiveEdgeNodesSet_dir[objectsetName]
            except:
                pass

            missionElementsLabelSet = []
            cohesiveElementsLabelSet = []
            for i in p.sets[setName].elements:
                elementnodesset = set([ node.label for node in i.getNodes() ])
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) < 4:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                        cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                    
                if len(elementnodesset & Integral_cohesiveEdgeNodesSet) == 4:
                    missionElementsLabelSet.append(i.label + cohesive_insert.skip)
                    updatenodes = []
                    for j in i.connectivity:
                        if p.nodes[j].label not in Integral_cohesiveEdgeNodesSet:
                            updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                            cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
                            continue
                        updatenodes.append(p.nodes[j])
                    
                nodes = tuple(updatenodes)
                p.Element(nodes = nodes, elemShape = HEX8, label = cohesive_insert.skip + i.label)
            
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(missionElementsLabelSet))
            for i in p.sets['Elset-' + setName].elements:
                m = [
                    (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label, i.getElemFaces()[0].getNodes()[3].label),
                    (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label, i.getElemFaces()[1].getNodes()[3].label),
                    (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                    (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                    (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label),
                    (i.getElemFaces()[5].getNodes()[0].label, i.getElemFaces()[5].getNodes()[1].label, i.getElemFaces()[5].getNodes()[2].label, i.getElemFaces()[5].getNodes()[3].label)]
                adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
                for j in adjacent_local_elements:
                    if j in p.sets[setName].elements:
                        new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                    else:
                        new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                    new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                    new_element_nodes_set = set(new_element_nodes_lis)
                    new_element_nodes_dir = { }
                    for node in new_element_nodes_lis:
                        new_element_nodes_dir[node % self.nodeskip] = node
                    
                    for k in m:
                        set_yu_k = set(np.array(k) % self.nodeskip)
                        set_k = set(k)
                        if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            if set_yu_k.issubset(Integral_cohesiveEdgeNodesSet):
                                pass
                            else:
                                cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                                p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                                cohesiveNodesSetsList.append(set_yu_k)
                        
                    
                
            
            for i in missionElementsLabelSet:
                p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
            
            for i in p.sets['Elset-' + setName].elements:
                i.setValues(i.label - cohesive_insert.skip)
            
            p.SetFromElementLabels(name = 'Elset-' + setName + '_inner_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
        

    
    def updateElements_2D_Interface_TRI3(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            setsElementLabellis_dir = { }
            setsElementLabellis_dir[setName1] = [ i.label for i in p.sets[setName1].elements ]
            setsElementLabellis_dir[setName2] = [ i.label for i in p.sets[setName2].elements ]
            interface_nodes_label = cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2]
            cohesiveNodesSetsList = []
            interface_elements_label_list = []
            cohesiveElementsLabelSet = []
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElements():
                    if j in p.sets[setName1].elements and p.elements.getFromLabel(j.label + cohesive_insert.skip) is None:
                        nodes_label = [ p.nodes[l].label for l in j.connectivity ]
                        for k in nodes_label:
                            index_k = nodes_label.index(k)
                            if k in interface_nodes_label:
                                nodes_label[index_k] += self.nodeskip
                                continue
                        p.Element(nodes = (p.nodes.getFromLabel(nodes_label[0]), p.nodes.getFromLabel(nodes_label[1]), p.nodes.getFromLabel(nodes_label[2])), elemShape = TRI3, label = j.label + cohesive_insert.skip)
                        interface_elements_label_list.append(j.label)
                        continue
            
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElemEdges():
                    edge_nodes_set = set([ k.label for k in j.getNodes() ])
                    if edge_nodes_set.issubset(interface_nodes_label) and edge_nodes_set not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        cohesiveNodesSetsList.append(edge_nodes_set)
                        (node1, node2) = j.getNodes()
                        cohesive_nodes = (node1, node2, p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node1.label + self.nodeskip))
                        p.Element(nodes = cohesive_nodes, elemShape = QUAD4, label = cohesive_insert.elements_num)
                        cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        continue
            
            for i in interface_elements_label_list:
                p.deleteElement(p.elements.getFromLabel(i))
                p.elements.getFromLabel(i + cohesive_insert.skip).setValues(i)
            
            p.SetFromElementLabels(name = 'Elset-' + setName1 + '-' + setName2 + '-interface_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName1, elementLabels = tuple(setsElementLabellis_dir[setName1]))
            p.SetFromElementLabels(name = 'Elset-' + setName2, elementLabels = tuple(setsElementLabellis_dir[setName2]))
        

    
    def updateElements_3D_Interface_TET4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            setsElementLabellis_dir = { }
            setsElementLabellis_dir[setName1] = [ i.label for i in p.sets[setName1].elements ]
            setsElementLabellis_dir[setName2] = [ i.label for i in p.sets[setName2].elements ]
            interface_nodes_label = cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2]
            cohesiveNodesSetsList = []
            interface_elements_label_list = []
            cohesiveElementsLabelSet = []
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElements():
                    if j in p.sets[setName1].elements and p.elements.getFromLabel(j.label + cohesive_insert.skip) is None:
                        nodes_label = [ p.nodes[l].label for l in j.connectivity ]
                        for k in nodes_label:
                            index_k = nodes_label.index(k)
                            if k in interface_nodes_label:
                                nodes_label[index_k] += self.nodeskip
                                continue
                        p.Element(nodes = (p.nodes.getFromLabel(nodes_label[0]), p.nodes.getFromLabel(nodes_label[1]), p.nodes.getFromLabel(nodes_label[2]), p.nodes.getFromLabel(nodes_label[3])), elemShape = TET4, label = j.label + cohesive_insert.skip)
                        interface_elements_label_list.append(j.label)
                        continue
            
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElemFaces():
                    face_nodes_set = set([ k.label for k in j.getNodes() ])
                    if face_nodes_set.issubset(interface_nodes_label) and face_nodes_set not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        cohesiveNodesSetsList.append(face_nodes_set)
                        (node1, node2, node3) = j.getNodes()
                        cohesive_nodes = (p.nodes.getFromLabel(node1.label + self.nodeskip), p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node3.label + self.nodeskip), node1, node2, node3)
                        p.Element(nodes = cohesive_nodes, elemShape = WEDGE6, label = cohesive_insert.elements_num)
                        cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        continue
            
            for i in interface_elements_label_list:
                p.deleteElement(p.elements.getFromLabel(i))
                p.elements.getFromLabel(i + cohesive_insert.skip).setValues(i)
            
            p.SetFromElementLabels(name = 'Elset-' + setName1 + '-' + setName2 + '-interface_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName1, elementLabels = tuple(setsElementLabellis_dir[setName1]))
            p.SetFromElementLabels(name = 'Elset-' + setName2, elementLabels = tuple(setsElementLabellis_dir[setName2]))
        

    
    def updateElements_2D_Interface_QUAD4(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            setsElementLabellis_dir = { }
            setsElementLabellis_dir[setName1] = [ i.label for i in p.sets[setName1].elements ]
            setsElementLabellis_dir[setName2] = [ i.label for i in p.sets[setName2].elements ]
            interface_nodes_label = cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2]
            cohesiveNodesSetsList = []
            interface_elements_label_list = []
            cohesiveElementsLabelSet = []
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElements():
                    if j in p.sets[setName1].elements and p.elements.getFromLabel(j.label + cohesive_insert.skip) is None:
                        nodes_label = [ p.nodes[l].label for l in j.connectivity ]
                        for k in nodes_label:
                            index_k = nodes_label.index(k)
                            if k in interface_nodes_label:
                                nodes_label[index_k] += self.nodeskip
                                continue
                        p.Element(nodes = (p.nodes.getFromLabel(nodes_label[0]), p.nodes.getFromLabel(nodes_label[1]), p.nodes.getFromLabel(nodes_label[2]), p.nodes.getFromLabel(nodes_label[3])), elemShape = QUAD4, label = j.label + cohesive_insert.skip)
                        interface_elements_label_list.append(j.label)
                        continue
            
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElemEdges():
                    edge_nodes_set = set([ k.label for k in j.getNodes() ])
                    if edge_nodes_set.issubset(interface_nodes_label) and edge_nodes_set not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        cohesiveNodesSetsList.append(edge_nodes_set)
                        (node1, node2) = j.getNodes()
                        cohesive_nodes = (node1, node2, p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node1.label + self.nodeskip))
                        p.Element(nodes = cohesive_nodes, elemShape = QUAD4, label = cohesive_insert.elements_num)
                        cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        continue
            
            for i in interface_elements_label_list:
                p.deleteElement(p.elements.getFromLabel(i))
                p.elements.getFromLabel(i + cohesive_insert.skip).setValues(i)
            
            p.SetFromElementLabels(name = 'Elset-' + setName1 + '-' + setName2 + '-interface_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName1, elementLabels = tuple(setsElementLabellis_dir[setName1]))
            p.SetFromElementLabels(name = 'Elset-' + setName2, elementLabels = tuple(setsElementLabellis_dir[setName2]))
        

    
    def updateElements_3D_Interface_HEX8(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            setsElementLabellis_dir = { }
            setsElementLabellis_dir[setName1] = [ i.label for i in p.sets[setName1].elements ]
            setsElementLabellis_dir[setName2] = [ i.label for i in p.sets[setName2].elements ]
            interface_nodes_label = cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2]
            cohesiveNodesSetsList = []
            interface_elements_label_list = []
            cohesiveElementsLabelSet = []
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElements():
                    if j in p.sets[setName1].elements and p.elements.getFromLabel(j.label + cohesive_insert.skip) is None:
                        nodes_label = [ p.nodes[l].label for l in j.connectivity ]
                        for k in nodes_label:
                            index_k = nodes_label.index(k)
                            if k in interface_nodes_label:
                                nodes_label[index_k] += self.nodeskip
                                continue
                        p.Element(nodes = (p.nodes.getFromLabel(nodes_label[0]), p.nodes.getFromLabel(nodes_label[1]), p.nodes.getFromLabel(nodes_label[2]), p.nodes.getFromLabel(nodes_label[3]), p.nodes.getFromLabel(nodes_label[4]), p.nodes.getFromLabel(nodes_label[5]), p.nodes.getFromLabel(nodes_label[6]), p.nodes.getFromLabel(nodes_label[7])), elemShape = HEX8, label = j.label + cohesive_insert.skip)
                        interface_elements_label_list.append(j.label)
                        continue
            
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElemFaces():
                    face_nodes_set = set([ k.label for k in j.getNodes() ])
                    if face_nodes_set.issubset(interface_nodes_label) and face_nodes_set not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        cohesiveNodesSetsList.append(face_nodes_set)
                        (node1, node2, node3, node4) = j.getNodes()
                        cohesive_nodes = (p.nodes.getFromLabel(node1.label + self.nodeskip), p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node3.label + self.nodeskip), p.nodes.getFromLabel(node4.label + self.nodeskip), node1, node2, node3, node4)
                        p.Element(nodes = cohesive_nodes, elemShape = HEX8, label = cohesive_insert.elements_num)
                        cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        continue
            
            for i in interface_elements_label_list:
                p.deleteElement(p.elements.getFromLabel(i))
                p.elements.getFromLabel(i + cohesive_insert.skip).setValues(i)
            
            p.SetFromElementLabels(name = 'Elset-' + setName1 + '-' + setName2 + '-interface_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName1, elementLabels = tuple(setsElementLabellis_dir[setName1]))
            p.SetFromElementLabels(name = 'Elset-' + setName2, elementLabels = tuple(setsElementLabellis_dir[setName2]))
        

    
    def updateElements_3D_Interface_WEDGE(self):
        p = mdb.models[self.model].parts[self.part]
        for sets in self.sets:
            (setName1, setName2) = sets.split(';')
            setsElementLabellis_dir = { }
            setsElementLabellis_dir[setName1] = [ i.label for i in p.sets[setName1].elements ]
            setsElementLabellis_dir[setName2] = [ i.label for i in p.sets[setName2].elements ]
            interface_nodes_label = cohesive_insert.interface_nodes_label_dir['Nset-interface-' + setName1 + '-' + setName2]
            cohesiveNodesSetsList = []
            interface_elements_label_list = []
            cohesiveElementsLabelSet = []
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElements():
                    if j in p.sets[setName1].elements and p.elements.getFromLabel(j.label + cohesive_insert.skip) is None:
                        nodes_label = [ p.nodes[l].label for l in j.connectivity ]
                        for k in nodes_label:
                            index_k = nodes_label.index(k)
                            if k in interface_nodes_label:
                                nodes_label[index_k] += self.nodeskip
                                continue
                        p.Element(nodes = (p.nodes.getFromLabel(nodes_label[0]), p.nodes.getFromLabel(nodes_label[1]), p.nodes.getFromLabel(nodes_label[2]), p.nodes.getFromLabel(nodes_label[3]), p.nodes.getFromLabel(nodes_label[4]), p.nodes.getFromLabel(nodes_label[5])), elemShape = WEDGE6, label = j.label + cohesive_insert.skip)
                        interface_elements_label_list.append(j.label)
                        continue
            
            for i in interface_nodes_label:
                for j in p.nodes.getFromLabel(i).getElemFaces():
                    face_nodes_set = set([ k.label for k in j.getNodes() ])
                    if face_nodes_set.issubset(interface_nodes_label) and face_nodes_set not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        if len(face_nodes_set) == 3:
                            cohesiveNodesSetsList.append(face_nodes_set)
                            (node1, node2, node3) = j.getNodes()
                            cohesive_nodes = (p.nodes.getFromLabel(node1.label + self.nodeskip), p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node3.label + self.nodeskip), node1, node2, node3)
                            p.Element(nodes = cohesive_nodes, elemShape = WEDGE6, label = cohesive_insert.elements_num)
                            cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        if len(face_nodes_set) == 4:
                            cohesiveNodesSetsList.append(face_nodes_set)
                            (node1, node2, node3, node4) = j.getNodes()
                            cohesive_nodes = (p.nodes.getFromLabel(node1.label + self.nodeskip), p.nodes.getFromLabel(node2.label + self.nodeskip), p.nodes.getFromLabel(node3.label + self.nodeskip), p.nodes.getFromLabel(node4.label + self.nodeskip), node1, node2, node3, node4)
                            p.Element(nodes = cohesive_nodes, elemShape = HEX8, label = cohesive_insert.elements_num)
                            cohesiveElementsLabelSet.append(cohesive_insert.elements_num)
                        
            
            for i in interface_elements_label_list:
                p.deleteElement(p.elements.getFromLabel(i))
                p.elements.getFromLabel(i + cohesive_insert.skip).setValues(i)
            
            p.SetFromElementLabels(name = 'Elset-' + setName1 + '-' + setName2 + '-interface_cohesive', elementLabels = tuple(cohesiveElementsLabelSet))
            p.SetFromElementLabels(name = 'Elset-' + setName1, elementLabels = tuple(setsElementLabellis_dir[setName1]))
            p.SetFromElementLabels(name = 'Elset-' + setName2, elementLabels = tuple(setsElementLabellis_dir[setName2]))
        

    
    def updateElements_2D_Multiple_TRI3(self):
        p = mdb.models[self.model].parts[self.part]
        cohesiveNodesSetsList = []
        unionsetName = 'Unionset'
        missionElementsLabelSet = []
        nodeslabelset_dir = { }
        elementslabellist_dir = { }
        cohesiveelementslabellists_dir = { }
        setNames = self.sets[0].split(';')
        sets_combinations = list(combinations(setNames, 2))
        interfacenodesunionset = set([])
        interfacenodescombinationlist = []
        for combination in sets_combinations:
            
            try:
                nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]] = set([ node.label for node in p.sets['Nset-interface-' + combination[0] + '-' + combination[1]].nodes ])
                interfacenodescombinationlist.append(combination)
                interfacenodesunionset = interfacenodesunionset | nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]
            except:
                pass

            cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]] = []
        
        for setName in setNames:
            nodeslabelset_dir[setName] = set([ node.label for node in p.sets[setName].nodes ])
            elementslabellist_dir[setName] = [ element.label for element in p.sets[setName].elements ]
            cohesiveelementslabellists_dir[setName] = []
        
        for i in p.sets[unionsetName].elements:
            missionElementsLabelSet.append(i.label + cohesive_insert.skip)
            updatenodes = []
            for j in i.connectivity:
                updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
            
            nodes = tuple(updatenodes)
            p.Element(nodes = nodes, elemShape = TRI3, label = cohesive_insert.skip + i.label)
        
        p.SetFromElementLabels(name = 'Elset-' + unionsetName, elementLabels = tuple(missionElementsLabelSet))
        for i in p.sets['Elset-' + unionsetName].elements:
            m = [
                (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label)]
            for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                if j in p.sets[unionsetName].elements:
                    n = [
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label)]
                else:
                    n = [
                        (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                        (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                        (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label)]
                for k in m:
                    for l in n:
                        set_k = set(np.array(k) % self.nodeskip)
                        set_l = set(np.array(l) % self.nodeskip)
                        if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                            cohesiveNodesSetsList.append(set_k)
                            for setName in setNames:
                                if set_k.issubset(nodeslabelset_dir[setName]) and not set_k.issubset(interfacenodesunionset):
                                    cohesiveelementslabellists_dir[setName].append(cohesive_insert.elements_num)
                                    break
                                    continue
                                for combination in interfacenodescombinationlist:
                                    if set_k.issubset(nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]):
                                        cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]].append(cohesive_insert.elements_num)
                                        break
                                        continue
                            
                        
                    
                
            
        
        for i in missionElementsLabelSet:
            p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
        
        for i in p.sets['Elset-' + unionsetName].elements:
            i.setValues(i.label - cohesive_insert.skip)
        
        for setName in setNames:
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(elementslabellist_dir[setName]))
            p.SetFromElementLabels(name = 'Elset-' + setName + '-cohesive', elementLabels = tuple(cohesiveelementslabellists_dir[setName]))
        
        for combination in interfacenodescombinationlist:
            p.SetFromElementLabels(name = 'Elset-interface-' + combination[0] + '-' + combination[1], elementLabels = tuple(cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]]))
        

    
    def updateElements_3D_Multiple_TET4(self):
        p = mdb.models[self.model].parts[self.part]
        cohesiveNodesSetsList = []
        unionsetName = 'Unionset'
        missionElementsLabelSet = []
        nodeslabelset_dir = { }
        elementslabellist_dir = { }
        cohesiveelementslabellists_dir = { }
        setNames = self.sets[0].split(';')
        sets_combinations = list(combinations(setNames, 2))
        interfacenodesunionset = set([])
        interfacenodescombinationlist = []
        for combination in sets_combinations:
            
            try:
                nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]] = set([ node.label for node in p.sets['Nset-interface-' + combination[0] + '-' + combination[1]].nodes ])
                interfacenodescombinationlist.append(combination)
                interfacenodesunionset = interfacenodesunionset | nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]
            except:
                pass

            cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]] = []
        
        for setName in setNames:
            nodeslabelset_dir[setName] = set([ node.label for node in p.sets[setName].nodes ])
            elementslabellist_dir[setName] = [ element.label for element in p.sets[setName].elements ]
            cohesiveelementslabellists_dir[setName] = []
        
        for i in p.sets[unionsetName].elements:
            missionElementsLabelSet.append(i.label + cohesive_insert.skip)
            updatenodes = []
            for j in i.connectivity:
                updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
            
            nodes = tuple(updatenodes)
            p.Element(nodes = nodes, elemShape = TET4, label = cohesive_insert.skip + i.label)
        
        p.SetFromElementLabels(name = 'Elset-' + unionsetName, elementLabels = tuple(missionElementsLabelSet))
        for i in p.sets['Elset-' + unionsetName].elements:
            m = [
                (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label),
                (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label)]
            adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
            for j in adjacent_local_elements:
                if j in p.sets[setName].elements:
                    new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                else:
                    new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                new_element_nodes_set = set(new_element_nodes_lis)
                new_element_nodes_dir = { }
                for node in new_element_nodes_lis:
                    new_element_nodes_dir[node % self.nodeskip] = node
                
                for k in m:
                    set_yu_k = set(np.array(k) % self.nodeskip)
                    set_k = set(k)
                    if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                        cohesiveNodesSetsList.append(set_yu_k)
                        for setName in setNames:
                            if set_yu_k.issubset(nodeslabelset_dir[setName]) and not set_yu_k.issubset(interfacenodesunionset):
                                cohesiveelementslabellists_dir[setName].append(cohesive_insert.elements_num)
                                break
                                continue
                            for combination in interfacenodescombinationlist:
                                if set_yu_k.issubset(nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]):
                                    cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]].append(cohesive_insert.elements_num)
                                    break
                                    continue
                        
                    
                
            
        
        for i in missionElementsLabelSet:
            p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
        
        for i in p.sets['Elset-' + unionsetName].elements:
            i.setValues(i.label - cohesive_insert.skip)
        
        for setName in setNames:
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(elementslabellist_dir[setName]))
            p.SetFromElementLabels(name = 'Elset-' + setName + '-cohesive', elementLabels = tuple(cohesiveelementslabellists_dir[setName]))
        
        for combination in interfacenodescombinationlist:
            p.SetFromElementLabels(name = 'Elset-interface-' + combination[0] + '-' + combination[1], elementLabels = tuple(cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]]))
        

    
    def updateElements_2D_Multiple_QUAD4(self):
        p = mdb.models[self.model].parts[self.part]
        cohesiveNodesSetsList = []
        unionsetName = 'Unionset'
        missionElementsLabelSet = []
        nodeslabelset_dir = { }
        elementslabellist_dir = { }
        cohesiveelementslabellists_dir = { }
        setNames = self.sets[0].split(';')
        sets_combinations = list(combinations(setNames, 2))
        interfacenodesunionset = set([])
        interfacenodescombinationlist = []
        for combination in sets_combinations:
            
            try:
                nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]] = set([ node.label for node in p.sets['Nset-interface-' + combination[0] + '-' + combination[1]].nodes ])
                interfacenodescombinationlist.append(combination)
                interfacenodesunionset = interfacenodesunionset | nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]
            except:
                pass

            cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]] = []
        
        for setName in setNames:
            nodeslabelset_dir[setName] = set([ node.label for node in p.sets[setName].nodes ])
            elementslabellist_dir[setName] = [ element.label for element in p.sets[setName].elements ]
            cohesiveelementslabellists_dir[setName] = []
        
        for i in p.sets[unionsetName].elements:
            missionElementsLabelSet.append(i.label + cohesive_insert.skip)
            updatenodes = []
            for j in i.connectivity:
                updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
            
            nodes = tuple(updatenodes)
            p.Element(nodes = nodes, elemShape = QUAD4, label = cohesive_insert.skip + i.label)
        
        p.SetFromElementLabels(name = 'Elset-' + unionsetName, elementLabels = tuple(missionElementsLabelSet))
        for i in p.sets['Elset-' + unionsetName].elements:
            m = [
                (i.getElemEdges()[0].getNodes()[0].label, i.getElemEdges()[0].getNodes()[1].label),
                (i.getElemEdges()[1].getNodes()[0].label, i.getElemEdges()[1].getNodes()[1].label),
                (i.getElemEdges()[2].getNodes()[0].label, i.getElemEdges()[2].getNodes()[1].label),
                (i.getElemEdges()[3].getNodes()[0].label, i.getElemEdges()[3].getNodes()[1].label)]
            for j in p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements():
                if j in p.sets[unionsetName].elements:
                    n = [
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[0].getNodes()[1].label),
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[1].getNodes()[1].label),
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[2].getNodes()[1].label),
                        (p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[0].label, p.elements.getFromLabel(j.label + cohesive_insert.skip).getElemEdges()[3].getNodes()[1].label)]
                else:
                    n = [
                        (j.getElemEdges()[0].getNodes()[0].label, j.getElemEdges()[0].getNodes()[1].label),
                        (j.getElemEdges()[1].getNodes()[0].label, j.getElemEdges()[1].getNodes()[1].label),
                        (j.getElemEdges()[2].getNodes()[0].label, j.getElemEdges()[2].getNodes()[1].label),
                        (j.getElemEdges()[3].getNodes()[0].label, j.getElemEdges()[3].getNodes()[1].label)]
                for k in m:
                    for l in n:
                        set_k = set(np.array(k) % self.nodeskip)
                        set_l = set(np.array(l) % self.nodeskip)
                        if set_k == set_l and k != l or set_k not in cohesiveNodesSetsList:
                            cohesive_insert.elements_num += 1
                            p.Element(nodes = (p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(l[1]), p.nodes.getFromLabel(l[0])), elemShape = QUAD4, label = cohesive_insert.elements_num)
                            cohesiveNodesSetsList.append(set_k)
                            for setName in setNames:
                                if set_k.issubset(nodeslabelset_dir[setName]) and not set_k.issubset(interfacenodesunionset):
                                    cohesiveelementslabellists_dir[setName].append(cohesive_insert.elements_num)
                                    break
                                    continue
                                for combination in interfacenodescombinationlist:
                                    if set_k.issubset(nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]):
                                        cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]].append(cohesive_insert.elements_num)
                                        break
                                        continue
                            
                        
                    
                
            
        
        for i in missionElementsLabelSet:
            p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
        
        for i in p.sets['Elset-' + unionsetName].elements:
            i.setValues(i.label - cohesive_insert.skip)
        
        for setName in setNames:
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(elementslabellist_dir[setName]))
            p.SetFromElementLabels(name = 'Elset-' + setName + '-cohesive', elementLabels = tuple(cohesiveelementslabellists_dir[setName]))
        
        for combination in interfacenodescombinationlist:
            p.SetFromElementLabels(name = 'Elset-interface-' + combination[0] + '-' + combination[1], elementLabels = tuple(cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]]))
        

    
    def updateElements_3D_Multiple_HEX8(self):
        p = mdb.models[self.model].parts[self.part]
        cohesiveNodesSetsList = []
        unionsetName = 'Unionset'
        missionElementsLabelSet = []
        nodeslabelset_dir = { }
        elementslabellist_dir = { }
        cohesiveelementslabellists_dir = { }
        setNames = self.sets[0].split(';')
        sets_combinations = list(combinations(setNames, 2))
        interfacenodesunionset = set([])
        interfacenodescombinationlist = []
        for combination in sets_combinations:
            
            try:
                nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]] = set([ node.label for node in p.sets['Nset-interface-' + combination[0] + '-' + combination[1]].nodes ])
                interfacenodescombinationlist.append(combination)
                interfacenodesunionset = interfacenodesunionset | nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]
            except:
                pass

            cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]] = []
        
        for setName in setNames:
            nodeslabelset_dir[setName] = set([ node.label for node in p.sets[setName].nodes ])
            elementslabellist_dir[setName] = [ element.label for element in p.sets[setName].elements ]
            cohesiveelementslabellists_dir[setName] = []
        
        for i in p.sets[unionsetName].elements:
            missionElementsLabelSet.append(i.label + cohesive_insert.skip)
            updatenodes = []
            for j in i.connectivity:
                updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
            
            nodes = tuple(updatenodes)
            p.Element(nodes = nodes, elemShape = HEX8, label = cohesive_insert.skip + i.label)
        
        p.SetFromElementLabels(name = 'Elset-' + unionsetName, elementLabels = tuple(missionElementsLabelSet))
        for i in p.sets['Elset-' + unionsetName].elements:
            m = [
                (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label, i.getElemFaces()[0].getNodes()[3].label),
                (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label, i.getElemFaces()[1].getNodes()[3].label),
                (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label),
                (i.getElemFaces()[5].getNodes()[0].label, i.getElemFaces()[5].getNodes()[1].label, i.getElemFaces()[5].getNodes()[2].label, i.getElemFaces()[5].getNodes()[3].label)]
            adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
            for j in adjacent_local_elements:
                if j in p.sets[setName].elements:
                    new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                else:
                    new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                new_element_nodes_set = set(new_element_nodes_lis)
                new_element_nodes_dir = { }
                for node in new_element_nodes_lis:
                    new_element_nodes_dir[node % self.nodeskip] = node
                
                for k in m:
                    set_yu_k = set(np.array(k) % self.nodeskip)
                    set_k = set(k)
                    if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                        cohesiveNodesSetsList.append(set_yu_k)
                        for setName in setNames:
                            if set_yu_k.issubset(nodeslabelset_dir[setName]) and not set_yu_k.issubset(interfacenodesunionset):
                                cohesiveelementslabellists_dir[setName].append(cohesive_insert.elements_num)
                                break
                                continue
                            for combination in interfacenodescombinationlist:
                                if set_yu_k.issubset(nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]):
                                    cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]].append(cohesive_insert.elements_num)
                                    break
                                    continue
                        
                    
                
            
        
        for i in missionElementsLabelSet:
            p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
        
        for i in p.sets['Elset-' + unionsetName].elements:
            i.setValues(i.label - cohesive_insert.skip)
        
        for setName in setNames:
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(elementslabellist_dir[setName]))
            p.SetFromElementLabels(name = 'Elset-' + setName + '-cohesive', elementLabels = tuple(cohesiveelementslabellists_dir[setName]))
        
        for combination in interfacenodescombinationlist:
            p.SetFromElementLabels(name = 'Elset-interface-' + combination[0] + '-' + combination[1], elementLabels = tuple(cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]]))
        

    
    def updateElements_3D_Multiple_WEDGE(self):
        p = mdb.models[self.model].parts[self.part]
        cohesiveNodesSetsList = []
        unionsetName = 'Unionset'
        missionElementsLabelSet = []
        nodeslabelset_dir = { }
        elementslabellist_dir = { }
        cohesiveelementslabellists_dir = { }
        setNames = self.sets[0].split(';')
        sets_combinations = list(combinations(setNames, 2))
        interfacenodesunionset = set([])
        interfacenodescombinationlist = []
        for combination in sets_combinations:
            
            try:
                nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]] = set([ node.label for node in p.sets['Nset-interface-' + combination[0] + '-' + combination[1]].nodes ])
                interfacenodescombinationlist.append(combination)
                interfacenodesunionset = interfacenodesunionset | nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]
            except:
                pass

            cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]] = []
        
        for setName in setNames:
            nodeslabelset_dir[setName] = set([ node.label for node in p.sets[setName].nodes ])
            elementslabellist_dir[setName] = [ element.label for element in p.sets[setName].elements ]
            cohesiveelementslabellists_dir[setName] = []
        
        for i in p.sets[unionsetName].elements:
            missionElementsLabelSet.append(i.label + cohesive_insert.skip)
            updatenodes = []
            for j in i.connectivity:
                updatenodes.append(p.nodes.getFromLabel(cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] * self.nodeskip + p.nodes[j].label))
                cohesive_insert.nodes_states[p.nodes[j].label]['usecode'] += 1
            
            nodes = tuple(updatenodes)
            p.Element(nodes = nodes, elemShape = WEDGE6, label = cohesive_insert.skip + i.label)
        
        p.SetFromElementLabels(name = 'Elset-' + unionsetName, elementLabels = tuple(missionElementsLabelSet))
        for i in p.sets['Elset-' + unionsetName].elements:
            m = [
                (i.getElemFaces()[0].getNodes()[0].label, i.getElemFaces()[0].getNodes()[1].label, i.getElemFaces()[0].getNodes()[2].label),
                (i.getElemFaces()[1].getNodes()[0].label, i.getElemFaces()[1].getNodes()[1].label, i.getElemFaces()[1].getNodes()[2].label),
                (i.getElemFaces()[2].getNodes()[0].label, i.getElemFaces()[2].getNodes()[1].label, i.getElemFaces()[2].getNodes()[2].label, i.getElemFaces()[2].getNodes()[3].label),
                (i.getElemFaces()[3].getNodes()[0].label, i.getElemFaces()[3].getNodes()[1].label, i.getElemFaces()[3].getNodes()[2].label, i.getElemFaces()[3].getNodes()[3].label),
                (i.getElemFaces()[4].getNodes()[0].label, i.getElemFaces()[4].getNodes()[1].label, i.getElemFaces()[4].getNodes()[2].label, i.getElemFaces()[4].getNodes()[3].label)]
            adjacent_local_elements = p.elements.getFromLabel(i.label - cohesive_insert.skip).getAdjacentElements()
            for j in adjacent_local_elements:
                if j in p.sets[setName].elements:
                    new_element_nodes_lis = [ node.label for node in p.elements.getFromLabel(j.label + cohesive_insert.skip).getNodes() ]
                else:
                    new_element_nodes_lis = [ node.label for node in j.getNodes() ]
                new_element_nodes_yu_set = set(np.array(new_element_nodes_lis) % self.nodeskip)
                new_element_nodes_set = set(new_element_nodes_lis)
                new_element_nodes_dir = { }
                for node in new_element_nodes_lis:
                    new_element_nodes_dir[node % self.nodeskip] = node
                
                for k in m:
                    set_yu_k = set(np.array(k) % self.nodeskip)
                    set_k = set(k)
                    if set_yu_k.issubset(new_element_nodes_yu_set) and not set_k.issubset(new_element_nodes_set) or set_yu_k not in cohesiveNodesSetsList:
                        cohesive_insert.elements_num += 1
                        if len(set_yu_k) == 3:
                            p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip])), elemShape = WEDGE6, label = cohesive_insert.elements_num)
                            cohesiveNodesSetsList.append(set_yu_k)
                        if len(set_yu_k) == 4:
                            p.Element(nodes = (p.nodes.getFromLabel(k[0]), p.nodes.getFromLabel(k[1]), p.nodes.getFromLabel(k[2]), p.nodes.getFromLabel(k[3]), p.nodes.getFromLabel(new_element_nodes_dir[k[0] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[1] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[2] % self.nodeskip]), p.nodes.getFromLabel(new_element_nodes_dir[k[3] % self.nodeskip])), elemShape = HEX8, label = cohesive_insert.elements_num)
                            cohesiveNodesSetsList.append(set_yu_k)
                        for setName in setNames:
                            if set_yu_k.issubset(nodeslabelset_dir[setName]) and not set_yu_k.issubset(interfacenodesunionset):
                                cohesiveelementslabellists_dir[setName].append(cohesive_insert.elements_num)
                                break
                                continue
                            for combination in interfacenodescombinationlist:
                                if set_yu_k.issubset(nodeslabelset_dir['Nset-interface-' + combination[0] + '-' + combination[1]]):
                                    cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]].append(cohesive_insert.elements_num)
                                    break
                                    continue
                        
                    
                
            
        
        for i in missionElementsLabelSet:
            p.deleteElement(p.elements.getFromLabel(i - cohesive_insert.skip))
        
        for i in p.sets['Elset-' + unionsetName].elements:
            i.setValues(i.label - cohesive_insert.skip)
        
        for setName in setNames:
            p.SetFromElementLabels(name = 'Elset-' + setName, elementLabels = tuple(elementslabellist_dir[setName]))
            p.SetFromElementLabels(name = 'Elset-' + setName + '-cohesive', elementLabels = tuple(cohesiveelementslabellists_dir[setName]))
        
        for combination in interfacenodescombinationlist:
            p.SetFromElementLabels(name = 'Elset-interface-' + combination[0] + '-' + combination[1], elementLabels = tuple(cohesiveelementslabellists_dir['Elset-interface-' + combination[0] + '-' + combination[1]]))
        



def mission_execute(Dimension, Part, Mode, Sets, ElementShape):
    x = cohesive_insert(Part, Sets)
    updateElements_method_dir = {
        (2, 10, 23): x.updateElements_2D_Inner_edge_TRI3,
        (2, 11, 23): x.updateElements_2D_Inner_TRI3,
        (2, 10, 24): x.updateElements_2D_Inner_edge_QUAD4,
        (2, 11, 24): x.updateElements_2D_Inner_QUAD4,
        (2, 20, 23): x.updateElements_2D_Interface_TRI3,
        (2, 20, 24): x.updateElements_2D_Interface_QUAD4,
        (2, 30, 23): x.updateElements_2D_Multiple_TRI3,
        (2, 30, 24): x.updateElements_2D_Multiple_QUAD4,
        (3, 10, 34): x.updateElements_3D_Inner_edge_TET4,
        (3, 11, 34): x.updateElements_3D_Inner_TET4,
        (3, 11, 36): x.updateElements_3D_Inner_WEDGE,
        (3, 10, 36): x.updateElements_3D_Inner_edge_WEDGE,
        (3, 10, 38): x.updateElements_3D_Inner_edge_HEX8,
        (3, 11, 38): x.updateElements_3D_Inner_HEX8,
        (3, 20, 34): x.updateElements_3D_Interface_TET4,
        (3, 20, 38): x.updateElements_3D_Interface_HEX8,
        (3, 20, 36): x.updateElements_3D_Interface_WEDGE,
        (3, 30, 34): x.updateElements_3D_Multiple_TET4,
        (3, 30, 38): x.updateElements_3D_Multiple_HEX8,
        (3, 30, 36): x.updateElements_3D_Multiple_WEDGE }
    copyNodes_method_dir = {
        (2, 10): x.copyNodes_2D_Inner_edge,
        (2, 11): x.copyNodes_2D_Inner,
        (2, 20): x.copyNodes_2D_Interface,
        (2, 30): x.copyNodes_2D_Multiple,
        (3, 10): x.copyNodes_3D_Inner_edge,
        (3, 11): x.copyNodes_3D_Inner,
        (3, 20): x.copyNodes_3D_Interface,
        (3, 30): x.copyNodes_3D_Multiple }
    if cohesive_insert.converttomeshpart == 0:
        x.convertToMeshpart()
        cohesive_insert.converttomeshpart = 1
    copyNodes_method_dir[(Dimension, Mode)]()
    updateElements_method_dir[(Dimension, Mode, ElementShape)]()