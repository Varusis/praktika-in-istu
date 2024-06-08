
import matplotlib.pyplot as plt


def koch_curve(order, p1, p2):
    if order == 0:
        return [p1, p2]
    else:
        x1, y1 = p1
        x2, y2 = p2
        dx, dy = (x2 - x1) / 3, (y2 - y1) / 3
        p3 = (x1 + dx, y1 + dy)
        p5 = (x1 + 2 * dx, y1 + 2 * dy)

        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        px, py = mx + (y1 - y2) * (3 ** 0.5) / 6, my + (x2 - x1) * (3 ** 0.5) / 6
        p4 = (px, py)

        return (
                koch_curve(order - 1, p1, p3)[:-1] +
                koch_curve(order - 1, p3, p4)[:-1] +
                koch_curve(order - 1, p4, p5)[:-1] +
                koch_curve(order - 1, p5, p2)
        )


def plot_koch_curve(order):
    p1 = (0, 0)
    p2 = (1, 0)

    points = koch_curve(order, p1, p2)
    x, y = zip(*points)

    plt.figure(figsize=(10, 10))
    plt.plot(x, y, 'b-')
    plt.axis('equal')
    plt.title(f'Кривая Коха {order} порядка')
    plt.show()

#здесь в скобках указывать какого порядка нужен фрактла
plot_koch_curve(8)
