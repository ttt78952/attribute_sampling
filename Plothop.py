import snap

# Undirected
g = snap.LoadEdgeList(snap.PUNGraph, "E:\\Research\\Jupyter\\WWW19 Random Walk Attribute Sampling\\power2_3_mhrw.edgelist", 0, 1)
snap.PlotHops(g, "mhrw", "hops", False, 512)

# Directed
#g = snap.LoadEdgeList(snap.PNGraph, "E:\\Research\\Jupyter\\Random Walk Attribute Sampling\\Dataset\\_nonattri_twitter_follows(Directed)\\soc-twitter-follows-mun.edges", 0, 1)
#snap.PlotHops(g, "twitter", "", True, 512)
