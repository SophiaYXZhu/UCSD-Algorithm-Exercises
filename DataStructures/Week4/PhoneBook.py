# python3

class DirectAddressing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def insert(self, key, value):
        if key < 0 or key >= self.size:
            raise ValueError("Key is out of range")
        self.table[key] = value
    
    def delete(self, key):
        if key < 0 or key >= self.size:
            raise ValueError("Key is out of range")
        self.table[key] = None

    def search(self, key):
        if key < 0 or key >= self.size:
            print(key)
            raise ValueError("Key is out of range")
        return self.table[key]

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

# This function simply uses the python dictionary, which also passes the stress tests
def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            try:
                del contacts[cur_query.number]
            except Exception:
                continue
        else:
            try:
                response = contacts[cur_query.number]
            except Exception:
                response = 'not found'
            result.append(response)
    return result

def process_queries_da(queries):
    result = []
    da = DirectAddressing(10**7)
    for cur_query in queries:
        if cur_query.type == 'add':
            da.insert(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            da.delete(cur_query.number)
        else:
            response = da.search(cur_query.number)
            if response == None:
                response = "not found"
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries_da(read_queries()))

