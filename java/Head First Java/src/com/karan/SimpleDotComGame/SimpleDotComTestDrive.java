package com.karan.SimpleDotComGame;

public class SimpleDotComTestDrive {
	
	public static void main (String[] args) {
		
		SimpleDotCom dot = new SimpleDotCom();
		
		int[] locations = {2,3,4};
		
		dot.setLocationCells(locations) ; 
		
		
		String userGuess = "2";
		String result = dot.checkYourself(userGuess);
		String testResult = "Failed";
				
		if (result.equals("hit"));{
			
			testResult = "passed";
		}
		
		System.out.println(testResult);
	}
	
	public String CheckYourself(String stringGuess) {
		
		int guess = Integer.parseInt(stringGuess);
		String result = "miss" ;
		
		for (int cell : locationCells) {
			
			if (guess == cell) {
				result = "hit";
				numOfHits++;
				break;
			}
			
		}
		
		
	}
}
