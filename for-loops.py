a = int(input())
b = int(input())
c = int(input())
d = int(input())
for top_left in range(a, b + 1):
    for top_right in range(a, b + 1):
        for bot_left in range(c, d + 1):
            for bot_right in range(c, d + 1):
                first_diagonal = top_left + bot_right
                second_diagonal = top_right + bot_left

                are_equal =first_diagonal == second_diagonal

                are_top = top_right != top_left
                are_bot = bot_right != bot_left

                if are_equal and are_top and are_bot:
                    print(f"{top_left}{top_right}\n{bot_left}{bot_right}")
                    print()