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
