
from collections import deque

class Parentheses:
    def __init__(self, strin, openCount, closeCount):
        self.strin = strin
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):

    result = []
    queue = deque()
    queue.append(Parentheses("", 0,0))

    while queue:
        ps = queue.popleft()

        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.strin)
        else:
            if ps.openCount < num:
                queue.append(Parentheses(ps.strin + "(", ps.openCount+1, ps.closeCount))

            if ps.openCount > ps.closeCount:
                queue.append(Parentheses(ps.strin+ ")", ps.openCount, ps.closeCount+1))

    return result

def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()