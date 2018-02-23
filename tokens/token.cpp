#include <iostream>
using std::cout; using std::endl;

#include <random>
using std::default_random_engine; using std::uniform_int_distribution;


// return 0, 1, 2 evenly
unsigned int rollDie(default_random_engine &gen){
  //set up coin
  uniform_int_distribution<int> distribution(0,2);

  //roll die
  return distribution(gen);
}

//true: I won
//false: you won
bool playGame(default_random_engine &gen){
  int myTokens=1, yourTokens=2, turns=0, MAX_TURNS=1000;

  while (myTokens != 0 && yourTokens != 0 && turns < MAX_TURNS ){
    if (rollDie(gen)==0){ // 1/3 of the time you win
      myTokens--; yourTokens++;
    } else { // 2/3 of the time I win
      myTokens++; yourTokens--;
    }

    turns++;
  }

  // -\_()_/-
  if (turns >= MAX_TURNS) throw std::runtime_error("too many turns");

  return myTokens!=0;
}

int main(){
  //build the rng
  default_random_engine generator;

  int totalGames=100000, myWins=0;
  for (int i=0; i < totalGames; ++i){
    if (playGame(generator)) myWins++;
  }

  cout << "Percentage that I win: " << float(myWins)/float(totalGames) << endl;

}

