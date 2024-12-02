<?php
session_start();
require "aputoiminnot.php";
$id = $_SESSION['id'];

$istuntotunnus = htmlspecialchars($_COOKIE["istuntotunnus"]);
$nimi = htmlspecialchars($_POST["nimi"]);
$kuvaus = htmlspecialchars($_POST["kuvaus"]);
$tiedosto = $_FILES["tiedosto"];

if(isset($_FILES['tiedosto'])) {
$tiedosto_name = $_FILES['tiedosto']['name'];
$tiedosto_type = $_FILES['tiedosto']['type'];
$uploaded_file = $_FILES['tiedosto'];
$file_tmp = $uploaded_file['tmp_name']; // Temporary location of the uploaded file
$file_name = basename($uploaded_file['name']); // Original name of the file

$destination = "C:\\xampp\\htdocs\\kuvakanta\\tallennetut\\" . $file_name;
}

if($id == "")
{
    if(!$kysely = mysqli_query($yhteys, "INSERT INTO tiedostot (nimi,kuvaus,
        tiedostonimi,tyyppi,tallentaja) VALUES ('$nimi', '$kuvaus', 
        '$tiedosto_name','$tiedosto_type', '$kayttajatunnus')"))
    {
        print "<H2>Tallennus epäonnistui!</H2>";
        exit;
    }
    else
    {
        if(move_uploaded_file($file_tmp, $destination))
        {
            print "<H2>Tallennus onnistui!</H2>";
        }
    }
}
else
{
    if(!$kysely = mysqli_query($yhteys, "UPDATE tiedostot SET nimi='$nimi',
        kuvaus='$kuvaus', tiedostonimi='$tiedosto_name', tyyppi='$tiedosto_type'
        WHERE id=$id AND tallentaja='$kayttajatunnus'"))
    {
        print "Tallennus epäonnistui!";
        exit;
    }
    else
    {
        if(move_uploaded_file($file_tmp, $destination))
        {
            print "Tallennus onnistui!";
        }
    }
}
?>
<br>
<a href="index.php">Takaisin etusivulle</A>