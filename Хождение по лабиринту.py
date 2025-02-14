from a_star import AStarPath
import cv2
import matplotlib.pyplot as plt

show_animation = True


def main():
    start_points = [(30, 30), (170, 175), (50, 100)]  # Начальные точки
    end_points = [(170, 175), (50, 100), (50, 175)]  # Конечные точки
    grid_size = 5.0
    robot_radius = 5.0

    image = cv2.imread("maze2.0.png")
    image = cv2.resize(image, (200, 200))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    (width, length) = gray.shape
    x_obstacle, y_obstacle = [], []
    for i in range(width):
        for j in range(length):
            if gray[i][j] <= 150:
                y_obstacle.append(i)
                x_obstacle.append(j)

    if show_animation:
        plt.figure(figsize=(6, 6))
        plt.plot(x_obstacle, y_obstacle, ".k")
        plt.plot(
            [start[0] for start in start_points],
            [start[1] for start in start_points],
            "og",
            label="Start Points",
        )
        plt.plot(
            [end[0] for end in end_points],
            [end[1] for end in end_points],
            "xb",
            label="End Points",
        )
        plt.legend(loc="lower right")
        plt.grid(True)
        plt.axis("equal")

    for idx, (start_x, start_y) in enumerate(start_points):
        end_x, end_y = end_points[idx]
        a_star = AStarPath(robot_radius, grid_size, x_obstacle, y_obstacle)
        x_out_path, y_out_path = a_star.a_star_search(start_x, start_y,
                                                      end_x, end_y)

        if show_animation:
            plt.plot(x_out_path, y_out_path, label=f"Path {idx + 1}")
            plt.pause(0.001)  # Для обновления графика в реальном времени

    if show_animation:
        plt.legend(loc="lower right")
        plt.show()


main()
