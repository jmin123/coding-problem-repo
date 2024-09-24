import java.util.*;

class Solution {
    private Set<String> candidateKeys = new HashSet<>();

    public int solution(String[][] relation) {
        int columnCount = relation[0].length;

        dfs(0, columnCount, "", relation);

        return candidateKeys.size();
    }

    private void dfs(int depth, int maxDepth, String currentKey, String[][] relation) {
        if (depth == maxDepth) {
            return;
        }

        // 유일성 검사
        boolean isUnique = isUnique(currentKey, relation);

        if (isUnique) {
            // 최소성 검사
            boolean isMinimal = true;
            for (String key : candidateKeys) {
                if (currentKey.contains(key)) {
                    isMinimal = false;
                    break;
                }
            }

            if (isMinimal) {
                candidateKeys.add(currentKey);
            }
        }

        dfs(depth + 1, maxDepth, currentKey, relation);
        dfs(depth + 1, maxDepth, currentKey + depth, relation);
    }

    private boolean isUnique(String key, String[][] relation) {
        Set<String> tuples = new HashSet<>();
        for (String[] row : relation) {
            StringBuilder tuple = new StringBuilder();
            for (int i = 0; i < key.length(); i++) {
                int columnIndex = Integer.parseInt(key.substring(i, i + 1));
                tuple.append(row[columnIndex]).append(",");
            }
            if (!tuples.add(tuple.toString())) {
                return false;
            }
        }
        return true;
    }
}