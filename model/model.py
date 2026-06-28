import itertools
from collections import defaultdict

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.DiGraph()
        self._artist = DAO.getAllArtist()
        self._idMapArtist = {}
        for a in self._artist:
            self._idMapArtist[a] = a


    def getGeneri(self):
        return DAO.getGeneri()

    def creaGrafo(self, g):
        self._graph.clear()
        nodes = DAO.getAllNodes(self, g)
        self._graph.add_nodes_from(nodes)
        custArt = DAO.getCustomerArt(self, g)

        custMap = defaultdict(dict)
        for customer_id, Name, ntracks in custArt:
            custMap[customer_id][Name] = ntracks

        artist_popularity = defaultdict(int)
        for customer, artist in custMap.items():
            for artist_id, ntracks in artist.items():
                artist_popularity[artist_id] += ntracks

        for customer_id, artists in custMap.items():

            for a, b in itertools.combinations(artists.keys(), 2):

                pop_a = artist_popularity[a]
                pop_b = artist_popularity[b]

                weight = pop_a + pop_b

                if pop_a < pop_b:
                    self._graph.add_edge(a, b, weight=weight)
                elif pop_a > pop_b:
                    self._graph.add_edge(b, a, weight=weight)
                else:
                    self._graph.add_edge(a, b, weight=weight)
                    self._graph.add_edge(b, a, weight=weight)

        print(f"N nodi: {len(self._graph.nodes)}, n archi: {len(self._graph.edges)}")

    def getInfo(self):

        bestArtist = None
        bestScore = None

        for v in self._graph.nodes:
            n1 = 0
            n2 = 0
            for _,_,data in self._graph.out_edges(v, data=True):
                n1 += data["weight"]
            for _,_,data in self._graph.in_edges(v, data=True):
                n2 += data["weight"]
            n = n1-n2

            if bestScore is None or n > bestScore:
                bestScore = n
                bestArtist = v

        return bestArtist, bestScore
