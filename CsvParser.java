import java.io.BufferedReader;
import java.io.FileReader;
import java.util.*;

public class CsvToMapLoader {

    public static class ColumnDetail {
        private String field;
        private String type;
        private String label;

        public ColumnDetail(String field, String type, String label) {
            this.field = field;
            this.type = type;
            this.label = label;
        }

        @Override
        public String toString() {
            return String.format("ColumnDetail{field='%s', type='%s', label='%s'}", field, type, label);
        }
    }

    public static void main(String[] args) throws Exception {
        String csvFile = "your_file.csv"; // Change to your path
        Map<String, Map<String, List<ColumnDetail>>> resultMap = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            String line;
            boolean isFirstLine = true;

            while ((line = br.readLine()) != null) {
                if (isFirstLine) {
                    isFirstLine = false;
                    continue; // Skip header
                }

                String[] parts = line.split(",", -1); // allow empty columns

                if (parts.length < 6) continue; // safety check

                String view = parts[1].trim();
                String table = parts[2].trim();
                String field = parts[3].trim();
                String type = parts[4].trim();
                String label = parts[5].trim();

                ColumnDetail column = new ColumnDetail(field, type, label);

                for (String v : view.split("\\|")) {
                    String cleanedView = v.trim();
                    resultMap
                        .computeIfAbsent(cleanedView, k -> new HashMap<>())
                        .computeIfAbsent(table, k -> new ArrayList<>())
                        .add(column);
                }
            }
        }

        // Debug: print the map
        for (String viewKey : resultMap.keySet()) {
            System.out.println("View: " + viewKey);
            for (String table : resultMap.get(viewKey).keySet()) {
                System.out.println("  Table: " + table);
                for (ColumnDetail col : resultMap.get(viewKey).get(table)) {
                    System.out.println("    " + col);
                }
            }
        }
    }
}
