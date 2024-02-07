
//I did this one because I play Dungeons and Dragons and was curious about this. This program
//calculates the probability of rolling each possible stat value in Dungeons and Dragons 
//character set up. It’s slightly complicated because you roll four six-sided dice and then 
//drop the lowest of the four, and then add up the three remaining dice. So for example, if you
//rolled a 3, 2, 6, and 4, you’d drop the 2 and add up the 3, 6, and 4 to get 13. But obviously 
//there are a lot of different ways to get 13, so it's fun! I wouldn't be surprised if there
//is a way simpler way to do this, but I wanted to be able to print out all the different
//permutations of the dice if I wanted to see them so maybe that makes mine more complicated 
//than it needs to be? lol... Regardless, here it is!

import java.util.Arrays;

class Stats {
    
    int possibilities;
    int[] sumWays;
    
    public Stats() {
	possibilities = 0;
	sumWays = new int[16];
    }

    public void possibleDiePermutations(char[] possibleDieValues, String current) {
	if (current.length() == 4) {
	    possibilities++;
	    countSums(addDie(dropLowest(current)));
	} else {
	    for (int i = 0; i < 6; i++) {
		String previous = current;
		current += possibleDieValues[i];
		possibleDiePermutations(possibleDieValues, current);
		current = previous;
	    }
	}
    }

    public int[] countSums(int sum) {
	sumWays[sum - 3] = sumWays[sum - 3] + 1;
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
	return dieOutcome.substring(0, indexOfDropped) + dieOutcome.substring(indexOfDropped + 1);
    }

    public static void main(String args[]) {
        Stats stats1 = new Stats();
        char[] possibleDieValues = {'1', '2', '3', '4', '5', '6'};
        stats1.possibleDiePermutations(possibleDieValues, "");
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
