def login_user(username, password):
    # Simple static authentication (for demo)
    valid_username = "admin"
    valid_password = "admin123"

    return username == valid_username and password == valid_password
