import random
class Chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self):
        weights = [10, 20, 30, 15, 25]
        values = [60, 100, 120, 75, 90]
        knapsack_weight_limit = 50

        total_weight = 0
        total_value = 0

        for i in range(len(self.genes)):
            if self.genes[i] == 1: 
                total_weight += weights[i] 
                total_value += values[i]   
        
        if total_weight <= knapsack_weight_limit:
            self.fitness = total_value
        else:
            self.fitness = 0
class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, generations):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.population = []
    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            genes = []
            for i in range(5):
                genes.append(random.randint(0, 1)) 
            chromosome = Chromosome(genes)
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

            child1 = Chromosome(child1_genes)
            child2 = Chromosome(child2_genes)
        else:
            child1 = Chromosome(parent1.genes[:])
            child2 = Chromosome(parent2.genes[:])

        return child1, child2
    def mutate(self, chromosome):
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                if chromosome.genes[i] == 0:
                    chromosome.genes[i] = 1  
                else:
                    chromosome.genes[i] = 0 
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
        best_chromosome = self.population[0]
        for chromosome in self.population:
            if chromosome.fitness > best_chromosome.fitness:
                best_chromosome = chromosome

        return best_chromosome


population_size = 10
mutation_rate = 0.01
crossover_rate = 0.7
generations = 20

ga = GeneticAlgorithm(population_size, mutation_rate, crossover_rate, generations)
ga.initialize_population()
ga.evolve()

best_solution = ga.get_best_solution()
print("Best Solution Genes:", best_solution.genes)
print("Best Solution Fitness (Value):", best_solution.fitness)
