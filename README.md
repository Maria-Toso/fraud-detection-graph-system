# Fraud Detection Graph System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask)
![Neo4j](https://img.shields.io/badge/Neo4j-008CC1?style=for-the-badge&logo=neo4j&logoColor=white)
![Cypher](https://img.shields.io/badge/Cypher-1F6FEB?style=for-the-badge)

---

A fullstack graph-based fraud detection prototype built with Neo4j, Flask, and Python to identify suspicious transaction patterns through relationship analysis and graph traversal techniques.

---

## Overview

This project explores how graph databases can be used to detect potential fraud by analyzing relationships between users, cards, devices, IP addresses, merchants, and transactions.

Instead of analyzing transactions in isolation, the system models financial behavior as a connected graph structure, enabling suspicious patterns to be detected through relationship traversal and graph analytics.

The project demonstrates how graph databases can improve fraud detection systems by identifying hidden connections and behavioral anomalies.

---

## Dashboard Preview

<p align="center">
  <img src="assets/dashboard-preview.png"/>
</p>

---

## Fraud Detection API Example

<p align="center">
  <img src="assets/api-preview.png"/>
</p>

---

## Core Idea

Fraud is often difficult to detect when transactions are analyzed individually.

However, suspicious activity becomes more visible when analyzing relationships such as:

- Multiple users sharing the same device
- Several cards linked to the same IP address
- Users connected to suspicious merchants
- Abnormal transaction relationship patterns
- Dense networks of related accounts and payment methods

This project uses Neo4j graph modeling to represent these relationships and identify potential fraud risks through connected data analysis.

---

## Features Implemented

- Transaction relationship modeling with Neo4j
- Shared device fraud detection
- Graph-based suspicious activity analysis
- Flask API integration
- Interactive fraud monitoring dashboard
- Cypher-based relationship queries
- Connected data exploration

---

## Architecture

The system is structured into three main layers:

### Backend Layer
- Flask API handling fraud analysis endpoints
- Data processing and transaction loading
- Fraud detection service logic

### Database Layer
- Neo4j graph database for connected data modeling
- Relationship traversal using Cypher queries
- Fraud pattern analysis through graph structures

### Frontend Layer
- Interactive dashboard interface
- Suspicious activity visualization
- Fraud monitoring cards and alerts

Transactions are transformed into graph relationships, enabling efficient exploration of suspicious behavioral patterns.

---

## Graph Model

The graph structure represents entities and relationships such as:

### Nodes
- Users
- Cards
- Devices
- IP Addresses
- Transactions
- Merchants

### Relationships
- `OWNS_CARD`
- `USES_DEVICE`
- `CONNECTED_TO`
- `USED_IN`
- `SENT_TO`

This structure enables advanced fraud analysis through graph traversal and relationship exploration.

---

## Features

- Graph-based fraud relationship modeling
- Suspicious device detection
- Shared relationship analysis
- Fraud monitoring dashboard
- Cypher query analysis
- Connected transaction exploration
- Backend API services
- Relationship traversal logic

---

## Technologies

- Python
- Flask
- Neo4j
- Cypher
- HTML
- CSS
- JavaScript
- Docker

---

## API Endpoints

| Endpoint | Description |
| --- | --- |
| `/load-data` | Loads transaction data into Neo4j |
| `/suspicious-devices` | Detects suspicious shared devices |
| `/dashboard` | Fraud monitoring dashboard |

---

## Project Structure

```txt
fraud-detection-graph-system/
│
┣ assets/
┣ data/
┣ docs/
┣ src/
┃ ┣ services/
┃ ┣ templates/
┃ ┣ static/
┃ ┣ app.py
┃ ┗ database.py
│
┣ requirements.txt
┣ .env.example
┗ README.md
```

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Maria-Toso/fraud-detection-graph-system.git
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Start Neo4j with Docker

```bash
docker run --name neo4j-fraud \
-p 7474:7474 \
-p 7687:7687 \
-e NEO4J_AUTH=neo4j/password123 \
-d neo4j:5
```

---

### 4. Create a `.env` file

```env
NEO4J_URI=bolt://localhost:7687
NEO4J_USERNAME=neo4j
NEO4J_PASSWORD=password123
```

---

### 5. Run the application

```bash
python src/app.py
```

---

### 6. Load sample data

Access:

```txt
/load-data
```

---

### 7. Open the dashboard

Access:

```txt
/dashboard
```

---

## Future Improvements

- Fraud risk scoring engine
- Real-time transaction monitoring
- Advanced graph analytics
- Interactive Neo4j visualization
- Authentication system
- Docker Compose integration
- Cloud deployment
- Machine learning fraud analysis
- Real-time alert system

---

## Project Status

Active development with core fraud detection and graph analysis features already implemented.

---

## Author

Maria Eduarda Toso
