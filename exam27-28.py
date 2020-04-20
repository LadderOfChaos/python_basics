tickets_count = int(input())
for ticket in range(tickets_count):
    ticket_number = input()
    ticket_number_len = len(ticket_number)
    if ticket_number_len == 4:
        first_char_ascii = ord(ticket_number[0])
        if first_char_ascii >= 65 and first_char_ascii <= 90:
            seat += ticket_number[0]
            seat += ticket_number[1]
            seat += ticket_number[2]

print(seat)
    #elif ticket_number_len == 5 or ticket_number_len == 6:
