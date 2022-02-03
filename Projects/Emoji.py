msg = input('>')
split_list = msg.split()

emojis = {
    ':)':'🙂',
    ':(':'☹',
    ':|':'😐'
}
output = ""
for x in split_list:
    output += emojis.get(x,x) + " "
print(output)