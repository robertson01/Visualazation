from plotly.graph_objs import  Bar, Layout
from plotly import offline

from Chapter_15_exe_6_die import Die

# Создание кубика D6
die = Die(8)
die_2 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке
results = []
for roll_num in range(110000):
    result = die.roll() + die_2.roll()
    results.append(result)

# Анализ результатов
frequencies = []
max_result = die.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Визуализация результатов.
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 50000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')