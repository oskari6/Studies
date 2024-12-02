<?php
function AvaaJaPalautaMetaTiedot($tiedostonimi)
{
    $metatiedot = get_meta_tags($tiedostonimi);
    return $metatiedot;
}

$polku = "C:\\xampp\\htdocs\\xml";

$hakemisto = opendir($polku);
print "<table border = 1>";
print "<tr><td>Tiedosto</td>Otsikko</td>
        <td>Avainsanat</td><td>Kuvaus</td></tr>";
while($tiedosto = readdir($hakemisto))
{
    if(ereg(".html", $tiedosto))
    {
        $meta = AvaaJaPalautaMetaTiedot($polku . "/" . $tiedosto);
        print "<tr>
                <td><a href=\"$tiedosto\">$tiedosto</a<</td>
                <td>$meta[title]</td>
                <td>$meta[keywords]</td>
                <td>$meta[description]</td>
                </tr>"
    }
}
print "</table>";
closedir($hakemisto);
?>