from StrTokenizer import StrTokenizer as st

__precedence={'+':1,'-':1,
              '*':2,"/":2,"%":2,
              "^":3}

def isExpressionValid(expression: str) -> bool:
    """
    Validates an infix expression for correct operator placement and balanced parentheses.

    Parameters:
    expression (str): The infix expression to validate.

    Returns:
    bool: True if the expression is valid, False otherwise.
    """
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string.")
    
    stack=[]
    previous_char=""
    operators=set("+-*/%^")

    for i, current_char in enumerate(expression):
        if current_char=='(':
            stack.append("(")
        elif current_char==')':
            if stack and stack[-1]=='(':
                stack.pop()
            elif not stack or stack[-1]!='(':
                return False
        
        if current_char in operators:
            if i==0:
                return False
            if previous_char in operators:
                return False
        previous_char=current_char
    if stack:
        return False
    if expression[-1] in operators:
        return False
    
    return True

def infixToPostfix(infixexpression: str) -> list[str]:
    """
    Converts an infix expression to a postfix expression.

    Parameters:
    infixexpression (str): The infix expression to convert.

    Returns:
    List[str]: The postfix expression as a list of tokens.
    """
    if not isinstance(infixexpression, str):
        raise TypeError("Infix expression must be a string.")
    
    if not isExpressionValid(infixexpression):
        return []
    infixexpression=infixexpression+')'
    infixexpression2=st(infixexpression,"+-*/%()",True)
    stack=['(',]
    ans=[]
    while infixexpression2.hasMoreTokens():
        i=infixexpression2.nextToken()
        if i in "+-*/()%^":
            if i == '(':
                stack.append(i)
            elif i==')':
                while stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and __precedence.get(stack[-1], 0) >= __precedence[i]:
                    ans.append(stack.pop())
                stack.append(i)
        else:
            ans.append(i)
    if(len(stack)!=0):
        raise TypeError("Wrong expression")
    return ans


def infixToPrefix(infixexpression: str) -> list[str]:
    """
    Converts an infix expression to a prefix expression.

    Parameters:
    infixexpression (str): The infix expression to convert.

    Returns:
    List[str]: The prefix expression as a list of tokens.
    """
    if not isinstance(infixexpression, str):
        raise TypeError("Infix expression must be a string.")
    
    if not isExpressionValid(infixexpression):
        return []
    infixexpression2=st(infixexpression,"+-*/%()",True)
    infixexpression3=[]
    while infixexpression2.hasMoreTokens():
        infixexpression3.append(infixexpression2.nextToken())
    infixexpression3.reverse()

    for i,ch in enumerate(infixexpression3):
        if(ch=='('):
            infixexpression3[i]=')'
        elif(ch==')'):
            infixexpression3[i]='('

    infixexpression3.append(')')
    stack=['(',]
    ans=[]
    for i in infixexpression3:
        if i in "+-*/()%^":
            if i == '(':
                stack.append(i)
            elif i==')':
                while stack[-1]!='(':
                    ans.append(stack.pop())
                stack.pop()
            else:
                while stack and __precedence.get(stack[-1], 0) > __precedence[i]:
                    ans.append(stack.pop())
                stack.append(i)
        else:
            ans.append(i)
    if(len(stack)!=0):
        raise TypeError("Wrong expression")
    return ans[::-1]


def evaluatePostfixExpression(expression: list[str]) -> float:
    """
    Evaluates a postfix expression.

    Parameters:
    expression (List[str]): The postfix expression as a list of string.

    Returns:
    float: The result of evaluating the postfix expression.
    """
    if not isinstance(expression, list):
        raise TypeError("Expression must be a list.")
    
    stack=[]
    for i in expression:
        if i in "+-*/%^":
            if len(stack)>=2:
                a=stack.pop()
                b=stack.pop()
                if i =='+':
                    stack.append(b+a)
                elif i =='-':
                    stack.append(b-a)
                elif i =='*':
                    stack.append(b*a)
                elif i =='/':
                    if a == 0:
                        raise ZeroDivisionError("Division by zero is not allowed")
                    stack.append(b/a)
                elif i =='%':
                    stack.append(b%a)
                elif i =='^':
                    stack.append(b**a)
            else:
                raise TypeError("Wrong expression")
        else:
            try:
                stack.append(float(i))
            except ValueError:
                raise ValueError(f"Invalid operand: {i}")

    if(len(stack)==1):
        return stack[0]
    else:
        raise TypeError("Wrong expression")