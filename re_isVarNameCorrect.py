import re

def main():
    name=input("请输入一个变量名：")
    ret= re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$",name)
    if ret:
        print("您输入的变量名%s合法" % name)
    else:
        print("您输入的变量名%s不合法"% name)


if __name__ == "__main__":
    main()
