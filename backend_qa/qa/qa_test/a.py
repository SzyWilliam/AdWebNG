from py2neo import Graph, Node

g = Graph("http://44.193.100.172:7474", auth=("neo4j", "000720"))

g.run("create (m:Disease{name:'aaa'})RETURN m")