import csv, os

path = os.getcwd()
files = os.listdir(path)
node_path = None
net_path = None
trips_path = None
for f in files:
    if '_node' in f and f.endswith('.tntp'):
        node_path = f
    if '_net' in f and f.endswith('.tntp'):
        net_path = f
    if '_trips' in f and f.endswith('.tntp'):
        trips_path = f
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
        writer.writerow([None, int(n[0]), float(n[1]), float(n[2])])
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
    header = ['name', 'road_link_id', 'from_node_id', 'to_node_id','facility_type','link_type', 'length', 'lanes', 'free_speed', 'capacity']
    writer = csv.writer(f)
    writer.writerow(header)
    road_link_id = 1
    for l in links:
        now_link = []
        now_link.extend([None, road_link_id, int(l[0]), int(l[1]),'Highway' ,int(l[9]), float(l[3]), 1, float(l[7]), float(l[2])])
        road_link_id += 1
        writer.writerow(now_link)
f.close()
del links
with open(trips_path, 'r', encoding='utf-8') as f:
    for i in range(11):
        f.readline()
    lines = f.readlines()
    ODs = []
    for i in range(len(lines)):
        if lines[i][0:6] == "Origin":
            line=lines[i].replace(' ','')
            line=line.replace('\n','')
            line = line.replace('Origin', '')
            O = int(line)
        else:
            lines[i]=lines[i].replace(' ','')
            now_line=lines[i].split(';')
            del now_line[len(now_line)-1]
            newOD=[]
            for D in now_line:
                D_and_value=D.split(':')
                newOD.append([O,int(D_and_value[0]),float(D_and_value[1])])
            ODs.extend(newOD)
f.close()
with open('demand.csv','w', newline='') as f:
    header=['o','d','value']
    writer=csv.writer(f)
    writer.writerow(header)
    for OD in ODs:
        writer.writerow(OD)
f.close()
print('转换完成')
