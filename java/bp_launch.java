import java.io.*;
import java.net.*;
import java.security.SecureRandom;
import java.security.Security;
import java.security.cert.CertificateException;
import java.security.cert.X509Certificate;
import java.util.*;

import javax.net.ssl.HostnameVerifier;
import javax.net.ssl.HttpsURLConnection;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSession;
import javax.net.ssl.TrustManager;
import javax.net.ssl.X509TrustManager;
import javax.xml.bind.DatatypeConverter;

import org.json.JSONArray;
import org.json.JSONObject;

import java.io.OutputStream;



public class Sample {
    private static final String USER_AGENT = "Mozilla/5.0";
    private static final String POST_PARAMS = "{\"length\":250}";
    private static final String BP_NAME = "eG Enterprise";
    private static final String APP_NAME = "eG Enterprise2";
    private static final String APP_PROFILE_NAME = "Nutanix";


    public void doTrustToCertificates() throws Exception {
        Security.addProvider(new com.sun.net.ssl.internal.ssl.Provider());
        TrustManager[] trustAllCerts = new TrustManager[]{
                new X509TrustManager() {
                    public X509Certificate[] getAcceptedIssuers() {
                        return null;
                    }

                    public void checkServerTrusted(X509Certificate[] certs, String authType) throws CertificateException {
                        return;
                    }

                    public void checkClientTrusted(X509Certificate[] certs, String authType) throws CertificateException {
                        return;
                    }
                }
        };

        SSLContext sc = SSLContext.getInstance("SSL");
        sc.init(null, trustAllCerts, new SecureRandom());
        HttpsURLConnection.setDefaultSSLSocketFactory(sc.getSocketFactory());
        HostnameVerifier hv = new HostnameVerifier() {

            public boolean verify(String urlHostName, SSLSession session) {
                if (!urlHostName.equalsIgnoreCase(session.getPeerHost())) {
                    System.out.println("Warning: URL host '" + urlHostName + "' is different to SSLSession host '" + session.getPeerHost() + "'.");
                }
                return true;
            }
        };
        HttpsURLConnection.setDefaultHostnameVerifier(hv);
    }

    // connecting to URL
    public void connectToUrl() throws Exception {
        doTrustToCertificates();//
        URL url = new URL("https://10.5.74.95:9440/api/nutanix/v3/blueprints/list");
        String encoding = DatatypeConverter.printBase64Binary("admin:Id42modulo!".getBytes());
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Authorization", "Basic " + encoding);
        conn.setRequestProperty("User-Agent", USER_AGENT);
        conn.setRequestProperty("Content-Type", "application/json");


        // For POST only - START
        conn.setDoOutput(true);
        OutputStream os = conn.getOutputStream();
        os.write(POST_PARAMS.getBytes());
        os.flush();
        os.close();
        // For POST only - END

        int responseCode = conn.getResponseCode();
        BufferedReader in =
                new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        String bpId = null;
        StringBuffer response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }

        JSONObject outerObject = new JSONObject(response.toString());
        JSONArray entities = outerObject.getJSONArray("entities");
        for (int i = 0; i < entities.length(); i++) {
            JSONObject entity = entities.getJSONObject(i);
            String entityName = entity.getJSONObject("status").getString("name");
            if (entityName.equalsIgnoreCase(Sample.BP_NAME)) {
                bpId = entity.getJSONObject("status").getString("uuid");
                break;
            }
        }

        if (bpId == null) {
            System.out.println("Blueprint with name " + Sample.BP_NAME + " not found in list");
            System.exit(1);
        }

        url = new URL("https://10.5.74.95:9440/api/nutanix/v3/apps/list");
        encoding = DatatypeConverter.printBase64Binary("admin:Id42modulo!".getBytes());
        HttpURLConnection app = (HttpURLConnection) url.openConnection();
        app.setRequestMethod("POST");
        app.setDoOutput(true);
        app.setRequestProperty("Authorization", "Basic " + encoding);
        app.setRequestProperty("User-Agent", USER_AGENT);
        app.setRequestProperty("Content-Type", "application/json");


