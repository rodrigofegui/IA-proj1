from genetic_algorithm import (crossover, fitness,
                               get_initial_generation, get_next_generation,
                               get_total_distance, mutation)
from utils import get_named_route, reached_stability
from variables import GENERATION_MAX

generation = get_initial_generation()

for cnt in range(GENERATION_MAX):
    print('cnt', cnt)

    generation = fitness(generation)

    if reached_stability(generation):
        break

    new_individuals = crossover(generation)
    new_individuals.extend(mutation(generation))

    generation = get_next_generation(generation, new_individuals)

print('best route:')
print(get_named_route(generation[0]))
print(get_total_distance(generation[0]))
#print(mutation(generation))
print(crossover(generation))
