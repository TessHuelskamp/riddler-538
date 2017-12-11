#include <iostream>
using std::cout; using std::endl;
#include <algorithm>
using std::find;

#include <vector>
using std::vector;

#include <map>
using std::map;

#include <utility>
using std::pair;


/*
 * 538 dart riddler December 2018
 *
 * How many ways are there to win a perfect game of darts?
 *
 * sounds susp like a problem we'd get in 831 so I thought I would
 * code it out as a recursive solution and then figure out how to
 * do it using dynamic programming :D
 *
 * not a bad way to spend a Sunday
 *
 */

class Dart{
private:
  map<pair<int,int>,unsigned long long> cache;
  unsigned long long internalCalc(int, int);
  unsigned long long cacheOrCalc(int, int);
  void makeBoard();
  vector<int> board;
  vector<int> lastTurn;


public:
  unsigned long long calculate();

};

unsigned long long Dart::calculate(){
  makeBoard();

  // *a* perfect game
  // 9*50 + 1 * 50 // need to end with a bulls eye or double
  cacheOrCalc(501,11);
  pair<int,int> key(501,11);
  return cache[key];
}

void Dart::makeBoard(){

  //init 1-20
  for (int i=1; i<=20; ++i){
    board.emplace_back(i); //wedge closest to center
    board.emplace_back(2*i); // double ring
    board.emplace_back(i); // wedge near outside
    board.emplace_back(3*i); //triple ring

    lastTurn.emplace_back(2*i); //double ring
  }

  //add bulls eyes
  board.emplace_back(25); board.emplace_back(50);
  lastTurn.emplace_back(25); board.emplace_back(50);

}

unsigned long long Dart::cacheOrCalc(int toScore, int turns){
  pair<int,int> key(toScore,turns);

  auto it = cache.find(key);
  if (it != cache.end()){
    return cache[key];
  } else {
    cache[key]=internalCalc(toScore, turns);
    return cache[key];
  }

}


unsigned long long Dart::internalCalc(int toScore, int turns){

  if (turns <= 0) return 0;
  else if (turns==1){
    //if what we need is in board, we win!
    auto it = find(lastTurn.begin(), lastTurn.end(), toScore);
    if (it != lastTurn.end()) return 1;
    else return 0; // :(
  } else { //this is where we check sub problems
    unsigned long long totalPossibleWins=0;
    for ( auto move : board){
      //check to see if score would go to or below 0
      //if score is 0 we'd win too early
      //less than zero wouldn't work
      //
      //if score is a possible win, then check
      if (toScore-move >0){
        totalPossibleWins+=cacheOrCalc(toScore-move,turns-1);
      }

    }
    return totalPossibleWins;
  }

}

int main(){
  Dart d;

  cout << d.calculate() << endl;


}
