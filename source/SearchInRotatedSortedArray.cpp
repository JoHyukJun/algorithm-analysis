//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2012.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


/*
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
*/


class Solution {
public:
    int search(vector<int>& nums, int target) {
        int output = -1;
        
        int head = 0;
        int tail = nums.size() - 1;
        
        int input_size = nums.size();
        
        if (input_size == 0) {
            return output;
        }
        else if (input_size == 1) {
            if (nums[0] == target) {
                output = 0;
                
                return output;
            }
            else {
                return output;
            }
        }
        
        while(head <= tail) {
            if (nums[head] <= target) {
                if (nums[head] == target) {
                    return head;
                }
                else {
                    head += 1;
                }
            }
            else if (nums[tail] >= target) {
                if (nums[tail] == target) {
                    return tail;
                }
                else {
                    tail -= 1;
                }
            }
            else {
                head += 1;
                tail -= 1;
            }
        }
        
        return output;    
    }
};