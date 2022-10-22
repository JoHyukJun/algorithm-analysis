//
//	main.swift
//
//	Created by Jo Hyuk Jun on 2020.
//	Copyright © 2020 Jo Hyuk Jun. All rights reserved.
//


import Foundation


func findGCD(_ in_a: Int, _ in_b: Int) -> Int {
    var in_a = in_a
    var in_b = in_b
    while (in_b != 0)
    {
        var temp = in_a % in_b
        in_a = in_b
        in_b = temp
    }

    return in_a
}


let n = Int(readLine()!)!
var arr = [Int]()

for i in 0..<n
{
    var temp = Int(readLine()!)!
    arr.append(temp)
}

var gcd: Int = findGCD(arr[1] - arr[0], arr[2] - arr[1])

for i in 2..<(n - 1)
{
    gcd = findGCD(gcd, arr[i + 1] - arr[i])
}

var cnt: Int = ((arr[n - 1] - arr[0]) / gcd) - n + 1

print(cnt)