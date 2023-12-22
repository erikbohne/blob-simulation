import pygame

class DataAnalysis:
    def __init__(self):
        self.data = {
            'average_speed': [],
            'blobs': [],
            'foods': [] 
        }

    def collect_data(self, blobs):
        if blobs:
            
            # Average speed
            average_speed = sum(blob.speed for blob in blobs) / len(blobs)
            self.data['average_speed'].append(average_speed)
            
            # Blobs
            self.data['blobs'].append(len(blobs))

    def draw_graph(self, screen, max_data_points=1000):
        graph_x, graph_y = 600, 10  # Top-right corner
        graph_width, graph_height = 200, 100

        pygame.draw.rect(screen, (0, 0, 0), (graph_x, graph_y, graph_width, graph_height))

        if len(self.data['average_speed']) > 1:
            max_value = max(max(self.data['average_speed'][-max_data_points:]), max(self.data['blobs'][-max_data_points:]))
            min_value = min(min(self.data['average_speed'][-max_data_points:]), min(self.data['blobs'][-max_data_points:]))
            value_range = max_value - min_value if max_value - min_value else 1
            prev_x, prev_y_speed = graph_x, graph_y + graph_height
            prev_y_blobs = graph_y + graph_height

            for i, (speed, blobs) in enumerate(zip(self.data['average_speed'][-max_data_points:], self.data['blobs'][-max_data_points:])):
                x = graph_x + (i / max_data_points) * graph_width
                y_speed = graph_y + graph_height - ((speed - min_value) / value_range) * graph_height
                y_blobs = graph_y + graph_height - ((blobs - min_value) / value_range) * graph_height
                pygame.draw.line(screen, (0, 0, 255), (prev_x, prev_y_speed), (x, y_speed))
                pygame.draw.line(screen, (255, 0, 0), (prev_x, prev_y_blobs), (x, y_blobs))
                prev_x, prev_y_speed, prev_y_blobs = x, y_speed, y_blobs
