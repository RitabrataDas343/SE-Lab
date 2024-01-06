# Name: Ritabrata Das
# Roll No. : 20CS8002

from pycfg.pycfg import PyCFG, CFGNode, slurp
import argparse

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('pythonfile', help ='The python file to be analyzed')
	args = parser.parse_args()
	arcs = []
	cfg = PyCFG()
	cfg.gen_cfg(slurp(args.pythonfile).strip())
	graph = CFGNode.to_graph(arcs)
	graph.draw(args.pythonfile + '.svg', prog ='dot')

	nodes = graph.number_of_nodes()	 
	edges = graph.number_of_edges()	 
	complexity = edges - nodes + 2		 

	print("The number of nodes is: ", nodes)
	print("The number of edges is: ", edges)
	print("The number of independent paths: ", complexity)
	print("The number of bounded regions: ", complexity-1)
	print("The cyclomatic complexity is: ", complexity)
	print("The number of loops: ", complexity-1)
