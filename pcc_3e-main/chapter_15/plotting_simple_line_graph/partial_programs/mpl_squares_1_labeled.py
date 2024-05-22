# 임포트한걸 plt라고 부르겠다
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

# fig는 박스창, ax는 축을 따라 그리는 그래프, fig와 ax는 변수, plt는 객체
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

plt.show()