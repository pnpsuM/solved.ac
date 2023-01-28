import sys

num_pokemon, num_query = tuple(map(int, sys.stdin.readline().split()))
pokedict_name = {}
pokedict_index = {}
for index in range(1, num_pokemon + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokedict_index[index] = pokemon
    pokedict_name[pokemon] = index
    
for query in range(num_query):
    query = sys.stdin.readline().rstrip()
    try:
        query = int(query)
    except: # string
        print(pokedict_name[query])
    else:
        print(pokedict_index[query])