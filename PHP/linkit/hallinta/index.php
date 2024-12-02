<html>
<head>
    <title>Linkkitietokannan yllapito</title>
</head>
<body bgcolor="#ffffff">
<H2>Linkdatabase maintenance</H2>

<?php
/*funktiot.phtml sisältää apukomennot mm. tietokantayhteyden avaamisen jne.*/
require "funktiot.php";

/*Kutsutaan tietokantayhteyden avaavaa functiota*/
$yhteys = AvaaTietokanta();

$query = "SELECT COUNT(*) from linkit";
$result = mysqli_query($yhteys, $query);

/*Selvitetään montako linkkiä kannassa on tällä hetkellä*/
if(!$result)
{
    print "Kysely epäonnistui. " . mysqli_error($yhteys);
}
else
{
    $row = mysqli_fetch_row($result);
    print "Tietokannassa on tällä hetkellä " . $row[0] . "linkkiä<P>";
}

?>
<A HREF="listaa.php">Listaa tallennetut linkit</A> (muutos/poisto)<BR>
<A HREF="tallenna.php">Tallenna uusi linkki</A>
</body>
</html>
