from pyscript import document

def candidate_checker(e):
    club_members = [
        "cyra cheang",
        "sage aguinaldo",
        "michael barrameda",
        "andrey santos",
        "heather son"
    ]

    f_name = document.getElementById("first_name").value.strip()
    l_name = document.getElementById("last_name").value.strip()

    candidate = f"{f_name} {l_name}".lower()

    if candidate in club_members:
        message = f"Congratulations {f_name} {l_name}, you are part of the Social Studies Club!"
    else:
        message = f"Sorry {f_name} {l_name}, your name is not on the list."

    document.getElementById("result").innerHTML = message