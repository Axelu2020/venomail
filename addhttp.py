with open('proxyy.txt') as f:
    lines = f.readlines()
new_lines = [''.join(["http://", x.strip(), "\n"]) for x in lines]
with open('proxy.txt', 'w') as f:
    f.writelines(new_lines)
