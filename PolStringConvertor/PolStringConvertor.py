from StrTokenizer import StrTokenizer as st

__precedence={'+':1,'-':1,
              '*':2,"/":2,"%":2,
              "^":3}

def infixToPostfix(infixexpression):
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