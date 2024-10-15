from StrTokenizer import StrTokenizer as st

__precedence={'+':1,'-':1,
              '*':2,"/":2,"%":2,
              "^":3}

def isExpressionValid(expression):
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

def infixToPostfix(infixexpression):
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