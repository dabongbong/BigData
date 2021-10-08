install.packages("ggplot2")

library(ggplot2)

x <- c("a","a","b","c")
x

qplot(x)

qplot(data= mpg, x=hwy)

qplot(data = mpg, x=drv, y=hwy)
qplot(data = mpg, x=drv, y=hwy, geom = "boxplot", colour=drv)

std <- c(80,60,70,50,90)
std

avg <- mean(std)
avg

df_mid <- data.frame(eng = c(90, 80, 60, 70),
                    math = c(50,60,90,30),
                    class = c(1,1,2,2))
df_mid

install.packages("readxl")
library(readxl)
exam <- read_excel("excel_exam.xlsx")

head(df_exam)
tail(exam)
dim(exam)
str(exam)

mpg <- as.data.frame(ggplot2::mpg)
install.packages("dplyr")
library(dplyr)

df_mid <- rename(df_mid, v2 = eng)
df_mid
mpg_new <- mpg
mpg_new$test <- ifelse(mpg_new$total >= 20,"pass","fail")
