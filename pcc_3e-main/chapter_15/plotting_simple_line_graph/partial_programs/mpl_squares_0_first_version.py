# matplotlib 설치
# python -m pip install --user matplotlib
# 구글드라이브 코랩

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()