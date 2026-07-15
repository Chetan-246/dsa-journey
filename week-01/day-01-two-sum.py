"""
Problem: 167. Two Sum II - Input Array Is Sorted
Pattern: Two Pointers
Date: 2026-07-15
Time Taken: 30 mins
Mistakes: Tried hash map first, forgot array is sorted
Key Insight: Sorted array → two pointers from ends
"""

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # No solution found


# Test
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(twoSum([2, 3, 4], 6))        # [1, 3]
