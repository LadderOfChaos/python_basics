whiskey = float(input())
bira_litri = float(input())
whine_litri = float(input())
rakia_litri = float(input())
whiskey_litri = float(input())

rakia_price = whiskey / 2
whine_price = rakia_price - (rakia_price * 0.4)
beer_price = rakia_price - (rakia_price * 0.8)
total = (rakia_price * rakia_litri) + (whine_price * whine_litri) + (beer_price * bira_litri) + (whiskey*whiskey_litri)

print(f"{total:.2f}")