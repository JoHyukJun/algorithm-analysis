//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


func solution(_ s:String) -> String {
    var answer: String = ""
    let basis: Int = s.count
    
    if basis % 2 == 0
    {
        answer += String(s[s.index(s.startIndex, offsetBy: ((basis / 2) - 1))])
        answer += String(s[s.index(s.startIndex, offsetBy: (basis / 2))])
    }
    else
    {
        answer += String(s[s.index(s.startIndex, offsetBy: (basis / 2))])
    }
    
    return answer
}