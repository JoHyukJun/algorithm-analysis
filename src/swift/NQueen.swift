//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


var answer: Int = 0


func ckr(_ in_arr:[Int], _ index:Int) -> Bool {
    for i in 0..<index
    {
        if (in_arr[i] == in_arr[index])
        {
            return false
        }
        
        if (abs(in_arr[i] - in_arr[index]) == abs(i - index))
        {
            return false
        }
    }
    
    return true
}


func mkr(_ in_arr:[Int], _ cnt:Int) {
    var arr = in_arr
    
    if (cnt == in_arr.count)
    {
        answer += 1
        
        return
    }
    
    for i in 0..<arr.count
    {
        arr[cnt] = i
        
        if (ckr(arr, cnt))
        {
            mkr(arr, cnt + 1)
        }
    }
    
    return
}


func solution(_ n:Int) -> Int {
    let org = [Int](repeating: 0, count: n)
    mkr(org, 0)
    
    return answer
}