//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


func solution(_ s:String) -> [Int] {
    var answer = [Int](repeating: 0, count: 2)
    var temp_str: String = s
    var z_cnt = 0
    var after_size = 0
    var temp_size = 0
    
    while (true)
    {
        temp_size = temp_str.count
        
        if temp_size == 1
        {
            break
        }
        
        z_cnt = 0
        
        for ch in temp_str
        {
            if (ch == "0")
            {
                z_cnt += 1
            }
        }
        
        after_size = temp_size - z_cnt
        
        temp_str = String(after_size, radix: 2)
        
        answer[0] += 1
        answer[1] += z_cnt
    }
    
    return answer
}