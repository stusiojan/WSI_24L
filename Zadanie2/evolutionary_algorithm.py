import numpy as np

class EvolutionaryAlgorithm:
    '''
    Na podstawie wykładu algorytm ewolucyjny powinien zawierać:
    g(x) - funkcję celu
    P_0 - populację początkową
    L - długość chromosomu
    mu - rozmiar populacji
    sigma - odchylenie standardowe
    p_m - prawdopodobieństwo mutacji
    p_c - prawdopodobieństwo krzyżowania
    t_max- maksymalną liczbę generacji (pokoleń)
    '''
    def __init__(self, gain_function, L, mu, sigma, p_m, p_c, t_max):
        self.function = gain_function
        self.chromosome_length = L
        self.population_size = mu
        self.sigma = sigma # odchylenie standardowe
        self.mutation_probability = p_m
        self.crossover_probability = p_c
        self.max_generations = t_max

    def fitness_function(self, x, function):
        # odleglosc od optimum
        return self.function(x)

    def mutation_operator(self, x: np.ndarray, p):
        # mutacja gaussowska
        # x = x + sigma * N(0, 1)
        if np.random.rand() < p:
            x = x + np.random.normal(0, self.sigma, self.chromosome_length)
        return x

    def crossover_operator(self, x1: np.ndarray, x2: np.ndarray, p):
        # krzyżowanie jednopunktowe
        # srednia wazona
        if np.random.rand() < p:
            # crossover_point = np.random.randint(0, self.chromosome_length)  # czy hardcodować 1?
            # for i in range(crossover_point, self.chromosome_length):
            #     x1[i], x2[i] = x2[i], x1[i]
            x1[0] = (x1[0] + x2[0]) / 2
            x2[0] = (x1[1] + x2[1]) / 2
            x1[1] = (x1[1] + x2[1]) / 2
            x2[1] = (x1[0] + x2[0]) / 2
        return x1, x2


    def initalize_population(self, population_size, chromosome_length):
        p_0 = np.random.rand(self.population_size, self.chromosome_length)
        return p_0

    def select_parents(self, population, fitness):
        parents = []
        for i in range(len(population)):
            parents.append(population[np.argmin(fitness)])
            fitness[np.argmin(fitness)] = 999999999999999999
        return parents

    def survivor_selection(self, population, fitness):
        # turniejowa reprodukcja
        survivors = np.array([])
        for i in range(self.population_size):
            survivors = np.append(survivors, population[np.argmin(fitness)], axis=0)
            fitness[np.argmin(fitness)] = 999999999999999999
        survivors = survivors.reshape(self.population_size, self.chromosome_length)
        return survivors


    def run(self):
        generations = []
        '''
        1.  Initialize population
        2.  Evaluate each individual (fitness function)
        3.  Repeat until termination condition is met or max generations is reached:
            a.  Select parents
            b.  Crossover
            c.  Mutate
            d.  Evaluate each individual
            e.  Select survivors
        '''
        # 1st step
        population = self.initalize_population(self.population_size, self.chromosome_length)

        # 2nd step
        fitness = []
        for individual in population:
            fitness.append(self.fitness_function(individual, self.function))
        
        # 3rd step
        for generation in range(self.max_generations):
            fitness = []
            for individual in population:
                fitness.append(self.fitness_function(individual, self.function))
            parents = self.select_parents(population, fitness)

            for i in range(len(parents)):
                successors = self.crossover_operator(parents[i], parents[len(parents)-i-1], self.crossover_probability)
            population = np.append( population, successors, axis=0)

            mutants = np.array([])
            for i in range(len(parents)):
                mutant = self.mutation_operator(parents[i], self.mutation_probability,)
                mutants = np.append(mutants, mutant, axis=0)
            mutants = mutants.reshape(len(parents), self.chromosome_length)
            population = np.append(population, mutants, axis=0)

            fitness = []
            for individual in population:
                fitness.append(self.fitness_function(individual, self.function))
            population = self.survivor_selection(population, fitness)

            parents = np.array([])
            generations.append(population)
        
        return generations