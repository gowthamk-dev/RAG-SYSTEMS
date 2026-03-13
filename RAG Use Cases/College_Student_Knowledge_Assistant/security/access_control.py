def check_access(user_role, document):

    if document.get("restricted") and user_role != "admin":
        return False

    return True
