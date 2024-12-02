<?php
ini_set('display_errors', 0);   //error handling
error_reporting(0);

require "funktiot.php";
$yhteys = AvaaTietokanta();
$sivunotsikko;
$teksti;
$linkki = htmlspecialchars($_POST["linkki"]);
$otsikko = htmlspecialchars($_POST["otsikko"]);
$avainsana = htmlspecialchars($_POST["avainsana"]);
$kuvaus = htmlspecialchars($_POST["kuvaus"]);

$sql_lauseke = "INSERT INTO linkit (linkki, otsikko, avainsana, kuvaus) VALUES ('$linkki', '$otsikko', '$avainsana', '$kuvaus')";

if(!$kysely = mysqli_query($yhteys, $sql_lauseke))
{
    $sivunotsikko = "Tallennus epäonnistui!";
    $teksti = "Virhe: " . mysqli_error();
}
else
{
    $sivunotsikko = "Linkin tallennus onnistui ";
    $teksti .= "Linkin tiedot tallennettu tietokantaan<P>";
    $teksti .= "Linkki: " . $linkki . "<br>";
    $teksti .= "Otsikko: " . $otsikko . "<br>";
    $teksti .= "Avainsana: " . $avainsana . "<br>";
    $teksti .= "Kuvaus: " . $kuvaus . "<p>";
}

?>
<html>
<head>
<title><?php print "$sivunotsikko"; ?></title>
</head>
<body bgcolor="#ffffff">
<H2><?php print "$sivunotsikko";?></H2>
<?php
    print "$teksti";
?>
<p>
<a href="index.php">Takaisin etusivulle</A>
</body>
</html>