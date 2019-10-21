import unittest  # use unittest.TestCase
from graph import Graph, GraphError


class Test_Graph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(('a','b',1),('a','c',3),('b','a',2),('d','b',2),('d','c',1),'e')

    
    def test_del_edge(self):
        edges = 5
        self.assertEqual(len(self.graph),edges)
        for e in self.graph:
            if type(e) is tuple:
                del self.graph[e[0:2]]
                edges -= 1
            self.assertEqual(len(self.graph),edges)

        
    def test_del_node(self):
        self.assertEqual(len(self.graph),5)
        for n_remove,new_len in zip('edcba',(5,3,2,0,0)):
            del self.graph[n_remove]
            self.assertEqual(len(self.graph),new_len)
            

    def test_del_exception(self):
        self.assertRaises(GraphError,self.graph.__delitem__,1)
        self.assertRaises(GraphError,self.graph.__delitem__,('a','b',1,1))
        self.assertRaises(GraphError,self.graph.__delitem__,(1,'a'))
        self.assertRaises(GraphError,self.graph.__delitem__,('a',1))

    
    def test_in(self):
        for e in self.graph:
            self.assertIn(e, self.graph)
            if type(e) is tuple:
                self.assertIn(e[0], self.graph)
                self.assertIn(e[1], self.graph)
                self.assertIn((e[0],e[1]), self.graph)
                self.assertIn((e[0],e[1],e[2]), self.graph)
        self.assertNotIn('x', self.graph)
        self.assertNotIn(('c','a'), self.graph)
        self.assertNotIn(('a','c',4), self.graph)
        

    def test_degree(self):
        degrees = {n: self.graph.degree(n) for n in 'abcde' if type(n) is str}
        self.assertDictEqual(degrees, {'a':3, 'b':3, 'c':2, 'd':2, 'e':0})
