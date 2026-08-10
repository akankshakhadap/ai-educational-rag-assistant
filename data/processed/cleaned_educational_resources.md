# Cleaned Educational Resources

## Dataset Purpose

This file contains the cleaned and structured version of the initial educational knowledge base prepared for the AI Educational RAG Assistant.

The data has been organized into topic-based sections to make it easier to split the content into chunks and retrieve relevant information during the RAG process.

---

## Document 1: Data Structures

### Topic
Data Structures

### Content

An array is a linear data structure that stores elements of the same type in contiguous memory locations.

Common array operations include traversal, insertion, deletion, searching, and sorting.

Accessing an array element using its index generally takes O(1) time.

A linked list is a linear data structure consisting of nodes. Each node contains data and a reference to another node.

Common types of linked lists are singly linked lists, doubly linked lists, and circular linked lists.

---

## Document 2: Database Management Systems

### Topic
Database Management Systems

### Content

A database is an organized collection of data that can be stored, managed, and retrieved efficiently.

A primary key is an attribute or combination of attributes that uniquely identifies a record in a table. A primary key cannot contain NULL values.

Normalization is a database design technique used to reduce data redundancy and improve data integrity.

Common normal forms include First Normal Form (1NF), Second Normal Form (2NF), Third Normal Form (3NF), and Boyce-Codd Normal Form (BCNF).

---

## Document 3: Computer Networks

### Topic
Computer Networks

### Content

An IP address is a numerical identifier assigned to a device participating in a computer network.

IPv4 and IPv6 are two commonly used versions of the Internet Protocol.

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between clients and web servers.

---

## Document 4: Operating Systems

### Topic
Operating Systems

### Content

A process is a program that is currently being executed by an operating system.

A process uses resources such as program code, memory, CPU state, and open files.

Deadlock is a situation in which processes cannot proceed because each process is waiting for a resource held by another process.

The four necessary conditions for deadlock are mutual exclusion, hold and wait, no preemption, and circular wait.

---

## Document 5: Machine Learning

### Topic
Machine Learning

### Content

Machine learning is a field of artificial intelligence in which algorithms learn patterns from data and use those patterns to make predictions or decisions.

The major types of machine learning include supervised learning, unsupervised learning, and reinforcement learning.

Supervised learning uses labelled training data. Classification and regression are common supervised learning tasks.

Unsupervised learning works with data without labelled target outputs. Clustering and dimensionality reduction are examples.

---

## Document 6: Artificial Intelligence and NLP

### Topic
Artificial Intelligence

### Content

Artificial Intelligence refers to techniques used to develop systems capable of performing tasks that normally require human intelligence.

Natural Language Processing focuses on enabling computers to process, understand, and generate human language.

NLP applications include text classification, question answering, sentiment analysis, machine translation, and chatbots.

---

## Document 7: Retrieval-Augmented Generation

### Topic
Retrieval-Augmented Generation

### Content

Retrieval-Augmented Generation (RAG) combines information retrieval with language generation.

A typical RAG pipeline includes a user query, query embedding, retrieval from a knowledge base, selection of relevant context, providing the context to a language model, and generating a response.

Embeddings are numerical representations of text that capture semantic information.

A vector database stores vector representations and supports similarity-based retrieval.

---

## Data Preparation Status

- Raw educational content collected
- Content organized by topic
- Duplicate and unnecessary formatting removed
- Content converted into structured documents
- Data prepared for future chunking and embedding

## Intended Next Step

The processed documents will later be divided into smaller chunks and converted into vector embeddings for retrieval by the RAG system.
