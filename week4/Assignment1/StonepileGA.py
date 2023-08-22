import random

# Read the number of stones and their weights
n = int(input().strip())  # number of stones
weights = list(map(int, input().split()))


# Define the fitness function for a chromosome
def fitness(ch):
    # Calculate the weight of pileA based on the given chromosome
    pileA_weight = sum(weights[i] for i, val in enumerate(ch) if val == 1)
    # Return the inverse of the absolute difference between the weights of the two piles (+1 to avoid division by zero)
    return 1 / (abs(pileA_weight - (sum(weights) - pileA_weight)) + 1)


# Define the Chromosome class
class Chromosome:
    def __init__(self, chrom=None):
        # Initialize a chromosome, either from given list or randomly
        self.chrom = chrom if chrom else [random.randint(0, 1) for _ in range(n)]
        # Calculate the fitness for this chromosome
        self.fit = fitness(self.chrom)


# Define the crossover function to generate offspring from parents
def crossover(parents):
    # Choose a random crossover point
    x = random.randint(0, n - 1)
    # Create two offspring using the crossover point
    offspring1 = parents[0].chrom[:x + 1] + parents[1].chrom[x + 1:]
    offspring2 = parents[1].chrom[:x + 1] + parents[0].chrom[x + 1:]
    return offspring1, offspring2


# Define the mutation function
def mutate(ch):
    # Randomly select a gene and flip it (0 to 1 or 1 to 0)
    i = random.randint(0, n - 1)
    ch[i] = random.randint(0, 1)


# Define the selection function using a stochastic acceptance method
def select(population, total_fitness):
    while True:
        # Randomly select a chromosome
        chosen = random.choice(population)
        # Select the chromosome based on its fitness proportionally
        if random.uniform(0, 1) < chosen.fit / total_fitness:
            return chosen


# Parameters for the genetic algorithm
n_pop = 200
mut_prob = 0.2
max_gen = 1000
plateau_count = 0

# Initialize a random population of chromosomes
population = [Chromosome() for _ in range(n_pop)]
# Sort the population based on their fitness in descending order
population.sort(key=lambda x: x.fit, reverse=True)

# Track the previous and current maximum fitness in the population
old_max = 0
new_max = population[0].fit
gen = 1

# Genetic algorithm main loop
while plateau_count < 5 and gen <= max_gen:
    new_gen = []
    # Calculate the total fitness of the current population
    total_fitness = sum(ch.fit for ch in population)
    for _ in range(n_pop // 2):
        # Select two parents and perform crossover and mutation
        parents = [select(population, total_fitness) for _ in range(2)]
        offspring_chroms = crossover(parents)
        offspring = []
        for chrom in offspring_chroms:
            if random.uniform(0, 1) < mut_prob:
                mutate(chrom)
            offspring.append(Chromosome(chrom))
        new_gen += offspring
    # Merge the old and new generations, and select the top n_pop chromosomes
    population = sorted(population + new_gen, key=lambda x: x.fit, reverse=True)[:n_pop]

    # Track and compare fitness to detect convergence
    old_max = new_max
    new_max = population[0].fit
    if new_max <= old_max:
        plateau_count += 1
    else:
        plateau_count = 0
    gen += 1

# Extract the best solution and compute the two piles
best_chromosome = population[0].chrom
pileA = [weights[i] for i, val in enumerate(best_chromosome) if val == 1]
pileB = [weights[i] for i, val in enumerate(best_chromosome) if val == 0]
difference = abs(sum(pileA) - sum(pileB))

# Print the results
print(f"Weight Difference: {difference}")
print(f"Pile A: {pileA}")
print(f"Pile B: {pileB}")
