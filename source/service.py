# creating a dummy database

database = {
    1: "All Systems Red",
    2: "Artificial Condition",
    3: "Rogue Protocol"
}


def get_user_from_db(user_id):

    return database.get(user_id)
