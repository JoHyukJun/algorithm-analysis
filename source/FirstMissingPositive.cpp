/*
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
*/


class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int output = 1;
        int input_size = nums.size();
        
        if (input_size == 0) {
            return output;
        }
        else if (input_size == 1) {
            if (nums[0] <= 0 || nums[0] > 1) {
                return output;
            }
            else if (nums[0] == 1) {
                output += 1;
                
                return output;
            }
            
        }
        
        int head = 0;
        bool isOK = true;
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < input_size; i++) {
            if (nums[i] > 0) {
                head = i;
                break;
            }
            else {
                head = i;
            }
        }
        
        if (head == input_size - 1) {
            if (nums[head] > 1) {
                return output;
            }
            else if(nums[head] == 1) {
                output += 1;
                
                return output;
            }
            return output;
        }
        
        while (isOK) {
            
            if (nums[head] > output) {
                return output;
            }
            else if (nums[head] == output) {
                output += 1;
            }
            else if (nums[head] < output) {
                head += 1;
            }
            
            
            if (head == input_size - 1) {
                if (nums[head] < output) {
                    return output;
                }
            }
        }
        
        output += 1;
        
        return output;
    }
};