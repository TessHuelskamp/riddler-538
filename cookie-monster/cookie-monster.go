package main

import (
    "fmt"
)

// numbers 0-9
func zeroThrough9(n int) string {
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

func teens(n int) string {
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

func zeroThrough99(n int) string {
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
var cache map[int]string
func zeroThrough999(n int) string {
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

func powersOf1000(n int) string{
    switch n{
    case 0: return ""
    case 1: return "thousand"
    case 2: return "million"
    case 3: return "billion"
    case 4: return "trillion"
    case 5: return "quadrillion"
    case 6: return "qintillion"
    case 7: return "sextillion"
    case 8: return "septillion"
    case 9: return "octillion"
    case 10: return "nonillion"
    case 11: return "decillion"
    case 12: return "undecillion"
    default: panic ("don't know how to count this high")
    }


}

func numberToString(n int) string{
    theSlice:= make([]int,0,10)

    for n>0{
        next := n%1000
        theSlice = append(theSlice, next)
        n/=1000
    }


    return sliceToString(theSlice)

}

//wrapper to convert all numbers (bigger than 0) to a string
func sliceToString(reverseSorted []int) string{
    if len(reverseSorted) <= 0 {
        //cookie monster is 1-indexed:)
        //this isn't the go way of handling errors (I'll learn that later)
        panic ("Cookie monster can only count numbers bigger than 1")
    }

    result:=""

    for power, n := range reverseSorted {
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

func printSlice(reverseSorted []int) string{
    //reverse how we print the string
    return "not done yet"
}


func countClosure(mod int) func() [20]int {
    var toCount [20]int
    max:=mod
    return func() [20]int{
        //add one to beginning
        toCount[0]+=1

        //carry things up if we need to
        for i:=0; i<len(toCount); i++{
            if toCount[i]>=max{
                toCount[i]=0
                if i+1 <len(toCount){
                    toCount[i+1]+=1
                }

            } else {
                break
            }
        }
        return toCount
    }
}



func main() {

 //   tweetLimit:=140
//    prevWinner:=int(1111373000000)
//    prevWinner:=int(1,111,373,000,000)
    //make the global cache
    cache=make(map[int]string)

    highestSeen:=0

    allHighest:= make([]int,0,19)
    allHighest= append(allHighest, 0) //we want to check transitions


    //find the highest we've seen until now.
    //Since we know that for a given entry, we'll find nothing higher until we jump a power of 1000
    //we limit the number of entries we need to check
    for i:=int(1) ; i<=999; i++ {
        result:=numberToString(i)
        if len(result) > highestSeen {
            highestSeen=len(result)
            allHighest = append(allHighest, i)
        }

    }

    testSlice:=[]int{373, 373, 373, 111, 1}

    r:= sliceToString(testSlice)
    fmt.Println(r)
    fmt.Println(len(r))




    incrementer:=countClosure(len(allHighest))

    for i:=1 ; i < 60; i++{
        stuff:=incrementer()
        for i, idx := range(stuff){
            stuff[i]=allHighest[idx]
        }
        fmt.Println(stuff)
        fmt.Println(sliceToString(stuff[:]))
    }
    print(len(allHighest))


    //now we want to actually check things
    //binary search
    //can't do a true binary search but this works


    ///looks like permutions...
    //if all highest is
    // a b c
    // we want to check
    // a, b, c
    // aa, ab, ac
    // ba, bb, bc
    // ca cb cc
    // aaa aab aac
    // aba abb abc
    // aca acb acc

    //not sure a good way to write this
    //if all of the bases of 1000 are in this array, check the number. Otherwise don't
    //it would still be better to build the numbers up somehow

}
