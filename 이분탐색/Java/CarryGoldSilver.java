package 이분탐색.Java;

public class CarryGoldSilver {
    public static long solution(long a, long b, long[] g, long[] s, long[] w, long[] t) {
        long left = 0;
        long right = 4_000_000_000_000_000L; // 4 * 10^14

        while (left <= right) {
            long mid = (left + right) / 2;

            long totalGold = 0;
            long totalSilver = 0;
            long totalCarrying = 0;

            for (int i = 0; i < g.length; i++) {
                // Mid 시간 내에 가능한 왕복 횟수를 계산
                long trips = mid / (2 * t[i]);
                if (mid % (2 * t[i]) >= t[i]) {
                    trips += 1;
                }

                // 해당 트립에서 운반할 수 있는 총 무게
                long maxCarrying = trips * w[i];
                long gold = Math.min(g[i], maxCarrying);
                long silver = Math.min(s[i], maxCarrying);
                long carrying = Math.min(g[i] + s[i], maxCarrying);

                totalGold += gold;
                totalSilver += silver;
                totalCarrying += carrying;
            }

            // 현재 mid 시간 내에 운반할 수 있는 총 무게가 조건을 만족하는지 확인
            if (totalGold >= a && totalSilver >= b && totalCarrying >= a + b) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}