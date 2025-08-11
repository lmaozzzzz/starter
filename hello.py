graph = {}
with open('index.txt', 'r', encoding='utf-8') as file:
    firstline = file.readline().strip().split()
    ttbandau = firstline[0]
    ttketthuc = firstline[1]
    
    for line in file:
        parts = line.strip().split()
        dinh = parts[0]
        trongso = int(parts[1])
        ttke = parts[2:]
        graph[dinh] = (trongso, ttke)


if ttbandau not in graph or ttketthuc not in graph:
    print("Trạng thái ban đầu hoặc trạng thái kết thúc không hợp lệ.")
    exit()

L = [ttbandau]
visited = set()
output = []
path = []

while L:
    u = L.pop(0)
    if u in visited:
        continue

    visited.add(u)
    path.append(u)

    ttke = graph[u][1]
    trongsottke = [f"{n} ({graph[n][0]})" for n in ttke] 
    L1 = sorted(trongsottke, key=lambda x: graph[x.split(' ')[0]][0])


    if u==ttbandau:
     output.append({
        "Trạng thái phát triển": "",
        "Trạng thái kề": "",
        "Danh sách L1": "",
        "Danh sách L": f"{u} ({graph[u][0]})",
        
        
    })


    output.append({
        "Trạng thái phát triển": f"{u} ({graph[u][0]})",
        "Trạng thái kề": ", ".join(trongsottke),
        "Danh sách L1": ", ".join(L1),
        "Danh sách L": ", ".join(L1 + [f"{v} ({graph[v][0]})" for v in L]),
        
    })

    if u == ttketthuc:
        output[-1]={
            "Trạng thái phát triển": f"{u} ({graph[u][0]})",
            "Trạng thái kề": "TTKT-Dừng",
            "Danh sách L1": "",
            "Danh sách L": "",
            
        }
        break
        
    

    L1 = [v for v in ttke if v not in visited and v in graph]
    L1.sort(key=lambda x: graph[x][0])
    L = L1 + L

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(f"{'Trạng thái phát triển':<30} {'Trạng thái kề':<40} {'Danh sách L1':<40} {'Danh sách L':<40} {'Danh sách L3':<40}\n")
    f.write("="*150 + "\n")
    for entry in output:
        f.write(f"{entry['Trạng thái phát triển']:<30} {entry['Trạng thái kề']:<40} {entry['Danh sách L1']:<40}  {entry['Danh sách L']:<40} \n")
    
    
    f.write("\nKết luận: Đường đi từ trạng thái ban đầu đến trạng thái kết thúc là:\n")
    f.write(" -> ".join([f"{node} ({graph[node][0]})" for node in path]) + "\n")

print("Kết quả đã được lưu vào output.txt")




lmaozzzzzzzzzzzzzzzzzzzzz
sadháhđánkládkládá