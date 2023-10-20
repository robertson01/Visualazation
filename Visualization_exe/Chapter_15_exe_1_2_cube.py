# Число, возведенное в третью степень, называется «кубом».
# Нанесите на диа-грамму первые пять кубов, а затем первые 5000 кубов.

import matplotlib.pyplot as pt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]
pt.style.use('seaborn-v0_8')
fix, ax = pt.subplots()
ax.scatter(x_values, y_values, c='red', s=200)

# Назначение заголовка диаграммы и меток осей
ax.set_title("График функций", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Назначение размера шрифта, делений на осях.
ax.tick_params(axis='both', labelsize=14)

pt.show()
