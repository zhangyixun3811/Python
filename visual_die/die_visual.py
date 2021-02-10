from die import Die
import pygal

骰子 = Die()
results = []
for roll_num in range(1000):
    result = 骰子.roll()
    results.append(result)

次数数组 = []
for value in range(1, 骰子.num_sides + 1):
    次数 = results.count(value)
    次数数组.append(次数)

hist = pygal.Bar()

hist.title = "抛6面骰子1000次的结果"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = '结果'
hist._y_title = '次数'

hist.add('D6', 次数数组)
hist.render_to_file('die_visual.svg')
