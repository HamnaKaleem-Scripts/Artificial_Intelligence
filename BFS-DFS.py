class CityData:
    def __init__(self,name,outconcount,outcons):
        self.name=name
        self.outconcount=outconcount
        self.outcons=outcons
        self.seen=False
        self.predecessor=-1
def read_file(filename):
    with open(filename, 'r') as file:
        city=[]
        n = int(file.readline().strip()) 
        for i in range(n): 
            data = file.readline().strip().split()
            name=data[1]
            # connections=data[3:]
            # if fname==name :
            #     city.append(name,connections)
            # city.append(CityData(name, connections))
            outConCount = int(data[2])
            if outConCount==0:
                outCons=None
            else:
                outCons = list(int(data[3:]))
            city.append(CityData(name, outConCount, outCons))
    return city

def recursive_dfs(city, current, d, path):
    city[current].seen = True
    path.append(city[current].name)

    if city[current].name == d:
        return True

    for i in city[current].outCons:
        if not city[i].seen:
            city[i].predecessor = current
            if recursive_dfs(city, i, d, path):
                return True

    path.pop()
    return False

def  path_des(city,start,destination):
     if start == -1:
        print(f"{start} is not a valid city, please re-enter options.")
        return
     if destination == -1:
        print(f"{destination} is not a valid city, please re-enter options.")
        return
     path = [] 
     if recursive_dfs(city, start, destination, path):
        print(path)
    
    


def main():
    filename = input("Please enter filename storing a network: ")
    cities = read_file(filename)

    start= input("Enter  name of starting city: ")
    destination = input("Enter  name of destination: ")

    path_des(cities, start, destination)

main()
        
        
        
    
