def is_balanced(expression):
    stack = []
    bracket_mapping = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack:
                return False
            top_element = stack.pop()
            if bracket_mapping[char] != top_element:
                return False
    
    return not stack