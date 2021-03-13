//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


func solution(_ seoul:[String]) -> String {
    var answer: String = ""
    var location: Int = 0
    
    for s in seoul
    {
        if (s == "Kim")
        {
            answer += "김서방은 " + String(location) + "에 있다"
        }
        
        location += 1
    }
    
    return answer
}