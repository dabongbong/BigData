import numpy as np  # 계산 관련 라이브러리
import pandas as pd # 데이터 분석 관련 라이브러리
import matplotlib.pyplot as plt # 그림 그리기 라이브러리
import seaborn as sns # 이쁜 그림 그리기 라이브러리

# %matplotlib inline

raw = pd.read_excel('titanic.xls')
raw.info()
