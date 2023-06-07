def largestRectangle(heights):
    heights.append(0) # 마지막에 스택에 남아있는 막대들을 처리하기 위한 '더미' 높이 추가
    stack = []
    max_area = 0
    
    for i, height in enumerate(heights):
        print(i)
        while stack and (heights[stack[-1]] > height):
            h = heights[stack.pop()]
            w = i if not stack else i-stack[-1]-1
            print(h, w)
            max_area = max(max_area, h*w)
        stack.append(i)
        print(stack)
    
    return max_area

heights = list(map(int, input().split()))
print(largestRectangle(heights))
