class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')

        for c in path:
            if c=='':
                continue
            elif c ==".":
                continue
            elif c=="..":
                if not stack:
                    continue
                else:
                    stack.pop()
            else:
                stack.append(c)
        
        return '/' + '/'.join(stack)
        