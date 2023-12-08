# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Rectangle
# import random
# from matplotlib.patches import Ellipse

# # Function to get user preferences
# def get_user_preferences():
#     color = input("Enter your preferred color (red/green/blue/yellow/purple): ")
#     shape = input("Enter your preferred shape (circle/rectangle/triangle/ellipse): ")
#     size = input("Enter your preferred size (small/medium/large): ")

#     return {'color': color, 'shape': shape, 'size': size}

# # Function to initialize population
# def initialize_population(population_size):
#     population = []
#     colors = ['red', 'green', 'blue', 'yellow', 'purple']
#     shapes = ['circle', 'rectangle', 'triangle', 'ellipse']

#     for _ in range(population_size):
#         individual = {
#             'color': random.choice(colors),
#             'shape': random.choice(shapes),
#             'size': random.choice(['small', 'medium', 'large']),
#         }
#         population.append(individual)
#     return population

# # Function to calculate fitness based on user preferences
# def calculate_fitness(individual, user_preferences):
#     fitness = 0
#     for feature, preference in user_preferences.items():
#         if individual[feature] == preference:
#             fitness += 1
#     return fitness

# # Function for crossover (single-point crossover in this example)
# def crossover(parent1, parent2):
#     crossover_point = random.randint(1, len(parent1) - 1)
#     child = {
#         k: parent1[k] if i < crossover_point else parent2[k]
#         for i, k in enumerate(parent1)
#     }
#     return child

# # Function for mutation
# def mutate(individual):
#     mutated_feature = random.choice(list(individual.keys()))
#     mutated_value = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'circle', 'rectangle', 'triangle', 'ellipse', 'small', 'medium', 'large'])
#     individual[mutated_feature] = mutated_value
#     return individual

# # Function to evolve the population
# def evolve_population(population, user_preferences, mutation_rate):
#     population.sort(key=lambda x: calculate_fitness(x, user_preferences), reverse=True)
#     new_population = population[:2]  # Keep the top 2 individuals

#     print(f"Generation {generation + 1} - Best Fitness: {calculate_fitness(new_population[0], user_preferences)}")

#     # Print details of the top individuals in the current population
#     print("Top Individuals:")
#     for i, ind in enumerate(new_population):
#         print(f"   {i + 1}. Fitness: {calculate_fitness(ind, user_preferences)}, Color: {ind['color']}, Shape: {ind['shape']}, Size: {ind['size']}")

#     while len(new_population) < population_size:
#         parent1 = random.choice(population[:10])  # Select from the top 10 individuals
#         parent2 = random.choice(population[:10])
#         child = crossover(parent1, parent2)
#         if random.random() < mutation_rate:
#             child = mutate(child)
#         new_population.append(child)

#     return new_population

# # Function to visualize the best individual in the population
# def visualize_best_individual(population, user_preferences):
#     best_individual = max(population, key=lambda x: calculate_fitness(x, user_preferences))
#     fig, ax = plt.subplots()
#     ax.set_title(f"Best Individual - Fitness: {calculate_fitness(best_individual, user_preferences)}")

#     shape = best_individual['shape']
#     color = best_individual['color']

#     if shape == 'rectangle':
#         ax.add_patch(Rectangle((0.5, 0.5), 1, 1, facecolor=color))
#     elif shape == 'circle':
#         circle = plt.Circle((0.5, 0.5), 0.5, color=color)
#         ax.add_patch(circle)
#     elif shape == 'triangle':
#         triangle = plt.Polygon([(0.5, 0.5), (0.6, 1.5), (0.4, 1.5)], closed=True, facecolor=color)
#         ax.add_patch(triangle)
#     elif shape == 'ellipse':
#         # Use Ellipse from matplotlib.patches
#         ellipse = Ellipse((0.5, 0.5), 1, 0.6, color=color)
#         ax.add_patch(ellipse)

#     plt.axis('equal')
#     plt.show()

# # Main program
# user_preferences = get_user_preferences()
# population_size = int(input("Enter the population size: "))
# num_generations = int(input("Enter the number of generations: "))
# mutation_rate = float(input("Enter the mutation rate (0.0 to 1.0): "))

# # Initial population
# population = initialize_population(population_size)

