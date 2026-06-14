/**
448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]


 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdlib.h>

int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    
    int *result = (int *)malloc(numsSize * sizeof(int));
    int k = 0;

    // Mark visited numbers
    for (int i = 0; i < numsSize; i++) {
        int index = abs(nums[i]) - 1;
        if (nums[index] > 0)
            nums[index] = -nums[index];
    }

    // Find missing numbers
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] > 0)
            result[k++] = i + 1;
    }

    *returnSize = k;
    return result;
}
