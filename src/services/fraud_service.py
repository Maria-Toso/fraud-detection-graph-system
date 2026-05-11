import json
from src.database import db


def load_transactions():

    with open("data/sample_transactions.json", "r") as file:
        transactions = json.load(file)

    query = """
    MERGE (u:User {id: $user_id, name: $user_name})
    MERGE (c:Card {id: $card_id})
    MERGE (d:Device {id: $device_id})
    MERGE (ip:IP {address: $ip_address})
    MERGE (m:Merchant {name: $merchant})

    CREATE (t:Transaction {
        amount: $amount,
        status: $status
    })

    MERGE (u)-[:OWNS_CARD]->(c)
    MERGE (u)-[:USES_DEVICE]->(d)
    MERGE (u)-[:CONNECTED_TO]->(ip)

    CREATE (c)-[:USED_IN]->(t)
    CREATE (t)-[:SENT_TO]->(m)
    """

    for transaction in transactions:
        db.execute_query(query, transaction)

    return {
        "message": "Transactions loaded successfully",
        "transactions": len(transactions)
    }