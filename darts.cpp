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
  void makeBoard();
  pair<int,int> makePair(int points, int turns){pair<int,int> result(points,turns); return result;};

  //board is all of the possible moves we could make on a normal turn
  //see makeBoard() for explanation on how tiles are counted
  vector<int> board;

  //moves that are only available on the last turn
  vector<int> lastTurn;

  //cache of all previous results
  map<pair<int,int>,unsigned long long> cache;

  const int maxPoints=501;
  const int maxTurns=9; //woops...


public:
  unsigned long long calculate();
  Dart(int mp, int t) : maxPoints(mp), maxTurns(t) {makeBoard();}
  Dart(){makeBoard();};

};

void Dart::makeBoard(){

  //construct wedges 1-20
  //note that some entries are double (or 4x!) counted
  //I assume that edge different spot on the board would count as a different move
  //For example, there's 4 different way to score 6 points:
  //  twice on the inner and outer 1x6 wedge, once on the double 3 wedge, and once on the triple 2 wedge
  //If those should be considered the same move, change the board to be a set and not a vector
  for (int i=1; i<=20; ++i){
    board.emplace_back(i); //wedge closest to center
    board.emplace_back(2*i); // double ring
    board.emplace_back(i); // wedge near outside
    board.emplace_back(3*i); //triple ring

    //construct the lastTurn board too
    lastTurn.emplace_back(2*i); //double ring
  }

  //add bulls eyes
  board.emplace_back(25); board.emplace_back(50);
  lastTurn.emplace_back(25); lastTurn.emplace_back(50);
}

unsigned long long Dart::calculate(){
  //interface to look things up
  pair<int,int> key;

  // mark all of the games that can be won on the last turn
  // I think this is fair to assume that the cache will be inited to zeros
  // There shouldn't be duplicate ways to win a game here but I increment in case we change the rules later
  // (all of the last winning moves have a unique number of points)
  for ( const int point : lastTurn){
    key=makePair(point,1);
    cache[key]++;
  }

  //check all possible games starting turn 2 to n
  for (int turn=2; turn<=maxTurns; ++turn){
    for (int point=1; point<=maxPoints; ++point){

      //sum all possible wins for this subgame
      unsigned long long possibleWins=0;

      //check all possible moves we can make
      for (const int move : board){

        // check to see if score would put us at or below 0
        // both cases would be an invalid game
        // (we'd go over or we'd finish too early)
        if (point-move >0){

          // check to see if the move we chose will get us to a game we previously have know to win
          key=makePair(point-move,turn-1);
          if (cache.find(key) != cache.end()){
            possibleWins+=cache[key];
          }
        }
      }

      //cache entry if bigger than 0
      //I only want to store winable games
      if (possibleWins > 0){
        key=makePair(point,turn);
        cache[key]=possibleWins;
      }
    }
  }

  //check to see if there's a way to win this board
  //It's possible to have a game that's unwinnable
  unsigned long long result=0;
  key=makePair(maxPoints, maxTurns);
  if (cache.find(key) != cache.end()) result=cache[key];
  return result;
}

int main(){
  Dart d;
  cout << d.calculate() << endl;
}
