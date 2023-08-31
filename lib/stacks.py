def is_balanced(expression):
    stack = []
    mapper = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top_element = stack.pop()
            if mapper[char] != top_element:
                return False
    
    return not stack