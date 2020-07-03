import csv, os

path = os.getcwd()
files = os.listdir(path)
node_path = None
net_path = None
for f in files:
    if '_node' in f and f.endswith('.tntp'):
        node_path = f
    if '_net' in f and f.endswith('.tntp'):
        net_path = f
with open(node_path, 'r', encoding='utf-8') as f:
    nodes = f.readlines()
    del nodes[0]
    for i in range(len(nodes)):
        nodes[i] = nodes[i].split('\t')
        del nodes[i][3]
f.close()
with open('node.csv', 'w', newline='') as f:
    header = ['name', 'node_id', 'x_coord', 'y_coord']
    writer = csv.writer(f)
    writer.writerow(header)
    for n in nodes:
        writer.writerow([None, int(n[0]), int(n[1]), int(n[2])])
f.close()
del nodes
with open(net_path, 'r', encoding='utf-8') as f:
    links = f.readlines()
    for i in range(9):
        del links[0]
    for i in range(len(links)):
        links[i] = links[i].split('\t')
        del links[i][0]
        del links[i][10]
f.close()
with open('road_link.csv', 'w', newline='') as f:
    header = ['name', 'road_link_id', 'from_node_id', 'to_node_id', 'link_type', 'length', 'lanes', 'free_speed', 'capacity']
    writer = csv.writer(f)
    writer.writerow(header)
    road_link_id = 1
    for l in links:
        now_link = []
        now_link.extend([None, road_link_id, int(l[0]), int(l[1]), int(l[9]), float(l[3]), 1, float(l[7]), int(l[2])])
        road_link_id += 1
        writer.writerow(now_link)
f.close()
print('转换完成')
