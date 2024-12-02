<?php
$xmltiedosto = "auto.xml";
$omistaja = "";
$hankintavuosi = "";
$huomautukset = "";
$merkkaus = "";

function elementinAloitus($jasennin, $nimi, $attribuutit)
{
    global $merkkaus;
    $merkkaus = $nimi;
}

function elementinLopetus($jasennin, $nimi)
{
    global $merkkaus;
    $merkkaus = "";
}

function merkit($jasennin, $merkit)
{
    global $merkkaus;
    global $omistaja;
    global $hankintavuosi;
    global $huomautukset;

    if($merkkaus == "OMISTAJA")
        $omistaja = $merkit;
    else if($merkkaus == "HANKINTAVUOSI")
        $hankintavuosi .=$merkit;
    else if($merkkaus == "HUOMAUTUKSET")
        $huomautukset .= $merkit;
}

$xml_jasennin = xml_parser_create();

xml_set_element_handler($xml_jasennin, "elementinAloitus", "elementinLopetus");
xml_set_character_data_handler($xml_jasennin, "$merkit");

if(!($tiedostohandle = fopen($xmltiedosto, "r")))
{
    die("Tiedostoa ei voitu avata!");
}
while($data = fread($tiedostohandle, 4096))
{
    if(!xml_parse($xml_jasennin, $data, feof($tiedostohandle)))
    {
        print "XML-virhe: ";
        print "<p>" . xml_error_string(xml_get_error_code($xml_jasennin)) . "</p>";
        print "<p>rivillä " . xml_get_current_line_number($xml_jasennin) . "</p>";
        exit;
    }
}

xml_parser_free($xml_jasennin);

print "<h2>XML-dokumentin sisältö</h2>";
print "<p>Omistaja_ $omistaja</p>";
print "<p>Hankintavuosi: $hankintavuosi</p>";
print "<p>Huomautukset: $huomautukset</p>";

?>