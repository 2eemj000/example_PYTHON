from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
import os
print(f"현재경로 : ${os.getcwd()}")


path = Path('the_csv_file_format/weather_data/sitka_weather_2021_simple.csv') # 경로 맞춰주기
lines = path.read_text().splitlines() # 파일을 읽어서 모든 행을 리스트로 변환해 lines에 할당함
# (lines는 리스트)
reader = csv.reader(lines) # lines를 reader객체로 만듦 (각 행을 분석), 일종의 커서같은 기능 
# (reader도 리스트로 간주 : 차이는 reader도 객체이지만 리스트를 갖고있고 커서개념을 가짐)
header_row = next(reader) # next함수 : 파일의 처음부터 시작해 다음행으로 진행 # 한번만 호출했으니까 header가 포함된 첫행이 반환, 그 데이터를 header_row에 할당
# ["STATION","NAME","DATE","TAVG","TMAX","TMIN"] 이렇게!

# Extract dates and high temperatures.
dates, highs = [], [] # 날짜와 최고기온을 저장할 빈 리스트 두개 생성
for row in reader: # 윗줄부터 차례로 아랫줄로 내려오면서
    current_date = datetime.strptime(row[2], '%Y-%m-%d') # row[2]데이터를 datetime 객체로 변환해서 dates에 추가함
    high = int(row[4]) # 네번째 column 값을 줌
    dates.append(current_date)
    highs.append(high)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red') # 날짜와 최고기온을 plot()에 전달

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # 날짜가 겹치지 않게 대각선으로 그림
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
