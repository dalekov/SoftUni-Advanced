def function(nums: list) -> str:
    nums = list(map(int, nums))
    negatives = [num for num in nums if num < 0]
    positives = [num for num in nums if num > 0]
    string = None

    if abs(sum(negatives)) > sum(positives):
        string = "The negatives are stronger than the positives"
    elif sum(positives) > abs(sum(negatives)):
        string = "The positives are stronger than the negatives"


    return f"{sum(negatives)}\n{sum(positives)}\n{string}" if string else None

nums = input().split()
print(function(nums))
