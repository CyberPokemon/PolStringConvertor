
# PolStringConvertor

PolStringConvertor is a Python package that provides utilities to convert infix expressions into postfix and prefix forms, and to evaluate postfix expressions. It also includes validation of infix expressions.

## Features

- Validate infix expressions for proper operator placement and balanced parentheses.
- Convert infix expressions to postfix notation.
- Convert infix expressions to prefix notation.
- Evaluate postfix expressions.

## Installation

To install the package, use pip:

```bash
pip install PolStringConvertor
```

This package requires the `StrTokenizer` package version 1.1.0 to function properly. It will be installed automatically when you install `PolStringConvertor`.

## Usage

Here’s how to use the main features of the package:

### 1. Validate an Infix Expression

```python
from PolStringConvertor import isExpressionValid

expression = "(a+b)*c"
print(isExpressionValid(expression))  # Returns True or False
```

### 2. Convert Infix to Postfix

```python
from PolStringConvertor import infixToPostfix

expression = "(a+b)*c"
postfix = infixToPostfix(expression)
print(postfix)  # Output: ['a', 'b', '+', 'c', '*']
```

### 3. Convert Infix to Prefix

```python
from PolStringConvertor import infixToPrefix

expression = "(a+b)*c"
prefix = infixToPrefix(expression)
print(prefix)  # Output: ['*', '+', 'a', 'b', 'c']
```

### 4. Evaluate a Postfix Expression

```python
from PolStringConvertor import evaluatePostfixExpression

postfix = ['3', '4', '+', '2', '*', '7', '/']
result = evaluatePostfixExpression(postfix)
print(result)  # Output: 2.0
```

### 5. Import All Functions at once

```python
from PolStringConvertor import *

expression = "(a+b)*c"
print(isExpressionValid(expression))  # Returns True or False

postfix = infixToPostfix(expression)
print(postfix)  # Output: ['a', 'b', '+', 'c', '*']

prefix = infixToPrefix(expression)
print(prefix)  # Output: ['*', '+', 'a', 'b', 'c']

postfix = ['3', '4', '+', '2', '*', '7', '/']
result = evaluatePostfixExpression(postfix)
print(result)  # Output: 2.0

```

You can install the `PolStringConvertor` package from PyPI:

[Install StrTokenizer from PyPI](https://pypi.org/project/PolStringConvertor/1.0.0/)

## Source Code:

[Github Link](https://github.com/CyberPokemon/PolStringConvertor)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
