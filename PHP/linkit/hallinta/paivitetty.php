<?php
require "funktiot.php";
$yhteys = AvaaTietokanta();
$toiminto = htmlspecialchars($_POST["toiminto"]);
$linkki = htmlspecialchars($_POST["linkki"]);
$otsikko = htmlspecialchars($_POST["otsikko"]);
$avainsana = htmlspecialchars($_POST["avainsana"]);
$kuvaus = htmlspecialchars($_POST["kuvaus"]);
$id = htmlspecialchars($_POST["id"]);

if($toiminto == "Tallenna")
{
    $sql_lauseke = "UPDATE linkit SET
    linkki='$linkki', otsikko='$otsikko',
    avainsana='$avainsana', kuvaus='$kuvaus'
    WHERE id=$id ";

    if(!$kysely = mysqli_query($yhteys, $sql_lauseke))
    {
        $sivunotsikko = "Tietojen muuttaminen epäonnistui";
        $teksti = "Virhe: " . mysqli_error();
    }
    else
    {
        $sivunotsikko = "Linkin tiedot päivitetty tietokantaan.";
        $teksti = "Päivitys onnistui";
    }
}
else if($toiminto == "Poista")
{
    $sql_lauseke = "DELETE FROM linkit WHERE id=$id";

    if(!$kysely = mysqli_query($yhteys, $sql_lauseke))
    {
        $sivunotsikko = "Poisto epäonnistui";
        $teksti = "Virhe: " - mysqli_error();
    }
    else
    {
        $sivunotsikko = "Linkin tiedot poistettu tietokannasta.";
        $teksti = "Poisto onnistui.";
    }
}
?>
<html>
<head>
<title><?php print "$sivunotsikko"; ?></title>
</head>
<body  bgcolor="#ffffff">
<H2><?php print "$sivunotsikko"; ?></H2>
<?php
    print "$teksti";
?>
<p>
<a href="index.php">Takaisin etusivulle</A>
</body>
</html>
