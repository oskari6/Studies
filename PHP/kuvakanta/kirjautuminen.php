<?php
require "funktiot.php";
$tunnus = htmlspecialchars($_POST["tunnus"]);
$salasana = htmlspecialchars($_POST["salasana"]);

if($tunnus == "" || $salasana == "")
{
    header("Location: http://127.0.0.1/kuvakanta/kirjautumislomake.php");
    exit;
}

$yhteys = AvaaTietokanta();

//Rakennetaan merkkijono ja luodaan uusi istuntotunnus
$avain = time() . $tunnus . $salasana . getenv("REMOTE_ADDR");
$istuntotunnus = md5($avain);

if(!$kysely = mysqli_query($yhteys, "UPDATE kayttaja SET istuntotunnus=
        '$istuntotunnus' WHERE tunnus='$tunnus' AND salasana=
        '$salasana'"))
{
    header("Location: http://127.0.0.1/kuvakanta/kirjautumislomake.php");
    exit;
}
else
{
    if(mysqli_affected_rows($yhteys) == 1)
    {
        setcookie("istuntotunnus", "$istuntotunnus", time() + 3600, "/");
        header("Location: http://127.0.0.1/kuvakanta/index.php");
        exit;
    }
    header("Location: http://127.0.0.1/kuvakanta/kirjautumislomake.php");
}
?>