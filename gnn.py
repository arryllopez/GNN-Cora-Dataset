from torch_geometric.datasets import Planetoid #planetoid has popular citation network datasets like Cora

#Loading the cora dataset
dataset = Planetoid(root='/tmp/Cora', name='Cora')

#accessing the first graph object
data = dataset[0]