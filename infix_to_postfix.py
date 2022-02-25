"""
convert an infix mathematical expression to postfix expression and evaluate the answer
"""

def infix_to_postfix(expr: str) -> list:
    prec = {"+":0,"-":0,"*":1,"/":1,"(":2 }
    operations = tuple("()+-/*")
    numbers = tuple("0123456789.")
    
    postfix_stack = []
    operator_stack = ['(']
    num = ""
    for c in expr:
        if c in numbers:
            num += c
        elif c in operations:
            # if any number was accumulated, then save it in the stack
            if num:
                postfix_stack.append(num)
                num = ""
            
            # if closing brace is encountered, then pop all operators until opening brace in encountered
            if c==")":
                while operator_stack and operator_stack[-1] != '(':
                    postfix_stack.append(operator_stack.pop())
                # remove opening brace as well
                operator_stack.pop()
            
            # else if precedence of the operator is less or equal to previous operator in stack, 
            # then pop all until opening brace or operator with lesser precedence is encountered
            elif prec[operator_stack[-1]] >= prec[c]:
                while (operator_stack and 
                       operator_stack[-1] != '(' and 
                       prec[operator_stack[-1]] >= prec[c]):
                    postfix_stack.append(operator_stack.pop())
                operator_stack.append(c)
            
            # if an operator with more precedence is encountered then just push to op_stack
            elif (not operator_stack) or prec[operator_stack[-1]] <= prec[c]:
                operator_stack.append(c)
        else:
            if num:
                postfix_stack.append(num)
                num = ""
            
    if num:
        postfix_stack.append(num)
    while operator_stack and operator_stack[-1] != '(':
        postfix_stack.append(operator_stack.pop())
            
    
    return postfix_stack

def find_first_operator(expr: list) -> int:
    for i, v in enumerate(expr):
        if v in "+-/*":
            return i 

def evaluate_postfix_expression(expr: list) -> float:
    while len(expr) > 1:
        operator_index = find_first_operator(expr)
        if operator_index:
            if expr[operator_index] == "*":
                result = float(expr[operator_index-2]) * float(expr[operator_index-1])
            elif expr[operator_index] == "/":
                result = float(expr[operator_index-2]) / float(expr[operator_index-1])
            if expr[operator_index] == "+":
                result = float(expr[operator_index-2]) + float(expr[operator_index-1])
            if expr[operator_index] == "-":
                result = float(expr[operator_index-2]) - float(expr[operator_index-1])
        else:
            raise Exception("Invalid expression")
        expr[operator_index-2:operator_index+1] = [str(result)]
    return expr[0]

  
if __name__=="__main__":
  out = evaluate_postfix_expression(infix_to_postfix("1+2*3+4"))
  print(out)
