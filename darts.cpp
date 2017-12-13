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


class Dart{
private:
  void makeBoard();

  // get a key for the cache
  pair<int,int> makePair(int points, int turns);

  // get value for a game
  unsigned long long findAndReturn(int points, int turns);

  // board is all of the possible moves we could make on a normal turn
  // see makeBoard() for explanation on how tiles are counted
  vector<int> board;

  // moves that are only available on the last turn
  // Per the rules, you can hit the bullseye or you can hit the double ring
  vector<int> lastTurn;

  // cache of previous results
  // key is points, turns
  // value is the number of ways to get to that point
  map<pair<int,int>,unsigned long long> cache;

  const int maxPoints=501;
  const int maxTurns=9;

public:
  unsigned long long calculate();

  // constructors
  // can pass in different "games" for debugging
  Dart(int mp, int t) : maxPoints(mp), maxTurns(t) {makeBoard();}
  Dart(){makeBoard();};

};

pair<int,int> Dart::makePair(int points, int turns){
  pair<int,int> result(points,turns);
  return result;
}

// look up value in cache
unsigned long long Dart::findAndReturn(int points, int turns){
  pair<int, int> key=makePair(points, turns);
  if (cache.find(key) != cache.end()) return cache[key];
  else return 0.0;

}

void Dart::makeBoard(){

  // construct wedges 1-20
  // note that some entries are double (or 4x!) counted
  // I assume that edge different spot on the board would count as a different move
  // If those should be considered the same move,
  // change the board to be a set and not a vector
  for (int i=1; i<=20; ++i){
    board.emplace_back(i);    // wedge closest to center
    board.emplace_back(2*i);  // double ring
    board.emplace_back(i);    // wedge near outside
    board.emplace_back(3*i);  // triple ring

    // construct the lastTurn board
    lastTurn.emplace_back(2*i); // double ring
  }

  // add bulls eyes
  board.emplace_back(25); board.emplace_back(50);
  lastTurn.emplace_back(25); lastTurn.emplace_back(50);
}

unsigned long long Dart::calculate(){

  // mark all of the games that can be won on the last turn
  for ( const int point : lastTurn){ cache[makePair(point,1)]++; }

  // check all possible games starting turn 2 to n
  for (int turn=2; turn<=maxTurns; ++turn){

    // check all possible point combinations
    for (int point=1; point<=maxPoints; ++point){

      // sum all possible wins for this subgame
      // each subgame has a different {point,turn} identifier
      unsigned long long possibleWins=0;

      // check all possible moves we can make on this turn
      for (const int move : board){

        // if the move we could make is valid,
        // add the subgame we'd get to's total
        //
        // A move can be invalid if it puts us at or below 0
        // (we'd go over or we'd finish a turn too early)
        if (point-move >0) possibleWins+=findAndReturn(point-move, turn-1);
      }

      //cache entry if bigger than 0
      //I only want to store winable games
      if (possibleWins > 0) cache[makePair(point,turn)]=possibleWins;
    }
  }

  return findAndReturn(maxPoints, maxTurns);
}

int main(){
  Dart d;
  cout << d.calculate() << endl;
}
