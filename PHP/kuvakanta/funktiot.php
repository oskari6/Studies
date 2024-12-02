<?php
function AvaaTietokanta($osoite = "127.0.0.1", $tietokanta="harjoitukset")
{
    $yhteys = mysqli_connect($osoite, "root", "", $tietokanta);

    if(!$yhteys)
    {
        die("Connection failed: " . mysqli_connect_error());
    }
    return $yhteys;
}
?>