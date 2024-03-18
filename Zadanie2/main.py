import numpy as np

from drop_wave_function import DropWaveFunction
from evolutionary_algorithm import EvolutionaryAlgorithm
from griewank_function import GriewankFunction
from rastrigin_function import RastriginFunction

drop_wave_function = DropWaveFunction().forward
griewank_function = GriewankFunction().forward
rastrigin_function = RastriginFunction().forward
'''
g(x) - funkcja celu
L - długość chromosomu
mu - rozmiar populacji
sigma - odchylenie standardowe, zasieg mutacji?
p_m - prawdopodobieństwo mutacji
p_c - prawdopodobieństwo krzyżowania
t_max- maksymalną liczbę generacji (pokoleń)
'''
drop_wave_function_evolutionary_algorithm = EvolutionaryAlgorithm(drop_wave_function, 2, 20, 0.1, 0.1, 0.1, 100)
griewank_evolutionary_algorithm = EvolutionaryAlgorithm(griewank_function, 2, 20, 0.1, 0.1, 0.1, 100)
rastrigin_evolutionary_algorithm = EvolutionaryAlgorithm(rastrigin_function, 2, 20, 0.1, 0.1, 0.1, 100)

drop_wave_best_population = drop_wave_function_evolutionary_algorithm.run()
griewank_best_population = griewank_evolutionary_algorithm.run()
rastrigin_best_population = rastrigin_evolutionary_algorithm.run()

visualize(drop_wave_function, drop_wave_best_population, "Drop Wave Function")
visualize(griewank_function, griewank_best_population, "Griewank Function")
visualize(rastrigin_function, rastrigin_best_population, "Rastrigin Function")

if __name__ == "__main__":
    pass
