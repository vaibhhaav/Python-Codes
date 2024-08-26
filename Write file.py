text = "This is new content"
fp = open("write_demo.txt",'w')
fp.write(text)
print('Done Writing')
fp.close()