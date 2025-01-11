import random

class Chromosome:
    def __init__(self, genes, distance_matrix):
        self.genes = genes  # A list representing the order of cities
        self.distance_matrix = distance_matrix
        self.fitness = 0
        self.calculate_fitness()

    def calculate_fitness(self):
        total_distance = 0
        for i in range(len(self.genes)):
            # Add distance from the current city to the next city
            total_distance += self.distance_matrix[self.genes[i]][self.genes[(i + 1) % len(self.genes)]]

        # Lower distances are better, so fitness is the inverse of total distance
        self.fitness = 1 / total_distance if total_distance > 0 else 0

class GeneticAlgorithm:
    def __init__(self, population_size, mutation_rate, crossover_rate, generations, distance_matrix):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.generations = generations
        self.distance_matrix = distance_matrix
        self.population = []

    def initialize_population(self):
        self.population = []
        # Generate initial population of chromosomes
        for _ in range(self.population_size):
            genes = list(range(len(self.distance_matrix)))  # Genes are the indices of cities
            random.shuffle(genes)  # Randomly shuffle cities for the initial tour
            chromosome = Chromosome(genes, self.distance_matrix)
            self.population.append(chromosome)

    def selection(self):
        # Calculate total fitness
        total_fitness = sum(chromosome.fitness for chromosome in self.population)

        # Select two parents based on their fitness
        selection_probabilities = [chromosome.fitness / total_fitness for chromosome in self.population]
        parents = random.choices(self.population, weights=selection_probabilities, k=2)
        return parents[0], parents[1]

    def crossover(self, parent1, parent2):
        if random.random() < self.crossover_rate:
            # Pick two crossover points
            start, end = sorted(random.sample(range(len(parent1.genes)), 2))
            child_genes = [-1] * len(parent1.genes)  # Create empty child genes
            child_genes[start:end] = parent1.genes[start:end]  # Copy genes from parent1
            
            # Fill remaining genes from parent2
            pointer = 0
            for gene in parent2.genes:
                if gene not in child_genes:
                    while child_genes[pointer] != -1:
                        pointer += 1
                    child_genes[pointer] = gene

            child1 = Chromosome(child_genes, self.distance_matrix)
        else:
            child1 = Chromosome(parent1.genes[:], self.distance_matrix)  # No crossover, copy parent1

        return child1

    def mutate(self, chromosome):
        # Mutate the chromosome by swapping two genes
        for i in range(len(chromosome.genes)):
            if random.random() < self.mutation_rate:
                j = random.randint(0, len(chromosome.genes) - 1)
                chromosome.genes[i], chromosome.genes[j] = chromosome.genes[j], chromosome.genes[i]

        # Recalculate fitness after mutation
        chromosome.calculate_fitness()

    def evolve(self):
        for generation in range(self.generations):
            new_population = []

            while len(new_population) < self.population_size:
                parent1, parent2 = self.selection()
                child = self.crossover(parent1, parent2)
                self.mutate(child)
                new_population.append(child)

            self.population = new_population[:self.population_size]

    def get_best_solution(self):
        best_chromosome = max(self.population, key=lambda chromosome: chromosome.fitness)
        return best_chromosome

# Example distance matrix for TSP
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Parameters
population_size = 10
mutation_rate = 0.01
crossover_rate = 0.7
generations = 20

# Initialize and run GA
ga = GeneticAlgorithm(population_size, mutation_rate, crossover_rate, generations, distance_matrix)
ga.initialize_population()
ga.evolve()

# Get the best solution after running the GA
best_solution = ga.get_best_solution()
print("Best Solution Genes (Order of Cities):", best_solution.genes)
print("Best Solution Fitness (Inverse of Distance):", best_solution.fitness)
