budget = float(input())
season = input()
destination = ""
type = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        type = "Camp"
    elif season == "winter":
        budget *= 0.7
        type = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
        type = "Camp"
    elif season == "winter":
        budget *= 0.8
        type = "Hotel"
elif budget > 1000:
    destination = "Europe"
    budget *= 0.9
    type = "Hotel"
print (f"Somewhere in {destination}\n{type} - {budget:.2f}")