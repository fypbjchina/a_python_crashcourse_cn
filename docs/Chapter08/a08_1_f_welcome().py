# a08_1_f_welcome().py
# 定义函数-welcome(): 关键字def

def welcome():
    """问候语""" # 文档字符串 (docstring）的注释，描述了函数是做什么的
    
    hints = "Please kindly enter your name ('quit' for stopping),\n"
    hints += "Your input is:\t"
       
    while True:        
        name = input(hints)
        
        if name.lower() == 'quit':
            break            
        else:
            print(f"Hello, {name.title()}, welcome to join Python-Beginner\n")

welcome()