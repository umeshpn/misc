import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class RestApiRunner {

    private final String url;
    private Map<String, String> singleValuedParms;
    private Map<String, List<String>> multiValuedParms;

    public RestApiRunner(String url) {
        this.url = url;
        this.singleValuedParms = new TreeMap<>();
        this.multiValuedParms = new TreeMap<>();
    }

    public void setParm(String key, String value) {
        this.singleValuedParms.put(key, value);
    }

    public void addParm(String key, String value) {
        if (this.multiValuedParms.containsKey(key)) {
           this.multiValuedParms.get(key).add(value);
        } else {
            final ArrayList<String> values = new ArrayList<>();
            values.add(value);
            this.multiValuedParms.put(key, values);
        }
    }

    public InputStream callApi(String url, Map<String, Set<String>> parms) {
        URLConnection connection = null;
        try {
            connection = new URL(this.url).openConnection();
        }
        catch (IOException e) {
            e.printStackTrace();
            return null;
        }
        if (connection == null) {
            return null;
        }
        for(Map.Entry<String, String> entry : this.singleValuedParms.entrySet()) {
            connection.setRequestProperty(entry.getKey(), entry.getValue());
        }
        for(Map.Entry<String, List<String>> entry : this.multiValuedParms.entrySet()) {
            String key = entry.getKey();
            List<String> values = entry.getValue();
            for (String value : values) {
                connection.addRequestProperty(key, value);
            }
        }
        try {
            return  connection.getInputStream();
        }
        catch (IOException e) {
            e.printStackTrace();
            return null;
        }
        
    }
}
