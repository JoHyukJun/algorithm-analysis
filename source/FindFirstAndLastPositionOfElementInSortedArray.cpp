//
//	main.cpp
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


/*
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
*/


class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> output;
        
        int head = 0;
        int tail = nums.size() - 1;
        int input_size = nums.size();
        
        if (input_size == 0) {
            output.push_back(-1);
            output.push_back(-1);
            return output;
        }
        else if (input_size == 1) {
            if (nums[0] == target) {
                output.push_back(0);
                output.push_back(0);
                return output;
            }
            else {
                output.push_back(-1);
                output.push_back(-1);
                return output;
            }
        }
        
        while (head <= tail) {
            if (nums[head] <= target) {
                if (nums[head] == target) {
                    output.push_back(head);
                    head += 1;
                }
                else {
                    head += 1;
                }
            }
            else if (nums[tail] >= target) {
                if (nums[tail] == target) {
                    output.push_back(tail);
                    tail -= 1;
                }
                else {
                    tail -= 1;
                }
            }
            else {
                break;
            }
        }
        
        if (output.size() == 0) {
            output.push_back(-1);
            output.push_back(-1);
        }
        else if (output.size() == 1) {
            output.push_back(output[0]);
        }
        
        vector<int> res;
        res.push_back(output[0]);
        res.push_back(output[output.size() - 1]);
        
        return res;
    }
};