import random

def initialize_population(pop_size, string_length):
    population = []
    for i in range(pop_size):
        individual = ''
        for j in range(string_length):
            individual += str(random.randint(0, 1)) 
        population.append(individual) 
    return population

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_scores):
    paired_population = list(zip(population, fitness_scores))
    paired_population.sort(key=lambda x: x[1], reverse=True)
    return paired_population[0][0], paired_population[1][0]

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
   new_individual = ''
   for bit in individual:
        if random.random() > mutation_rate:
            new_individual += bit 
        else:
            if bit == '0':
                new_individual += '1'
            else:
                new_individual += '0' 
   return new_individual


def genetic_algorithm(string_length, pop_size, num_generations, mutation_rate):
    population = initialize_population(pop_size, string_length)
    
    for generation in range(num_generations):
        fitness_scores = [calculate_fitness(ind) for ind in population]
        
        if max(fitness_scores) == string_length:
            break 
        
        parent1, parent2 = select_parents(population, fitness_scores)
        new_population = []
        
        for _ in range(pop_size // 2):
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        
        population = new_population[:pop_size]  

    best_solution = max(population, key=calculate_fitness)
    return best_solution, calculate_fitness(best_solution)

string_length = 10
pop_size = 20
num_generations = 100
mutation_rate = 0.01

best_solution, best_fitness = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
print(f"Best solution: {best_solution}, Fitness: {best_fitness}")


string_length = 20
pop_size = 50
num_generations = 100
mutation_rate = 0.05

best_solution, best_fitness = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
print(f"Best solution: {best_solution}, Fitness: {best_fitness}")

string_length = 50
pop_size = 100
num_generations = 100
mutation_rate = 0.1

best_solution, best_fitness = genetic_algorithm(string_length, pop_size, num_generations, mutation_rate)
print(f"Best solution: {best_solution}, Fitness: {best_fitness}")
