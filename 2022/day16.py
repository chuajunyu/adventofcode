from tools import extract_input



'''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB'''


input = extract_input(r"test.txt")


class ValveNode:
    def __init__(self, name, flow_rate, direct_connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connections = {valve: 1 for valve in direct_connections}

    @property
    def direct_connection(self):
        return [connection for connection in self.connections if self.connections[connection] == 1]
    
    def update_connections(self, valve):
        for conn in valve.connections:
            if conn == self.name:
                continue
            elif conn not in self.connections:
                self.connections[conn] = valve.connections[conn] + 1
            elif conn in self.connections:
                self.connections[conn] = min([valve.connections[conn] + 1, self.connections[conn]])


def create_valve_node(line):
    result = line.split('; tunnels lead to valves ')
    if len(result) == 1:
        result = line.split('; tunnel leads to valve ')
    valve_info, connection_info = result
    valve_name_info, flow_rate_info = valve_info.split(' has flow rate=')
    _, valve_name = valve_name_info.split('Valve ')
    flow_rate = int(flow_rate_info)

    connections = connection_info.strip().split(', ')
    valve = ValveNode(valve_name, flow_rate, connections)
    return valve_name, valve


def create_graph(input):
    valve_dict = dict()
    for line in input:
        name, valve = create_valve_node(line)
        valve_dict[name] = valve

    while True:
        done = [False] * len(valve_dict)
        for i, valve in enumerate(valve_dict):
            valve_obj = valve_dict[valve]
            print(list(valve_obj.connections.keys()))
            if len(valve_obj.connections.keys()) == len(valve_dict.keys()) - 1:
                done[i] = True
            else:
                for valve_connected in valve_obj.direct_connection:
                    conn_valve_obj = valve_dict[valve_connected]
                    valve_obj.update_connections(conn_valve_obj)
    
        if all(done):
            break

    return valve_dict





def calculate_pressure(time, valve):
    print(valve.flow_rate)
    return (time - 1) * valve.flow_rate


def dfs(valve_graph):
    pressure_released = 0
    opened = list()
    curr = valve_graph['AA']
    time = 30

    while len(opened) < len(valve_graph) and time > 0:

        valve_list = list()
        for valve in curr.connections:
            if valve in opened:
                continue
            time_cost = curr.connections[valve]

            if time_cost + 1 > time:
                continue
            valve_obj = valve_graph[valve]
            pressure = calculate_pressure(time - time_cost, valve_obj)

            if pressure == 0:
                continue

            valve_list.append((pressure, time_cost + 1, valve_obj))

        if valve_list:
            print(valve_list)
            pressure_relieved, time_cost, valve_obj = max(valve_list)
            pressure_released += pressure_relieved
            curr = valve_obj
            opened.append(valve_obj.name)
            time -= time_cost
        else:
            break

    return pressure_released


valve_graph = create_graph(input)
print(dfs(valve_graph))