# # Evolution loop
# for generation in range(num_generations):
#     population = evolve_population(population, user_preferences, mutation_rate)

# # Visualize the best individual after evolution
# visualize_best_individual(population, user_preferences)



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
from matplotlib.patches import Ellipse

# Function to get user preferences
def get_user_preferences():
    color = input("Enter your preferred color (red/green/blue/yellow/purple): ")
    shape = input("Enter your preferred shape (circle/rectangle/triangle/ellipse): ")
    size = input("Enter your preferred size (small/medium/large): ")

    return {'color': color, 'shape': shape, 'size': size}

# Function to initialize population
def initialize_population(population_size):
    population = []
    colors = ['red', 'green', 'blue', 'yellow', 'purple']
    shapes = ['circle', 'rectangle', 'triangle', 'ellipse']

    for _ in range(population_size):
        individual = {
            'color': random.choice(colors),
            'shape': random.choice(shapes),
            'size': random.choice(['small', 'medium', 'large']),
        }
        population.append(individual)
    return population

# Function to calculate fitness based on user preferences
def calculate_fitness(individual, user_preferences):
    fitness = 0
    for feature, preference in user_preferences.items():
        if individual[feature] == preference:
            fitness += 1
    return fitness

# Function for crossover (single-point crossover in this example)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = {
        k: parent1[k] if i < crossover_point else parent2[k]
        for i, k in enumerate(parent1)
    }
    return child

# Function for mutation
def mutate(individual):
    mutated_feature = random.choice(list(individual.keys()))
    mutated_value = random.choice(['red', 'green', 'blue', 'yellow', 'purple', 'circle', 'rectangle', 'triangle', 'ellipse', 'small', 'medium', 'large'])
    individual[mutated_feature] = mutated_value
    return individual

# Function to evolve the population
def evolve_population(population, user_preferences, mutation_rate):
    population.sort(key=lambda x: calculate_fitness(x, user_preferences), reverse=True)
    new_population = population[:2]  # Keep the top 2 individuals

    print(f"Generation {generation + 1} - Best Fitness: {calculate_fitness(new_population[0], user_preferences)}")

    # Print details of the top individuals in the current population
    print("Top Individuals:")
    for i, ind in enumerate(new_population):
        print(f"   {i + 1}. Fitness: {calculate_fitness(ind, user_preferences)}, Color: {ind['color']}, Shape: {ind['shape']}, Size: {ind['size']}")

    while len(new_population) < population_size:
        parent1 = random.choice(population[:10])  # Select from the top 10 individuals
        parent2 = random.choice(population[:10])
        child = crossover(parent1, parent2)
        if random.random() < mutation_rate:
            child = mutate(child)
        new_population.append(child)

    return new_population

# Function to visualize the best individual in the population
def visualize_best_individual(population, user_preferences):
    best_individual = max(population, key=lambda x: calculate_fitness(x, user_preferences))
    fig, ax = plt.subplots()
    ax.set_title(f"Best Individual - Fitness: {calculate_fitness(best_individual, user_preferences)}")

    shape = best_individual['shape']
    color = best_individual['color']

    if shape == 'rectangle':
        ax.add_patch(Rectangle((0.5, 0.5), 1, 1, facecolor=color))
    elif shape == 'circle':
        circle = plt.Circle((0.5, 0.5), 0.5, color=color)
        ax.add_patch(circle)
    elif shape == 'triangle':
        triangle = plt.Polygon([(0.5, 0.5), (0.6, 1.5), (0.4, 1.5)], closed=True, facecolor=color)
        ax.add_patch(triangle)
    elif shape == 'ellipse':
        # Use Ellipse from matplotlib.patches
        ellipse = Ellipse((0.5, 0.5), 1, 0.6, color=color)
        ax.add_patch(ellipse)

    plt.axis('equal')
    plt.show()

# Main program
user_preferences = get_user_preferences()
population_size = int(input("Enter the population size: "))
num_generations = int(input("Enter the number of generations: "))
mutation_rate = float(input("Enter the mutation rate (0.0 to 1.0): "))

# Initial population
population = initialize_population(population_size)

# Evolution loop
for generation in range(num_generations):
    population = evolve_population(population, user_preferences, mutation_rate)

# Visualize the best individual after evolution
visualize_best_individual(population, user_preferences)
