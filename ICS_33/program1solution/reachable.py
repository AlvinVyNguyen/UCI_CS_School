import goody
import prompt
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    graph = defaultdict(set)
    for line in open_file:
        s,d = line.strip().split(';')
        graph[s].add(d)
    open_file.close()
    return graph


def graph_as_str(graph : {str:{str}}) -> str:
#     answer =''
#     for s,d in sorted(graph.items()):
#         answer += '  '+s+' -> '+str(sorted(d))+'\n'
#     return answer
    return '\n'.join('  '+s+' -> '+str(sorted(d)) for s,d in sorted(graph.items()))+'\n'

        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    reached, exploring = set(), [start]
    while exploring:
        s = exploring.pop(0)
        reached.add(s)
        for d in graph.get(s,{}):
            if d not in reached:
                exploring.append(d)
    return reached





if __name__ == '__main__':
    graph_file = goody.safe_open('Enter file with graph', 'r', 'Could not find that file')
    graph = read_graph(graph_file)
    print('Graph: source -> {destination} edges\n' + graph_as_str(graph))
    while True:
        start = prompt.for_string('\nEnter starting node name', None, (lambda x : x in graph or x == 'quit'), 'Illegal: not a source node')
        if start == 'quit':
            break
        print('From',start,'the reachable node names are',reachable(graph,start))

    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
