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
  pair<int,int> makePair(int points, int turns){pair<int,int> result(points,turns); return result;};

  //board is all of the possible moves we could make
  //note that some numbers are double (or triply!) counted due to how
  //I decided to count "different" ways of throwing a dart
  vector<int> board;

  //moves that are only available on the last turn
  vector<int> lastTurn;

  const int maxPoints=501;
  const int maxTurns=11;


public:
  unsigned long long calculate();
  unsigned long long dypro();
  Dart(int mp,int t) : maxPoints(mp), maxTurns(t) {}
  Dart(){};

};


unsigned long long Dart::calculate(){
  makeBoard();

  cacheOrCalc(maxPoints,maxTurns);
  pair<int,int> key(maxPoints,maxTurns);
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
  lastTurn.emplace_back(25); lastTurn.emplace_back(50);

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

unsigned long long Dart::dypro(){
  cache.clear();

  //interface
  pair<int,int> key;

  // mark all of the games that can be won on the last turn
  // I think this is fair to assume that the cache will be inited to zeros
  // There shouldn't be duplicate ways to win a game here
  // (all of the last winning moves have a unique number of points)
  for ( const int point : lastTurn){
    key=makePair(point,1);
    cache[key]++;
  }

  for (int turn=2; turn<=maxTurns; ++turn){
    for (int point=1; point<=maxPoints; ++point){
      //check all possible games starting from the ground up
      unsigned long long possibleWins=0;

      //check all possible moves we can make
      for (const int move : board){
        //check to see if score would put us at or below 0
        //both cases would be an invalid game
        if (point-move >0){

          //check to see if that game is a previously winning game
          key=makePair(point-move,turn-1);
          auto it = cache.find(key);
          if (it != cache.end()){
            possibleWins+=cache[key];
          }
        }
      }

      //cache entry if bigger than 0
      //I only want to score winable games
      if (possibleWins > 0){
        key=makePair(point,turn);
        cache[key]=possibleWins;
      }

    }
  }

  //check to see if there's a way to win this board
  unsigned long long result=0;
  auto it=cache.find(makePair(maxPoints, maxTurns));
  if (it!=cache.end()) result=cache[makePair(maxPoints, maxTurns)];
  return result;
}

int main(){
  Dart d;
  cout << d.calculate() << endl;
  cout << d.dypro() << endl;

  Dart e(121,2);
  cout << e.calculate() << endl;

  Dart f(50,1);
  cout << f.calculate() << endl;

  cout << endl << endl;
  cout << "should not work" << e.dypro() << endl;

}
