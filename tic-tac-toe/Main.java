
import java.util.*;
import java.lang.*;

public class Main{

        public static void main(String[] args) {

        List<Board> previous  = new ArrayList<Board>();
        List<Board> current  = new ArrayList<Board>();
        List<Board> finalBoards = new ArrayList<Board>();

        // set up first moves
        for (int i=1; i<=9; ++i) {
            Board game = new Board();
            game.play(i, Status.X);
            current.add(game);
        }

        Boolean turn=true;

        while (!current.isEmpty()){

            // nuke the previous round
            previous.clear();
            previous = new ArrayList(current);
            current.clear();

            // Pick whose turn it is to play.
            Status play = (turn) ? Status.O : Status.X;
            turn ^= true;

            //For each board int the previous round, play all possible, open moves
            for (Board b : previous) {
                for (Integer i=1; i<=9; ++i){

                    if (! b.spotOpen(i)) {
                        continue;
                    }

                    Board newBoard  = new Board(b);
                    newBoard.play(i, play);

                    if (newBoard.isOver()){
                        finalBoards.add(newBoard);
                    } else {
                        current.add(newBoard);
                    }
                }
            }
        }


        // Number of possible games is twice the final boards
        // (started with X; could reverse who played what move)
        System.out.println(2*finalBoards.size());

    }


}
