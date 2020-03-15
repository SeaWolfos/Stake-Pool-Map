<style>
    table, th, tr, td {
        border: 1px solid black;
        border-collapse: collapse;
    }

    th, td {
        padding: 5px 30px;
    }
</style>

<?php
    include '/home/cam/projects/project_secrets/geoAPI.key';
	 
	 $apiKey = fopen("geoAPI.key", "r");
    $ips = array("173.212.246.91", "209.195.106.120", "91.184.220.227", "5.189.162.14", "91.158.25.32");

    echo "<table>";
    echo "<tr>";
    echo "<th>IP</th>";
    echo "<th>Continent</th>";
    echo "<th>Country</th>";
    echo "<th>Organization</th>";
    echo "<th>ISP</th>";
    echo "<th>Languages</th>";
    echo "<th>Is EU Member?</th>";
    echo "<th>Currency</th>";
    echo "<th>Timezone</th>";
    echo "</tr>";

    foreach ($ips as $ip) {
        $location = get_geolocation($apiKey, $ip);
        $decodedLocation = json_decode($location, true);

        echo "<tr>";
        echo "<td>".$decodedLocation['ip']."</td>";
        echo "<td>".$decodedLocation['continent_name']." (".$decodedLocation['continent_code'].")</td>";
        echo "<td>".$decodedLocation['country_name']." (".$decodedLocation['country_code2'].")</td>";
        echo "<td>".$decodedLocation['organization']."</td>";
        echo "<td>".$decodedLocation['isp']."</td>";
        echo "<td>".$decodedLocation['languages']."</td>";
        if($decodedLocation['is_eu'] == true) {
            echo "<td>Yes</td>";
        } else {
            echo "<td>No</td>";
        }
        echo "<td>".$decodedLocation['currency']['name']."</td>";
        echo "<td>".$decodedLocation['time_zone']['name']."</td>";
        echo "</tr>";
    }
    echo "</table>";

    function get_geolocation($apiKey, $ip, $lang = "en", $fields = "*", $excludes = "") {
        $url = "https://api.ipgeolocation.io/ipgeo?apiKey=".$apiKey."&ip=".$ip."&lang=".$lang."&fields=".$fields."&excludes=".$excludes;
        $cURL = curl_init();

        curl_setopt($cURL, CURLOPT_URL, $url);
        curl_setopt($cURL, CURLOPT_HTTPGET, true);
        curl_setopt($cURL, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($cURL, CURLOPT_HTTPHEADER, array(
            'Content-Type: application/json',
            'Accept: application/json'
        ));
        return curl_exec($cURL);
    }
?>
