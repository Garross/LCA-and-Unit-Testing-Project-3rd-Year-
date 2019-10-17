""" A Python Class
A simple Python graph class, demonstrating the essential
facts and functionalities of graphs.

FOUND ON GITHUB which led to website: https://www.nco.ncep.noaa.gov/pmb/codes/nwprod/nwm.v2.0.0/ush/resume_forecast/Graph.py
"""

import unittest
import itertools


class DAG_LCA:

    def findLCA(dagDict, v1, v2):

        solution = []

        anc1 = [v1]
        anc2 = [v2]
        v1ancestors = getAncestors(v1, dagDict, anc1)
        v2ancestors = getAncestors(v2, dagDict, anc2)

        for i in v1ancestors:
            for i2 in v2ancestors:
                if i == i2:
                    solution.append(i)

        return solution

    def getAncestors(v, dagDict, anc):

        if prev(v, dagDict) == []:
            return []

        anc.append(prev(v, dagDict))
        anc = list(itertools.chain(*anc))

        for i in prev(v, dagDict):
            anc.append(getAncestors(i, dagDict, anc))
            anc = list(itertools.chain(*anc))

        return list(set(anc))

    def prev(v, dagDict):

        prev = []

        for i in dagDict.keys():
            if v in dagDict[i]:
                prev.append(i)

        return prev


# class to hold DAG objet
# Adopted and modified from https://www.nco.ncep.noaa.gov/pmb/codes/nwprod/nwm.v2.0.0/ush/resume_forecast/Graph.py

class DAG:

    def __init__(self, graph_dict=None):
        """ initializes a graph object
            If no dictionary or None is given, an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list;
            between two vertices can be multiple edges!
            Adds path from first given vertex to second given vertex
        """

        if len(edge) != 2:
            return

        vertex1, vertex2 = edge

        if vertex1 in self.__graph_dict and vertex2 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.add_vertex(vertex2)
            self.add_vertex(vertex1)
            self.__graph_dict[vertex1].append(vertex2)

    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                s = [vertex, neighbour]
                if s not in edges:
                    edges.append(s)
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + ", "
        res += "edges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def graphDict(self):
        return (self.__graph_dict)


