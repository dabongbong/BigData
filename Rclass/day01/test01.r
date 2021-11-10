version
library(stringr)
1+1
var1 <- 0
var1
goods.code <-'a001'
goods.name <- '냉장고'
goods.name
goods.code

a <- c(1,2,'3')
a
result <-as.integer(a) *3
result
mode(a)
mode(result)

gender <- c("man", "woman", "woman","man", "man")

plot(gender)

ngender <- as.factor(gender)
plot(ngender)
table(ngender)

class(ngender)
is.factor(ngender)

ogender <- factor(gender, levels=c("woman","man"), ordered=T)

par(mfrow=c(1,2))
plot(ngender)
plot(ogender)




help(mean)
args(mean)
args(max)

example(seq)

getwd()

c(1:20)

seq(2,10,2)
rep(1:3, each = 3)
rep(1:3, 3)

v1 <- c(1,2,3,4,5)
v1; mode(v1); class(v1)

age<- c(30,40,50)
age
names(age) <- c("홍길동","이순신","강감찬")
age

a <- c(1:50)
a[10:45]

v1 <- c(13, -5, 20:23, 12, -2:3)
v1

v1[c(2,4)]
v1[c(3:5)]

v1[c(4, 5:8, 7)]

v1[-1]]
v1[-c(24)]
library(RSADBE)

data(Severity_Counts)
str(Severity_Counts)

