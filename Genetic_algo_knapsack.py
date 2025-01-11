import random

class Chromosome:
    def __init__(self, genes, weights, values, weight_limit):
        self.genes = genes
        self.weights = weights
        self.values = values
        self.weight_limit = weight_limit
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self):
        total_weight = 0
        total_value = 0

        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                total_weight += self.weights[i]
                total_value += self.values[i]

        if total_weight <= self.weight_limit:
            self.fitness = total_value
        else:
            self.fitness = 0  

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, generations, weights, values, weight_limit):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.weights = weights
        self.values = values
        self.weight_limit = weight_limit
        self.population = []
        self.initialize_population()

    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            genes=[]
            for i in len (self.weights):
                genes.append(random.randint(0, 1)) 
            chromosome = Chromosome(genes, self.weights, self.values, self.weight_limit)
            self.population.append(chromosome)

    def selection(self):
        total_fitness = 0
        for chromosome in self.population:
            total_fitness += chromosome.fitness

        selection_probabilities = []
        for chromosome in self.population:
            probability = chromosome.fitness / total_fitness
            selection_probabilities.append(probability)
        parents = random.choices(self.population, weights=selection_probabilities, k=2)
        return parents[0], parents[1]

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            # crossover_point = random.randint(1, len(parent1.genes) - 1)
            crossover_point=2
            child1_genes = parent1.genes[:crossover_point] + parent2.genes[crossover_point:]
            child2_genes = parent2.genes[:crossover_point] + parent1.genes[crossover_point:]
            child1 = Chromosome(child1_genes, self.weights, self.values, self.weight_limit)
            child2 = Chromosome(child2_genes, self.weights, self.values, self.weight_limit)
        else:
            child1 = Chromosome(parent1.genes[:], self.weights, self.values, self.weight_limit)
            child2 = Chromosome(parent2.genes[:], self.weights, self.values, self.weight_limit)
        return child1, child2

    def mutate(self, chromosome):
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                chromosome.genes[i] = 1 - chromosome.genes[i]
        chromosome.calculate_fitness()

    def evolve(self):
        for generation in range(self.generations):
            new_population = []
            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection()
                child1, child2 = self.crossover(parent1, parent2)
                self.mutate(child1)
                self.mutate(child2)
                new_population.append(child1)
                new_population.append(child2)
            self.population = new_population[:self.population_size]

    def get_best_solution(self):
        best_chromosome = max(self.population, key=lambda chromo: chromo.fitness)
        return best_chromosome

population_size = 10
mutation_rate = 0.01
crossover_rate = 0.7
generations = 20
weights = [10, 20, 30, 15, 25]   # Item weights
values = [60, 100, 120, 75, 90]  # Item values
weight_limit = 50                # Knapsack weight limit

# Initialize and run GA
ga = GeneticAlgorithm(population_size, mutation_rate, crossover_rate, generations, weights, values, weight_limit)
ga.evolve()

# Get the best solution after running the GA
best_solution = ga.get_best_solution()
print("Best Solution Genes:", best_solution.genes)
print("Best Solution Fitness (Total Value):", best_solution.fitness)
