import numpy as np

from drop_wave_function import DropWaveFunction
from evolutionary_algorithm import EvolutionaryAlgorithm
from griewank_function import GriewankFunction
from rastrigin_function import RastriginFunction
from plot import visualize

def test_mutation():
    # init functions
    drop_wave_function = DropWaveFunction().forward
    griewank_function = GriewankFunction().forward
    rastrigin_function = RastriginFunction().forward

    # parameters
    mu = 50
    p_m = [0.1, 0.5, 0.9]
    p_c = 0.2
    t_max = 100
    '''
    g(x) - funkcja celu
    L - długość chromosomu
    mu - rozmiar populacji
    sigma - odchylenie standardowe, zasieg mutacji?
    p_m - prawdopodobieństwo mutacji                        0.2
    p_c - prawdopodobieństwo krzyżowania                    0.8
    t_max- maksymalną liczbę generacji (pokoleń)
    '''
    for i in p_m:
        # init evolutionary algorithms
        drop_wave_function_evolutionary_algorithm = EvolutionaryAlgorithm(drop_wave_function, 2, mu, 0.1, i, p_c, t_max)
        griewank_evolutionary_algorithm = EvolutionaryAlgorithm(griewank_function, 2, mu, 0.1, i, p_c, t_max)
        rastrigin_evolutionary_algorithm = EvolutionaryAlgorithm(rastrigin_function, 2, mu, 0.1, i, p_c, t_max)

        # run evolutionary algorithms
        drop_wave_best_populations = drop_wave_function_evolutionary_algorithm.run()
        griewank_best_populations = griewank_evolutionary_algorithm.run()
        rastrigin_best_populations = rastrigin_evolutionary_algorithm.run()

        # visualize results
        visualize(drop_wave_function, drop_wave_best_populations, "Drop Wave Function", mu, i, p_c, t_max)
        visualize(griewank_function, griewank_best_populations, "Griewank Function", mu, i, p_c, t_max)
        visualize(rastrigin_function, rastrigin_best_populations, "Rastrigin Function", mu, i, p_c, t_max)

    print("Done with testing mutation values")

def test_crossover():
    drop_wave_function = DropWaveFunction().forward
    griewank_function = GriewankFunction().forward
    rastrigin_function = RastriginFunction().forward

    mu = 50
    p_m = 0.2
    p_c = [0.1, 0.5, 0.9]
    t_max = 100

    for i in p_c:
        drop_wave_function_evolutionary_algorithm = EvolutionaryAlgorithm(drop_wave_function, 2, mu, 0.1, p_m, i, t_max)
        griewank_evolutionary_algorithm = EvolutionaryAlgorithm(griewank_function, 2, mu, 0.1, p_m, i, t_max)
        rastrigin_evolutionary_algorithm = EvolutionaryAlgorithm(rastrigin_function, 2, mu, 0.1, p_m, i, t_max)

        drop_wave_best_populations = drop_wave_function_evolutionary_algorithm.run()
        griewank_best_populations = griewank_evolutionary_algorithm.run()
        rastrigin_best_populations = rastrigin_evolutionary_algorithm.run()

        visualize(drop_wave_function, drop_wave_best_populations, "Drop Wave Function", mu, p_m, i, t_max)
        visualize(griewank_function, griewank_best_populations, "Griewank Function", mu, p_m, i, t_max)
        visualize(rastrigin_function, rastrigin_best_populations, "Rastrigin Function", mu, p_m, i, t_max)

    print("Done with testing crossover values")

def test_population_size():
    drop_wave_function = DropWaveFunction().forward
    griewank_function = GriewankFunction().forward
    rastrigin_function = RastriginFunction().forward

    mu = [20, 100, 500]
    p_m = 0.2
    p_c = 0.8
    t_max = 100

    for i in mu:
        drop_wave_function_evolutionary_algorithm = EvolutionaryAlgorithm(drop_wave_function, 2, i, 0.1, p_m, p_c, t_max)
        griewank_evolutionary_algorithm = EvolutionaryAlgorithm(griewank_function, 2, i, 0.1, p_m, p_c, t_max)
        rastrigin_evolutionary_algorithm = EvolutionaryAlgorithm(rastrigin_function, 2, i, 0.1, p_m, p_c, t_max)

        drop_wave_best_populations = drop_wave_function_evolutionary_algorithm.run()
        griewank_best_populations = griewank_evolutionary_algorithm.run()
        rastrigin_best_populations = rastrigin_evolutionary_algorithm.run()

        visualize(drop_wave_function, drop_wave_best_populations, "Drop Wave Function", i, p_m, p_c, t_max)
        visualize(griewank_function, griewank_best_populations, "Griewank Function", i, p_m, p_c, t_max)
        visualize(rastrigin_function, rastrigin_best_populations, "Rastrigin Function", i, p_m, p_c, t_max)

    print("Done with testing population size values")

def test_max_iteration_size():
    drop_wave_function = DropWaveFunction().forward
    griewank_function = GriewankFunction().forward
    rastrigin_function = RastriginFunction().forward

    mu = 50
    p_m = 0.2
    p_c = 0.8
    t_max = [50, 100, 200]

    for i in t_max:
        drop_wave_function_evolutionary_algorithm = EvolutionaryAlgorithm(drop_wave_function, 2, mu, 0.1, p_m, p_c, i)
        griewank_evolutionary_algorithm = EvolutionaryAlgorithm(griewank_function, 2, mu, 0.1, p_m, p_c, i)
        rastrigin_evolutionary_algorithm = EvolutionaryAlgorithm(rastrigin_function, 2, mu, 0.1, p_m, p_c, i)

        drop_wave_best_populations = drop_wave_function_evolutionary_algorithm.run()
        griewank_best_populations = griewank_evolutionary_algorithm.run()
        rastrigin_best_populations = rastrigin_evolutionary_algorithm.run()

        visualize(drop_wave_function, drop_wave_best_populations, "Drop Wave Function", mu, p_m, p_c, i)
        visualize(griewank_function, griewank_best_populations, "Griewank Function", mu, p_m, p_c, i)
        visualize(rastrigin_function, rastrigin_best_populations, "Rastrigin Function", mu, p_m, p_c, i)

    print("Done with testing iteration size values")