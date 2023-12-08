#Evolution Art:
#Creating evolutionary art involves using genetic algorithms to evolve visual representations over multiple generations.



import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QImage, QPixmap
import numpy as np
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QHeaderView

class EvolutionaryArtApp(QMainWindow):
    def __init__(self, num_generations, image_size, population_size, mutation_rate, target_pattern):
        super().__init__()

        self.num_generations = num_generations
        self.image_size = image_size
        self.population_size = population_size
        self.target_pattern = target_pattern

        self.setWindowTitle('Evolutionary Art')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.image_label = QLabel()
        self.evolve_button = QPushButton('Evolve')
        self.evolve_button.clicked.connect(self.evolve_images)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.evolve_button)
        self.central_widget.setLayout(layout)

        self.population_table = QTableWidget()
        self.population_table.setColumnCount(3)
        self.population_table.setHorizontalHeaderLabels(['Index', 'Fitness', 'Image'])
        self.population_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)

        layout.addWidget(self.population_table)

        self.mutation_rate = mutation_rate
        self.population = [self.generate_random_image() for _ in range(self.population_size)]
        self.generation = 0

        self.evolve_images()

    def generate_random_image(self):
        return np.random.rand(self.image_size, self.image_size, 3) * 255

    def calculate_fitness(self, image):
        fitness = -np.sum((image - self.target_pattern) ** 2)
        return fitness

    def crossover(self, parent1, parent2):
        crossover_point = np.random.randint(0, len(parent1))
        child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
        return child

    def mutate(self, image):
        mutated_image = image.copy()
        mutation_mask = np.random.rand(*image.shape) < self.mutation_rate

        # Update only in regions where the target pattern is non-zero
        non_zero_mask = (self.target_pattern != 0)
        mutation_mask = np.logical_and(mutation_mask, non_zero_mask)

        mutated_values = np.random.rand(np.count_nonzero(mutation_mask)) * 255
        mutated_image[mutation_mask] = mutated_values

        # Add random shapes during mutation to introduce more details
        mutated_image = self.add_random_shapes(mutated_image)

        return mutated_image

    def add_random_shapes(self, image):
        # Add random circles
        for _ in range(np.random.randint(1, 4)):
            radius = np.random.randint(5, 20)
            center_x, center_y = np.random.randint(radius, self.image_size - radius, size=2)
            color = np.random.rand(3) * 255
            self.draw_circle(image, center_x, center_y, radius, color)

        # Add random squares
        for _ in range(np.random.randint(1, 4)):
            size = np.random.randint(10, 30)
            top_left_x, top_left_y = np.random.randint(size, self.image_size - size, size=2)
            color = np.random.rand(3) * 255
            self.draw_square(image, top_left_x, top_left_y, size, color)

        return image

    def draw_circle(self, image, center_x, center_y, radius, color):
        for i in range(self.image_size):
            for j in range(self.image_size):
                distance = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
                if 0 <= i < self.image_size and 0 <= j < self.image_size and distance <= radius:
                    image[i, j, :] = color

    def draw_square(self, image, top_left_x, top_left_y, size, color):
        for i in range(top_left_x, top_left_x + size):
            for j in range(top_left_y, top_left_y + size):
                if 0 <= i < self.image_size and 0 <= j < self.image_size:
                    image[i, j, :] = color

    def evolve_images(self):
            if self.generation < self.num_generations:
                # Evaluate fitness for each individual in the population
                fitness_values = [self.calculate_fitness(ind) for ind in self.population]

                # Select parents based on fitness
                parents_indices = np.argsort(fitness_values)[-2:]
                parents = [self.population[i] for i in parents_indices]

                # Create offspring through crossover
                offspring = [self.crossover(parents[0], parents[1]) for _ in range(self.population_size - 2)]

                # Mutate offspring
                mutated_offspring = [self.mutate(child) for child in offspring]

                # Replace the old generation with the new generation
                self.population = parents + mutated_offspring

                # Display details to console
                print(f"Generation {self.generation + 1}")
                print(f"  Best Fitness: {max(fitness_values)}")
                print(f"  Average Fitness: {np.mean(fitness_values)}")
                print(f"  Mutation Rate: {self.mutation_rate}")

                # Display the best individual in the current generation
                best_individual = self.population[np.argmax(fitness_values)]
                self.display_image(best_individual)

                # Update the population table
                self.update_population_table(fitness_values)

                self.generation += 1
            else:
                self.evolve_button.setEnabled(False)
                print("Evolution completed.")

    def update_population_table(self, fitness_values):
            self.population_table.setRowCount(len(self.population))

            for i, (fitness, individual) in enumerate(zip(fitness_values, self.population)):
                index_item = QTableWidgetItem(str(i))
                fitness_item = QTableWidgetItem(str(round(fitness, 2)))
                image_item = QTableWidgetItem()  
                self.population_table.setItem(i, 0, index_item)
                self.population_table.setItem(i, 1, fitness_item)
                self.population_table.setItem(i, 2, image_item)

    

    def display_image(self, image):
        # Create a black background
        background = np.zeros((self.image_size, self.image_size, 3), dtype=np.uint8)

        # Set the background to black where the target pattern is zero
        background[self.target_pattern == 0] = 0

        # Merge the image with the target pattern on the background
        merged_image = np.where(self.target_pattern != 0, image, background)

        merged_image = merged_image.astype(np.uint8)

        height, width, channel = merged_image.shape
        bytes_per_line = 3 * width
        q_image = QImage(merged_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)
        pixmap = pixmap.scaledToHeight(400)  # Adjust the height as needed
        self.image_label.setPixmap(pixmap)

def create_target_pattern(image_size):
    target_pattern = np.zeros((image_size, image_size, 3), dtype=np.uint8)

    # Create a circular pattern with random colors
    center_x, center_y = image_size // 2, image_size // 2
    radius = min(center_x, center_y) // 2

    for i in range(image_size):
        for j in range(image_size):
            distance = np.sqrt((i - center_x) ** 2 + (j - center_y) ** 2)
            if distance <= radius:
                target_pattern[i, j, :] = np.random.randint(0, 255, size=3)

    return target_pattern

def main():
    app = QApplication(sys.argv)

    num_generations = int(input("Enter the number of genrations: "))
    image_size = int(input("Enter the image size: "))
    population_size = int(input("Enter the population size: "))
    #mutation rate is for exploration of possible species in a search space
    mutation_rate = float(input("Enter the mutation rate: "))

    # Create a circular pattern with random colors
    target_pattern = create_target_pattern(image_size)

    window = EvolutionaryArtApp(num_generations, image_size, population_size, mutation_rate, target_pattern)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
