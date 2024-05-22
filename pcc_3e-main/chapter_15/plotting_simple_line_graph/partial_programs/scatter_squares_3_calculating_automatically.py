import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# Set chart title and label axes. (그래프 타이틀, 축 이름표)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels. (축 기준들 label 폰트크기)
ax.tick_params(labelsize=14)

# Set the range for each axis. (각 축의 범위 지정, [x축최소,x축최대,y축최소,y축최대])
ax.axis([0, 1100, 0, 1_100_000])

plt.show()