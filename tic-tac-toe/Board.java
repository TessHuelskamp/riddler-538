import static java.lang.System.err;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

public class Board {

    /*
     * 1 2 3
     * 4 5 6
     * 7 8 9
     */

    private HashMap<Integer, Status> board;
    private static final List<List<Integer>> lines =
        Arrays.asList(
            //horz
            Arrays.asList(1, 2, 3),
            Arrays.asList(4, 5, 6),
            Arrays.asList(7, 8, 9),
            //vert
            Arrays.asList(1, 4, 7),
            Arrays.asList(3, 5, 8),
            Arrays.asList(4, 6, 9),
            //diag
            Arrays.asList(1, 5, 9),
            Arrays.asList(3, 5, 7)
            );

    Board() {
        board = new HashMap<Integer, Status>();
        for (Integer i=1; i<=9; ++i){
            board.put(i,Status.E);
        }
    }

    Board(Board b) {
        this.board = new HashMap<Integer, Status>();
        this.board.putAll(b.board);
    }

    public String toString(){
        String result="";
        result += board.get(1) + "|" + board.get(2) + "|" + board.get(3) + "\n";
        result += board.get(4) + "|" + board.get(5) + "|" + board.get(6) + "\n";
        result += board.get(7) + "|" + board.get(8) + "|" + board.get(9) + "\n";
        return result;
    }

    public Boolean full(){
        for (Integer i=1; i<=9; ++i){
            if (board.get(i) == Status.E){
                return false;
            }
        }
        return true;
    }

    public Boolean isOver(){

        // check for wins
        for (List<Integer> possibleWin : lines){

            Boolean allX=true;
            Boolean allO=true;

            // check to see if all entries in a line are the same value
            // either all X's or all O's
            for (Integer loc : possibleWin){
                Status value = board.get(loc);
                switch (board.get(loc)){
                    case E:
                        allX=false;
                        allO=false;
                        break;
                    case O:
                        allX=false;
                        break;
                    case X:
                        allO=false;
                        break;
                }
            }

            if (allX || allO){
                return true;
            }

        }

        // If there isn't a win, the game is only over if the board is full.
        return full();
    }

    public void play(Integer location, Status turn) {
        board.put(location, turn);
    }

    public boolean spotOpen(Integer location){
        return board.get(location) == Status.E;
    }
}

