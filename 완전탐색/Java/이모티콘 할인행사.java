package 완전탐색.Java;
import java.util.*;

public class Solution {
    static int[] discountRates = {10, 20, 30, 40};
    static int maxSubscribers = 0;
    static int maxSales = 0;

    public static int[] solution(int[][] users, int[] emoticons) {
        generateCombinations(emoticons, 0, new int[emoticons.length], users, emoticons.length);
        return new int[]{maxSubscribers, maxSales};
    }

    private static void generateCombinations(int[] emoticons, int depth, int[] currentDiscounts, int[][] users, int length) {
        if (depth == length) {
            evaluateCombination(currentDiscounts, users, emoticons);
            return;
        }
        for (int rate : discountRates) {
            currentDiscounts[depth] = rate;
            generateCombinations(emoticons, depth + 1, currentDiscounts, users, length);
        }
    }

    private static void evaluateCombination(int[] discounts, int[][] users, int[] emoticons) {
        int subscribers = 0;
        int sales = 0;

        for (int[] user : users) {
            int userDiscountThreshold = user[0];
            int userBudgetThreshold = user[1];
            int total = 0;

            for (int i = 0; i < emoticons.length; i++) {
                if (discounts[i] >= userDiscountThreshold) {
                    total += emoticons[i] * (100 - discounts[i]) / 100;
                }
            }

            if (total >= userBudgetThreshold) {
                subscribers++;
            } else {
                sales += total;
            }
        }

        if (subscribers > maxSubscribers || (subscribers == maxSubscribers && sales > maxSales)) {
            maxSubscribers = subscribers;
            maxSales = sales;
        }
    }
}