package main

import (
    "fmt"
    "math"
)
// numbers 0-9
func zeroThrough9(n uint64) string {
    if n<0 || n>=10 { panic ("Function requires 0<=1<10:") }

    switch n {
    case 0: return ""
    case 1: return "one"
    case 2: return "two"
    case 3: return "three"
    case 4: return "four"
    case 5: return "five"
    case 6: return "six"
    case 7: return "seven"
    case 8: return "eight"
    case 9: return "nine"
    default: panic ("invalid number passed in")
    }
}

func teens(n uint64) string {
    if n<10 || n>=20 { panic ("Function requires 0<=1<100") }

    switch n {
    case 10: return "ten"
    case 11: return "eleven"
    case 12: return "twelve"
    case 13: return "thirteen"
    case 14: return "fourteen"
    case 15: return "fifteen"
    case 16: return "sixteen"
    case 17: return "seventeen"
    case 18: return "eighteen"
    case 19: return "nineteen"
    default: panic ("invalid number passed in")
    }
}

func zeroThrough99(n uint64) string {
    if n<0 || n>=100 { panic ("Function requires 0<=1<100") }

    ones := n%10
    tens := n/10
    intermediate := ""
    switch tens{
    case 0: return zeroThrough9(n)
    case 1: return teens(n)
    case 2: intermediate="twenty"
    case 3: intermediate="thirty"
    case 4: intermediate="fourty"
    case 5: intermediate="fifty"
    case 6: intermediate="sixty"
    case 7: intermediate="seventy"
    case 8: intermediate="eighty"
    case 9: intermediate="ninety"
    default: panic ("invalid number passed in")
    }

    if tens==0 || ones==0 {
        return intermediate
    } else {
        return intermediate + " " + zeroThrough9(ones)
    }
}

var global string
var cache map[uint64]string
func zeroThrough999(n uint64) string {
    if n<0 || n>=1000 { panic ("Function requires 0<=1<1000") }

    hundreds := n/100
    remainder := n%100

    if result, ok := cache[n]; ok{
        return result
    } else {
        if hundreds ==0{
            result=zeroThrough99(n)
        } else {
            if remainder==0{
               result=zeroThrough9(hundreds) + " hundred"
            } else {
               result=zeroThrough9(hundreds) + " hundred " + zeroThrough99(n%100)
            }
        }
        cache[n]=result
        return result
    }

}

func powersOf1000(n uint64) string{
    switch n{
    case 0: return ""
    case 1: return "thousand"
    case 2: return "million"
    case 3: return "billion"
    case 4: return "trillion"
    case 5: return "quadrillion"
    case 6: return "quintillion"
    case 7: return "sextillion"
    case 8: return "septillion"
    case 9: return "octillion"
    case 10: return "nonillion"
    case 11: return "decillion"
    case 12: return "undecillion"
    default: panic ("don't know how to count this high")
    }


}

//wrapper to convert all numbers (bigger than 0) to a string
func numberToString(n uint64) string{
    if n <= 0 {
        //cookie monster is 1-indexed:)
        //this isn't the go way of handling errors (I'll learn that later)
        panic ("Cookie monster can only count numbers bigger than 1")
    }

    power:=uint64(0)
    result:=""

    for n >0 {
        nextEntry:=n%1000
        n/=1000
        if nextEntry!=0{
            if power==0{
                result = zeroThrough999(nextEntry)
            } else if result=="" {
                result = zeroThrough999(nextEntry) + " " + powersOf1000(power)
            } else {
                result = zeroThrough999(nextEntry) + " " + powersOf1000(power) + " " + result
            }

        }

        power++

    }


    //don't forget the "!"
    return result+"!"


}


func main() {

    tweetLimit:=140
    prevWinner:=uint64(1111373000000)

    highest:=0
    var allHighest []int
    for i:=uint64(1) ; i<=999; i++ {
        result:=numberToString(i)
        if len(result) > highest {
            highest=len(result)
            allHighest = append(allHighest, highest)
            fmt.Println(i)
            fmt.Println(result)
        }
    }

    //binary search
    //can't do a true binary search but this works

}