        // For POST only - START
        app.setDoOutput(true);
        os = app.getOutputStream();
        os.write(POST_PARAMS.getBytes());
        os.flush();
        os.close();
        // For POST only - END

        responseCode = app.getResponseCode();
        in =
                new BufferedReader(new InputStreamReader(app.getInputStream()));
        String APP_NAME = null;
        response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        //System.out.println(line);
        outerObject = new JSONObject(response.toString());
        entities = outerObject.getJSONArray("entities");
        boolean appExists = false;
        for (int i = 0; i < entities.length(); i++) {
            JSONObject entity = entities.getJSONObject(i);
            String entityName = entity.getJSONObject("status").getString("name");
            if (entityName.equalsIgnoreCase(Sample.APP_NAME)) {
                appExists = true;
                break;
            }
        }

        if (appExists) {
            System.out.println("Application with name " + Sample.APP_NAME + " already exists");
            System.exit(1);
        }

        url = new URL("https://10.5.74.95:9440/api/nutanix/v3/blueprints/" + bpId);
        encoding = DatatypeConverter.printBase64Binary("admin:Id42modulo!".getBytes());
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Authorization", "Basic " + encoding);
        con.setRequestProperty("User-Agent", USER_AGENT);
        con.setRequestProperty("Content-Type", "application/json");
        int responseCod = con.getResponseCode();
        in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }
        JSONObject launchBp = new JSONObject(response.toString());
        launchBp.remove("status");
        launchBp.getJSONObject("spec").remove("name");
        launchBp.getJSONObject("spec").put("application_name", Sample.APP_NAME);
        String appProfileUuid = null;
        // get app profile refrence from name
        JSONArray appProfileList = launchBp.getJSONObject("spec").getJSONObject("resources").getJSONArray("app_profile_list");
        for (int i = 0; i < appProfileList.length(); i++) {
            JSONObject appProfile = appProfileList.getJSONObject(i);
            if (appProfile.getString("name").equalsIgnoreCase(Sample.APP_PROFILE_NAME)) {
                appProfileUuid = appProfile.getString("uuid");
                break;
            }
        }

        if (appProfileUuid == null) {
            System.out.println("App profile with name " + Sample.APP_PROFILE_NAME + " not found in list");
            System.exit(1);
        }
        JSONObject appProfileReference = new JSONObject();
        appProfileReference.put("kind", "app_profile");
        appProfileReference.put("uuid", appProfileUuid);
        launchBp.getJSONObject("spec").put("app_profile_reference", appProfileReference);

        url = new URL("https://10.5.74.95:9440/api/nutanix/v3/blueprints/" + bpId + "/launch");
        encoding = DatatypeConverter.printBase64Binary("admin:Id42modulo!".getBytes());
        conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setDoOutput(true);
        conn.setRequestProperty("Authorization", "Basic " + encoding);
        conn.setRequestProperty("User-Agent", USER_AGENT);
        conn.setRequestProperty("Content-Type", "application/json");
        // For POST only - START
        conn.setDoOutput(true);
        os = conn.getOutputStream();
        os.write(launchBp.toString().getBytes());
        os.flush();
        os.close();
        in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        response = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            response.append(inputLine);
        }

        if (responseCode == 200) {
            System.out.println("Blueprint with name " + Sample.BP_NAME + " launched sucessfully"  + " with the profile "
                    + Sample.APP_PROFILE_NAME + " and application name " + Sample.APP_NAME);

        }
        else{
            System.out.println("Blueprint with name " + Sample.BP_NAME + "launched sucessfully"  + " with the profile "
                    + Sample.APP_PROFILE_NAME + " and application name " + Sample.APP_NAME);
            System.exit(1);



        }
    }
    public static void main(String []args) {
            Sample s = new Sample();
            try {
                s.connectToUrl();
            } catch (Exception e) {
                // TODO Auto-generated catch block

                e.printStackTrace();
            }
    }
}
