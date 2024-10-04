package 완전탐색.Java;

import java.util.Arrays;

public class 최고의 집합 {
    public int[] solution(int n, int s) {
        // n이 s보다 클 경우, 합을 s로 만들 수 없으므로 [-1] 반환
        if (n > s) {
            return new int[]{-1};
        }
        
        int[] result = new int[n];
            
        // 기본값과 나머지를 계산
        int base = s / n;
        int remainder = s % n;
                
        // 먼저 나머지 부분에 base + 1을 할당하여 높은 숫자부터 채움
        for (int i = 0; i < remainder; i++) {
            result[i] = base + 1;
        }
            
        // 나머지 요소에 base를  할당
        for (int i = remainder; i < n; i++) {
            result[i] = base;
        }
            
        // 마지막으로 오름차 순 정렬
        Arrays.sort(result);
        return result;
    }
}
