### **HKS Data Science Bootcamp**
## Welcome to HKS Data Science Bootcamp!

## Week 2

* **Two main kinds of loops**: For Loops & While Loops
* Good Resource
    * [R Loops](https://www.datacamp.com/community/tutorials/tutorial-on-loops-in-r)
    * [Python Loops](https://www.datacamp.com/community/tutorials/loops-python-tutorial)

* General Idea: You want to do a certain set of steps many times or for an entire column in data table
* Why Does It Matter?
      * When you have really big datasets, it is completely crazy to do something for every row in the dataset

* Example: Say you have a table with the GDP Per Capita and Median Life Expectancy for every country in the world but you want to create a separate graph for each country

   * With a loop, you can create a list of continents then have the loop create all 5 plots at once
   
   
Here is R Code to do this:
```R

continent <- c('Africa', 'Americas', 'Asia', 'Europe', 'Oceania')

for (n in continent){
  something <- subset(table1, table1$continent == n)
  plot(something$GdpPerCapita, something$MedianLifeExpectancy)
}
```

* More Complicated Example: Say you are running a K Nearest Neighbors (KNN) Regression model but you don't really know what to choose as a k value 

   * KNN Explanation: KNN divides data into "k" number of groups and then predicts on this number, but it is hard to know what value of k is best)

* To solve this, you might want to run every value of k betweeen 1 and 30, but you don't want to manually write that code 30 times. Here a for loop would be perfect. 

R Code:
```R
    for (k in 1:30) {
      knn_train   <- knn.reg(train = train_data[,-1],
                             test = test_data[,-1],
                             y = train_data[,1],
                             k = k)
      MSE_k[k]    <- mean((knn_train$pred - test_data[,1])^2)
    }
```

* As you can see, it would be very difficult to write the column names if you had hundreds of columns. You would want to do a loop 
