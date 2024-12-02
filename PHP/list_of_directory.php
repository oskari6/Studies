<?php
$polku = "C:\\xampp\\htdocs\\xml";
$hakemisto = opendir($polku);
print "<ul>";
while ($tiedosto = readdir($hakemisto))
{
    print "<li>" . $tiedosto;
}
print "</ul>";
closedir($hakemisto);
?>