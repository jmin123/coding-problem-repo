package 완전탐색.Java;

class Solution {
    public int solution(int[] arrayA, int[] arrayB) {
        int gcdA = gcdArr(arrayA);
        int gcdB = gcdArr(arrayB);

        boolean isVaildA = true;
        // arrayB의 모든 숫자가 arrayA의 최대 공약수로 나누어 떨어지면 서로 나누어진다는 거다
        for (int b : arrayB) {
            if (b % gcdA == 0) {
                isVaildA = false;
                break;
            }
        }

        // arrayA의 모든 숫자가 arrayB의 최대 공약수로 나누어 떨어지면 서로 나누어진다는 거다
        boolean isVaildB = true;
        for (int a : arrayA) {
            if (a % gcdB == 0) {
                isVaildB = false;
                break;
            }
        }

        // 서로 최대 공약수가 있을 수도 있지만, 이런 경우에는 둘 중에 더 큰 값을 반환
        if (isVaildA && isVaildB) {
            return Math.max(gcdA, gcdB);
        } else if (isVaildA) {
            return gcdA;
        } else if (isVaildB) {
            return gcdB;
        } else {
            return 0;
        }
    }
    
    // 배열이 유클리드 호제법 상 최대 공약수가 뭔지 구하기
    private int gcdArr(int[] arr) {
        int result = arr[0];
        for (int i = 1; i < arr.length; i++) {
            result = gcd(result, arr[i]);
            if (result == 1) return 1; // 더는 나눌 수 없음
        }
        return result;
    }
    
    // 유클리드 호제법
    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}