---
title: "Designing Data Intensive Applications: Chapter 8, Batch Processing"
date: 2021-01-25
tags: ['software engineering']
categories: ['textbooks']
---

## Motivation

Chapter 8 begins my motivating why batch processing jobs exist. No database meets all of the needs for how we will want to access and interact with our data. Different databases are optimized for different use cases. We will want to move our data from one database to another to unlock different use cases.

Databases can be broken into two categories:

**Systems of record**
- Data is first written here
- Each fact is represented once
- This system always contains the correct data
- Necessary that we have good write performance

**Derived Data Systems**
- We take data and transform it
- Can always be recreated from source data
- Necessary that we have good read performance.

A database is really just a tool. Many different databases can be used to do both of these things. The difference between these types of systems are based on use.

A very common system design is that of request and response. This is how many API's work. The system waits for a request or instructions, handles the request and then returns some response. One way to measure the performance of this kind of system is looking at response time.

Batch processing is different though. There is often a very large amount of input and the job takes a while to run. There should not be a user directly waiting on the output. It is run periodically. We can measure the performance of a batch processing system using through put.

Another type of system which is covered in Chapter 9 is a stream processing system. Stream processing is in between batch and request / response. It consumes an input and makes output. Events are consumed by the system shortly after they happen. This type of system should have much lower latency.

### Unix Example

The textbook provides an example of doing data processing using Unix tools. This example is powerful because it shows how to do batch processing with tools that everyone is familiar with. It also introduces the reader to a lot of principles that will appear in other batch processing systems. The example is the following.

We have a log file that we are appending HTTP requests to. We want to process the logs and make the data available in a different format. In this situation the logs are our system of record and we processing data to make a derived data system. [The Unix Philosophy](https://en.wikipedia.org/wiki/Unix_philosophy) can be written as the following four tenants.
1. Each program does one thing well
2. Output of one program is the input to another
3. Everything should be built to be tried early
4. Use tools rather than unskilled help.

The unix philosophy was developed in 1978 but it sounds a lot like some of the core tenants of agile and devops today. Here are three big themes that we get from unix which we will see in other batch processing systems

- **A uniform interface**: All tools have the same data format as input. With unix it is a file or a file descriptor that contains Ascii text, has lines separated by the same character and has fields separated by spaces, tabs or commas.
- **Separation of logic and wiring**: We take the output from one job and feed it as the input into another. We can build a big system by combining a lot of small tools.
- **Transparency and experimentation**: We can run the same set of commands over and over again and get the same result. We can expect the output of commands at any point in the chain.

But using Unix to do batch processing is limited because it runs on only a single machine...

### Mapreduce and Distributed File Systems (DFS)

Mapreduce and DFS allow us to do processing across many machines. DFS is built on a network service that allows access to files on many different machines. There is a central server that keeps track of locations of all the files. There are replications of files to tolerate machine and disk failure.

Mapreduce is a programming framework to create batch processing jobs. For each job there is both a mapper and reducer function. We will often string together many mapreduce jobs to create one processing job. Mapreduce makes it easy to run code in parallel. The programmer does not have to handle any of the parallelism. The code is copied and sent directly to the machine.
- Mapper function is run once for every record. It can generate more than one key-value pair. Each record is processed independently. That output is then partitioned by key and written to a sorted file.
- Reducer function takes key-value pairs as input. It connects all of the values that have the same key together. It then run a function that reduces all of the keys together.

#### Joins with Mapreduce
Often in data processing jobs we will want to join two different datasets together. But Mapreduce is not natively built to handle that kind of workflow well. There are quite a few different ways to do joins when using mapreduce.

###### Reduce side joins and grouping
To do reduce side joins we will take a copy of the dataset that we want to join and put it into the same file system. We then will bring in that data and records with the same key will be next to each other. The reducer job will then handle the logic of joining the data together. A group by function looks very similar to joining, just the reduce code is executed slightly differently.

Reduce side joins become problematic when our dataset is skewed. This means that some keys have a lot more data than others. We will often have to wait for the slowest reducer to finish to move on in our pipeline. THis slows everything down by having to wait for the one key with a lot of data.

It is possible to run a skewed join to mitigate this impact. We identify the keys that contain a lot of data and we spread our join over multiple reducers. We send all of the data from one side of the join to each job and then random subsets of the other. This way we can divide the join over multiple workers.

##### Map side joins
Reduce sides joins do not make any assumptions about the data. But there can also be a lot of redundancy when we are doing reduce side joins. We are sending a copy of all of the data to every machine. It is possible that we do not need to do that. If we can confidently make certain assumptions about our data we can execute map side joins which should be faster. There is no need to do reducing or sorting.
- **Broadcast Hash Join** - We do a broadcast join when one of our datasets is a lot smaller than the other. We load the entire small dataset in memory in a hash table.
- **Partition Hash Join** - If are datasets are partitioned we can do each join separately. This requires our two datasets to be partitioned in the same way though.

We might not want to do map side joins thought because the data does not get reformated for the next downstream task.

### Output of Batch Workflows

We should never write directly to our database in a reduce job. We should store the data in a filesystem and then have another step in our job that either switches the database over to the new data or appends the data to the end of the table.

Mapreduce is a general purpose structure that can be used in many different ways. It allows the data to be structured in any way. One of the biggest ways mapreduce has unlinked data is we do not need to know how we are going to use the data ahead of time. We can dump data in an unstructured format and then later figure out processing. It shifts the burden of making sense of the data from the producer to the consumer.

Mapreduce is really good when we want to handle large jobs and we have to be good at handling faults. Google designed mapreduce so that machines could be used with shared compute. Rather than having to save compute for high priority tasks, machine can just cancel mapreduce jobs when something more high priority comes in. This achieves better efficiency than having separate compute. But Mapreduce only really makes sense when we have this fault tolerance requirement.

### Beyond MapReduce

Mapreduce can end up being very slow for some types of jobs. It stores output after every job. But with large data processing pipelines we do not need to do that. The output is only being used as input into another part of the job. It is simply intermediate state. Mapreduce also enforces that we have to wait for preceding tasks to finish. It does not let the next jobs start when some data is ready. By requiring a mapper and reduce for every part of the pipeline the mapper can often be redundant.

[Apache Spark](https://spark.apache.org/), [Apache Tez](https://tez.apache.org/) and [Apache Flink](https://flink.apache.org/) are advancements beyond Mapreduce. With all of these approaches we do not need to alternate between map and reduce jobs. They use lazy evaluation to make optimizations at run time. They do not always require sorting of data.

These new advancements are not as good at handling fault tolerance though. They will often require re-computing data and therefore it is important we make operators deterministic.


## Closing thoughts

This chapter did a good job motivating the current landscape of analytics and how to transition from a production database to an analytics database. It covered the history of data processing going from unix, to map reduce to current improvements on map reduce.

One of the key insights for me from this chapter was that google built mapreduce because they had high fault tolerance needs. But for most data processing jobs that is not actually the need. Mapreduce is a helpful conceptual framework, but it should not be used for most use cases today.





