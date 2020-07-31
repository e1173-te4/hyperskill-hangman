my_text = input()
to_delete = [',', '.', '!', '?']
for i in to_delete:
    my_text = my_text.replace(i, '')
print(my_text.lower())