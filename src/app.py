"""
Cloud-Based Secure E-Commerce Analytics and Monitoring System
MSIT Unit 3 - Placeholder Application

This file simulates core modules:
- Authentication
- Product Service
- Order Service
- Event Processing
- Monitoring
"""

from datetime import datetime


# ---------------------------
# AUTH SERVICE
# ---------------------------
def authenticate_user(username: str, password: str) -> dict:
    if username == "admin" and password == "password":
        return {
            "status": "success",
            "token": "sample-jwt-token",
            "message": "User authenticated"
        }
    return {"status": "failed", "message": "Invalid credentials"}


# ---------------------------
# PRODUCT SERVICE
# ---------------------------
def get_products():
    return [
        {"id": 1, "name": "Luxury Dress", "price": 120},
        {"id": 2, "name": "Handbag", "price": 200},
        {"id": 3, "name": "Heels", "price": 150}
    ]


# ---------------------------
# ORDER SERVICE
# ---------------------------
def create_order(user_id, product_id, quantity):
    return {
        "order_id": 101,
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": "Order placed",
        "time": datetime.now().isoformat()
    }


# ---------------------------
# EVENT PROCESSING
# ---------------------------
def process_event(event_name, data):
    return {
        "event": event_name,
        "data": data,
        "processed": True,
        "timestamp": datetime.now().isoformat()
    }


# ---------------------------
# MONITORING
# ---------------------------
def system_health():
    return {
        "api": "healthy",
        "database": "healthy",
        "queue": "healthy",
        "checked_at": datetime.now().isoformat()
    }


# ---------------------------
# MAIN TEST
# ---------------------------
if __name__ == "__main__":
    print("=== System Test Run ===")

    print(authenticate_user("admin", "password"))
    print(get_products())
    print(create_order(1, 2, 1))
    print(process_event("OrderCreated", {"order_id": 101}))
    print(system_health())
