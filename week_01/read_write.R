# Read iris dataset and store as df
df <- read.csv('iris.csv')

# Write df object and save as iris2.csv
write.csv(df, 'iris2,csv', row.names = FALSE)
