import numpy as np

class EvolutionaryAlgorithm:
    # Na podstawie wykładu algorytm ewolucyjny powinien zawierać:
    # - funkcję celu
    # - długość chromosomu
    # - rozmiar populacji
    # - maksymalną liczbę generacji (pokoleń)
    # - prawdopodobieństwo krzyżowania
    # - prawdopodobieństwo mutacji
    def __init__(self, function, chromosome_length=2, population_size=100, max_generations=1000, crossover_probability=0.8, mutation_probability=0.1):
        self.function = function
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.max_generations = max_generations
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

    # główne metody algorytmu ewolucyjnego:
    def fitness(self, x, function):
        # return value of evaluation function
        return self.function.forward(x)

    def mutation_operator(self, x, p):
        # return from propability p a new chromosome(x[0], x[1]) for mutation
        # jak wyznaczyć prawdopodobieństwo mutacji?
        return x

    def crossover_operator(self, x1, x2, p):
        # return from propability p two chromosomes for crossover and crossover probability
        # jak wyznaczyć prawdopodobieństwo krzyżowania?
        # losowo wybrany inny osobnik z populacji, ale to w algorytmie
        return x1, x2

    # metody pomocnicze
    def initalize_population(self, population_size):
        # return n random chromosomes or return n from domain
        return np.random.rand(population_size, self.chromosome_length)
