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
        self.sigma = sigma
        self.mutation_probability = p_m
        self.crossover_probability = p_c
        self.max_generations = t_max

    def fitness_function(self, x, function):
        return self.function(x)

    def mutation_operator(self, x, p):
        # return from propability p a new chromosome(x[0], x[1]) for mutation
        # jak wyznaczyć prawdopodobieństwo mutacji?
        return x

    def crossover_operator(self, x1, x2, p):
        # return from propability p two chromosomes for crossover and crossover probability
        # return punkt pośredni między x1 a x2
        # jak wyznaczyć prawdopodobieństwo krzyżowania?
        # losowo wybrany inny osobnik z populacji, ale to w algorytmie
        return x1, x2


    def initalize_population(self, population_size, chromosome_length):
        p_0 = np.random.rand(self.population_size, self.chromosome_length)
        return p_0

    def select_parents(self, population, fitness):
        parents = []
        for i in range(2):
            parents.append(population[np.argmin(fitness)])
            fitness[np.argmin(fitness)] = 999999999999999999
        return parents

    def survivor_selection(self, population, fitness):
        survivors = []
        for i in range(self.population_size):
            survivors.append(population[np.argmin(fitness)])
            fitness[np.argmin(fitness)] = 999999999999999999
        return survivors


    def run(self):
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
        print('Initial population: ')
        print(population)

        # 2nd step
        fitness = []
        for individual in population:
            fitness.append(self.fitness_function(individual, self.function))
        print('Initial population fitness: ')
        print(fitness)
        
        # 3rd step
        for generation in range(self.max_generations):
            parents = self.select_parents(population, fitness) # wybieram tylko 2 rodziców
            population = np.append( population, (self.crossover_operator(parents[0], parents[1], self.crossover_probability)))
            population = np.append( population, (self.mutation_operator(population[np.argmin(fitness)], self.mutation_probability))) # jak wybrać osobnika do mutacji?
            # populacja rosnie z x do x+2
            for individual in population:
                self.fitness_function(individual, self.function)
            population = self.survivor_selection(population, fitness)
        
        return self.population