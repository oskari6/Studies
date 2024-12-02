<?php
function AvaaTietokanta($osoite = "127.0.0.1", $tietokanta="harjoitukset")
{
    $yhteysnumero = mysqli_connect($osoite, "root", "", $tietokanta);

    if(!$yhteysnumero)
    {
        die("Connection failed: " . mysqli_connect_error());
    }
    return $yhteysnumero;
}
?>