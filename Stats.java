import java.util.Arrays;

class Stats {
    
    int possibilities;
    int[] sumWays;
    
    public Stats() {
	possibilities = 0;
	sumWays = new int[16];
    }

    public void possibleDieCombinations(char[] possibleDieValues, String current) {
	if (current.length() == 4) {
	    //System.out.println("Die rolled: " + current);
	    possibilities++;
	    //System.out.println("Die counted: " + dropLowest(current));
	    //System.out.println("Sum of die counted: " + addDie(dropLowest(current)));
	    countSums(addDie(dropLowest(current)));
	} else {
	    for (int i = 0; i < 6; i++) {
		String previous = current;
		current += possibleDieValues[i];
		possibleDieCombinations(possibleDieValues, current);
		current = previous;
	    }
	}
    }

    public int[] countSums(int sum) {
	sumWays[sum - 3] = sumWays[sum - 3] + 1;
	//System.out.println("Sum: " + sum + "# of times: " + sumWays[sum - 3]);
	return sumWays; 
    }

    public int addDie(String dieCounted) {
	int sum = 0;
	for (int i = 0; i < 3; i++) {
	    sum += Character.getNumericValue(dieCounted.charAt(i));
	}
	return sum;
    }

    public String dropLowest(String dieOutcome) {
	//set the dropped value as the first number
	int droppedValue = Character.getNumericValue(dieOutcome.charAt(0));
	int indexOfDropped = 0;
	//start at i = i because we'll start checking from the second number
	for (int i = 1; i < 4; i++) {
	    if (Character.getNumericValue(dieOutcome.charAt(i)) < droppedValue) {
                droppedValue = Character.getNumericValue(dieOutcome.charAt(i));
		indexOfDropped = i;
	    }
        }
	//System.out.println("Die value dropped: " + droppedValue);
	return dieOutcome.substring(0, indexOfDropped) + dieOutcome.substring(indexOfDropped + 1);
    }

    public static void main(String args[]) {
        Stats stats1 = new Stats();
        char[] possibleDieValues = {'1', '2', '3', '4', '5', '6'};
        stats1.possibleDieCombinations(possibleDieValues, "");
	//System.out.println(stats1.possibilities);
	double probability;
	System.out.println();
	for (int i = 0; i < 16; i++) {
            System.out.println("A stat of: " + (i + 3) + " can result from " + stats1.sumWays[i] + " different permutations of the four dice.");
	    probability = (double) (stats1.sumWays[i])/(stats1.possibilities) * 100;
	    System.out.println("This results in a " + (probability) + "% chance of rolling a stat of " + (i + 3) + ".");
	    System.out.println();
        }
    }

}
