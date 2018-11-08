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

* Example: Say you want to put a lot 

```R

continent <- c('Africa', 'Americas', 'Asia', 'Europe', 'Oceania')

for (n in continent){
  something <- subset(table1, table1$continent == n)
  plot(something$GdpPerCapita, something$MedianLifeExpectancy)
}
```
