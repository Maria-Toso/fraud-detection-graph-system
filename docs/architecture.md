# System Architecture

## Overview

The system uses a graph database approach to model financial relationships and identify suspicious fraud patterns.

---

## Main Entities

- Users
- Credit Cards
- Devices
- IP Addresses
- Transactions
- Merchants

---

## Relationship Modeling

Examples of graph relationships:

- USER_USES_DEVICE
- USER_OWNS_CARD
- CARD_USED_IN_TRANSACTION
- TRANSACTION_SENT_TO_MERCHANT
- USER_CONNECTED_TO_IP

---

## Fraud Detection Logic

Potential fraud indicators include:

- Shared devices between unrelated accounts
- Multiple cards linked to the same IP
- Abnormal transaction patterns
- Dense relationship clusters
- High-risk transaction paths

---

## Technologies

- Flask backend
- Neo4j graph database
- Cypher query analysis
- Graph traversal techniques