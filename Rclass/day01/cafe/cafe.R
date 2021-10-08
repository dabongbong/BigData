install.packages("readxl")
library(readxl)

sales = read_xlsx("Cafe_Sales.xlsx")
head(sales)

head(sales)
tail(sales)
dim(sales)
str(sales)
summary(sales)
View(sales)

is.na(sales)


table(is.na(sales))
table(is.na(sales$order_id))
table(is.na(sales$order_date))

sales <- na.omit(sales)
table(is.na(sales))


head(sales)

head(sales,20)

unique(sales$order_date)
unique(sales$price)

table(sales$item)
sort(table(sales$item))

sort(table(sales$item), decreasing = TRUE)

sales_tr <- data.frame(table(sales$item))
sales_tr

sales_item <- subset.data.frame(sales, select = c("item","price"))
sales_item
sales_item <- unique(sales_item)
sales_item

item_list = merge(sales_tr, sales_item, by.x = "Var1", by.y = "item")
item_list

item_list$amount = item_list$Freq * item_list$price
item_list

sum(item_list$amount)
