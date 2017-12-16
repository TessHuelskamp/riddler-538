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

func zeroThrough999(n uint64) string {
    if n<0 || n>=1000 { panic ("Function requires 0<=1<1000") }

    hundreds := n/100
    remainder := n%100
    if hundreds ==0{
        return zeroThrough99(n)
    } else {
        if remainder==0{
           return zeroThrough9(hundreds) + " hundred"
        } else {
           return zeroThrough9(hundreds) + " hundred " + zeroThrough99(n%100)
        }
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

    power1000:=0

    for n >0 {
        power1000++
        //nextEntry:=n%1000
        n/=1000

    }


    return ""


}


func main(){

    for i:=uint64(1) ; i<=math.MaxInt64; i++ {
        if i > 10  {
            break
        }
    }

    testing :=[]uint64 {1, 3, 12314, 123421124134}

    for _, entry := range testing {
        numberToString(entry)
    }

    for i:=uint64(0) ; i<=999; i++ {
        result:=zeroThrough999(i)

        if result == "" { result="empty"
        } else { result= "'"+ result + "'" }

        fmt.Println(result)

    }
}
