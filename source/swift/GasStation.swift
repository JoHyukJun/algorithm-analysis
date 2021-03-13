//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


var n = Int(readLine()!)!
var dist = [Int]()
dist = readLine()!.split(separator: " ").map{ Int($0)! }
var price = [Int]()
price = readLine()!.split(separator: " ").map{ Int($0)! }

var dp = Array(repeating: 0, count: 100001)
dp[0] = dist[0] * price[0]

var temp_min: Int = price[0]

dist.append(0)

for i in 1..<n
{
    if price[i] < temp_min
    {
        temp_min = price[i]
    }

    dp[i] = dp[i - 1] + (temp_min * dist[i])
} 

print(dp[n - 1])