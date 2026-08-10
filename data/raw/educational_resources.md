# Educational Resources Dataset

## Purpose

This file contains the initial educational knowledge base for the AI Educational RAG Assistant.

The information is organized into small, topic-focused sections so that the RAG system can later retrieve relevant information when answering student questions.

---

## 1. Data Structures

### Arrays

An array is a linear data structure that stores elements of the same type in contiguous memory locations.

Common operations on arrays include:
- Traversal
- Insertion
- Deletion
- Searching
- Sorting

The time complexity of accessing an element using its index is generally O(1).

### Linked Lists

A linked list is a linear data structure in which elements are stored in nodes. Each node contains data and a reference to another node.

Common types include:
- Singly linked list
- Doubly linked list
- Circular linked list

Linked lists allow efficient insertion and deletion when the position is known.

---

## 2. Database Management Systems

### Database

A database is an organized collection of data that can be stored, managed, and retrieved efficiently.

### Primary Key

A primary key is an attribute or combination of attributes that uniquely identifies each record in a table.

A primary key:
- Must uniquely identify records
- Cannot contain NULL values
- Helps maintain entity integrity

### Normalization

Normalization is a database design technique used to reduce data redundancy and improve data integrity.

Common normal forms include:
- First Normal Form (1NF)
- Second Normal Form (2NF)
- Third Normal Form (3NF)
- Boyce-Codd Normal Form (BCNF)

---

## 3. Computer Networks

### IP Address

An IP address is a numerical identifier assigned to a device participating in a computer network.

Two commonly discussed versions are:
- IPv4
- IPv6

### HTTP

HTTP (Hypertext Transfer Protocol) is an application-layer protocol used for communication between clients and web servers.

---

## 4. Operating Systems

### Process

A process is a program that is currently being executed by the operating system.

A process has resources such as:
- Program code
- Memory
- CPU state
- Open files

### Deadlock

Deadlock is a situation in which processes are unable to proceed because each process is waiting for a resource held by another process.

The four necessary conditions for deadlock are:
1. Mutual exclusion
2. Hold and wait
3. No preemption
4. Circular wait

---

## 5. Machine Learning

### Machine Learning

Machine learning is a field of artificial intelligence in which algorithms learn patterns from data and use those patterns to make predictions or decisions.

Major types of machine learning include:
- Supervised learning
- Unsupervised learning
- Reinforcement learning

### Supervised Learning

Supervised learning uses labelled training data to learn a relationship between input features and target outputs.

Examples include:
- Classification
- Regression

### Unsupervised Learning

Unsupervised learning works with data that does not have labelled target outputs.

Examples include:
- Clustering
- Dimensionality reduction

---

## 6. Artificial Intelligence

### Artificial Intelligence

Artificial Intelligence (AI) refers to techniques used to develop systems capable of performing tasks that normally require human intelligence.

Examples include:
- Natural language processing
- Computer vision
- Speech recognition
- Decision making

### Natural Language Processing

Natural Language Processing (NLP) focuses on enabling computers to process, understand, and generate human language.

NLP applications include:
- Text classification
- Question answering
- Sentiment analysis
- Machine translation
- Chatbots

---

## 7. Retrieval-Augmented Generation

### RAG

Retrieval-Augmented Generation (RAG) is an approach that combines information retrieval with language generation.

A typical RAG pipeline contains:

1. User query
2. Query embedding
3. Retrieval from a knowledge base
4. Relevant document/context selection
5. Context provided to an LLM
6. Generated response

The retrieval component provides relevant external information to the language model before response generation.

### Vector Embeddings

Embeddings are numerical representations of text that capture semantic information.

Texts with similar meanings can have similar vector representations, allowing semantic similarity search.

### Vector Database

A vector database stores vector representations and supports similarity-based retrieval.

It can be used to retrieve educational content relevant to a student's question.

---

## Dataset Scope

The initial knowledge base focuses on foundational Computer Science and Artificial Intelligence educational topics.

Future versions may include:
- Programming
- Data Structures and Algorithms
- DBMS
- Operating Systems
- Computer Networks
- Machine Learning
- Artificial Intelligence
- NLP
- RAG

## Dataset Status

**Status:** Initial raw knowledge-base preparation

**Project:** AI Educational RAG Assistant

**Purpose:** Initial dataset for Week 2 data preparation and subsequent RAG development
