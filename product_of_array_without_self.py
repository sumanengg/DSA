def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            totalProduct = totalProduct * nums[i]
        count = 0
        for num in nums:
            if num == 0:
                count += 1
        answer = []
        if count == 1:
            for num in nums:
                if num == 0:
                    product = totalProduct
                else:
                    product = 0
                answer.append(product)
        elif count > 1:
            answer = [0] * len(nums)
        else:
            for num in nums:
                answer.append(totalProduct // num)
        return answer
