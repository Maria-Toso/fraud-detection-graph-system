# Fraud Detection Graph System

Graph-based fraud detection system using Neo4j, Python and Flask to identify suspicious transaction patterns through relationship analysis.

---

## Overview

This project explores how graph databases can be used to detect potential fraud by analyzing connections between users, cards, devices, IP addresses, merchants, and transactions.

The system models financial behavior as a graph, allowing suspicious patterns to be detected through relationship traversal and graph-based risk analysis.

---

## Core Idea

Fraud is often not visible in isolated transactions.

However, suspicious behavior can appear when analyzing relationships such as:

- Multiple users sharing the same device
- Several cards linked to the same IP address
- Users connected to suspicious merchants
- Transactions occurring through unusual connection patterns
- Dense networks of related accounts and payment methods

This project uses Neo4j to represent these connections and identify potential fraud risks.

---

## Planned Features

- Graph-based fraud relationship modeling
- Suspicious transaction detection
- Risk scoring system
- Cypher queries for fraud pattern analysis
- Flask backend API
- Simple dashboard for visualizing suspicious activity
- Neo4j graph visualization

---

## Technologies

- Python
- Flask
- Neo4j
- Cypher
- HTML
- CSS
- JavaScript

---

## Project Status

In development.
