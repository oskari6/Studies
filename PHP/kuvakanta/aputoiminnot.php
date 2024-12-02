<?php
require "funktiot.php";
$yhteys = AvaaTietokanta();
$istuntotunnus = htmlspecialchars($_COOKIE["istuntotunnus"]);

if($istuntotunnus == "")
{
    $istuntotunnus = "tyhja";
}

if(!$kysely = mysqli_query($yhteys, "SELECT tunnus,istuntotunnus FROM 
        kayttaja WHERE istuntotunnus='$istuntotunnus'"))
{
    header("Location: http://127.0.0.1/kuvakanta/kirjautumislomake.php");
    exit;
}

if(mysqli_num_rows($kysely) != 1)
{
    header("Location: http://127.0.0.1/kuvakanta/kirjautumislomake.php");
    exit;
}

$kayttaja = mysqli_fetch_row($kysely);
$kayttajatunnus = $kayttaja[0];
?>