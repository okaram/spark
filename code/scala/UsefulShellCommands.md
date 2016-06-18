Useful Spark Shell commands
===

## Changing log levels
```
sc.setLogLevel("WARN")
```

Or "INFO", "DEBUG" ... 

## Super simple example
```scala
sc.parallelize(1.to(1000) ).collect()  
```
