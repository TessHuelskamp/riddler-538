package main

import (
    "fmt"
    "strconv"
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

    if tens==0 || ones==0 { return intermediate
    } else { return intermediate + " " + zeroThrough9(ones) }
}

//yes this a global var but I wasn't sure how to deal with this in go
var cache map[int]string
func zeroThrough999(n int) string {
    if n<0 || n>=1000 { panic ("Function requires 0<=1<1000") }

    // if we've already calculated the number, return it
    if result, ok := cache[n]; ok{ return result }

    result:=""
    hundreds := n/100
    remainder := n%100

    if hundreds==0{
        result=zeroThrough99(n)
    } else if remainder ==0 {
       result=zeroThrough9(hundreds) + " hundred"
    } else {
       result=zeroThrough9(hundreds) + " hundred " + zeroThrough99(n%100)
    }

    //store and return result
    cache[n]=result
    return result
}

func powersOf1000(n int) string{
    switch n {
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
    default: panic ("Don't know how to count this high")
    }


}

// wrapper to convert all numbers (bigger than 0) to a string
// reverseSorted is a number that's broken down into powers of 1000
//
// to contruct number do:
// sequence[0]*1000^1 + sequence[1]*1000^2 + ... + sequence[n-1]*1000^n
func SliceToString(reverseSorted []int) string{
    if len(reverseSorted) == 0 { panic ("empty slice passed in") }

    result:=""

    //build up the answer walking along the number
    for power, entry := range reverseSorted {
        if entry==0{ //do nothing
        } else if  power==0 {
            result = zeroThrough999(entry)
        } else if result=="" {
            result = zeroThrough999(entry) + " " + powersOf1000(power)
        } else {
            result = zeroThrough999(entry) + " " + powersOf1000(power) + " " + result
        }
    }

    //don't forget the "!"
    return result+"!"
}

//print a reverse sorted slice like an int
func printSlice(reverseSorted []int) string{
    //while the last entry is=0, remove the last element
    for reverseSorted[len(reverseSorted)-1]==0 {
        reverseSorted=reverseSorted[:len(reverseSorted)-1]
    }

    //reconstruct element from right to left
    result:=""
    for i, entry := range reverseSorted{

        //don't pad if we're last digit or if we're bigger than 100
        if i==len(reverseSorted)-1 || entry >=100{
            result=strconv.Itoa(entry)+result

        //lazy padding here on out
        } else if entry==0 {
            result="000"
        } else if entry <=9 {
            result="00"+ strconv.Itoa(entry)+result
        } else {
            result="0"+ strconv.Itoa(entry)+result
        }

    }

    return result
}


func countClosure(mod int) func() []int {
    toCount:=make([]int,1,20)
    toCount[0]=0
    max:=mod

    return func() []int{

        //add one to beginning
        toCount[0]+=1

        //carry things up if we need to
        idx:=0
        for toCount[idx]>=max{
            toCount[idx]=0

            if idx+1==len(toCount){
                toCount=append(toCount, 1)
            } else {
                toCount[idx+1]+=1
            }

            idx+=1
        }
        return toCount
    }
}



func main() {

    // store the numbers that are higher than numbers previous to them
    // for example, three is the (first) longest number between 1 and 9
    // one : 3
    // two : 3
    // three : *5*
    // four : 4
    // five : 4
    // six : 3
    // seven : 5 (but we've already seen three)
    // eight : 5 (but we've already seen three)
    // nine : 4
    //
    // Realizing that, we store all of the numbers are transition points
    // between 1 and 999 and then check those to see when we go over 280 characters
    // we limit the number of entries we need to check
    highestSeen:=0

    transitionPoints:= make([]int,0)
    transitionPoints= append(transitionPoints, 0) //we want to check transitions

    // also make the global cachefor numbers 0-999
    cache=make(map[int]string)

    for i:=1 ; i<=999; i++ {
        result:=SliceToString([]int{i})
        if len(result) > highestSeen {
            highestSeen=len(result)
            transitionPoints = append(transitionPoints, i)
        }
    }



    //incrementer is a helper function that returns a slice
    // of the indicies of transitionPoints we need to check
    incrementer:=countClosure(len(transitionPoints))
    var answerSlice []int
    tweetLimit:=280

    for {
        indicies:=incrementer()

        //generate the number we need to check from the indicies of transition points
        numberSlice:=make([]int,len(indicies))
        for i, idx := range(indicies){ numberSlice[i]=transitionPoints[idx] }

        //generate the string
        numberString:=SliceToString(numberSlice)

        //check it
        if len (numberString) > tweetLimit{
            answerSlice=numberSlice
            break
        }
    }

    //the number we found is just over the limit so we subtract one
    //(the 999^0 is in answerSlice[0]
    //and then print it
    answerSlice[0]-=1
    answerFullString:=SliceToString(answerSlice)
    answerIntString:=printSlice(answerSlice)

    fmt.Println("chars:", len(answerFullString))
    fmt.Println("spelled out:", answerFullString)
    fmt.Println("as int:", answerIntString)

}
