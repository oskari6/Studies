<?php
//in php.ini configure:
//SMTP=postipalvelimennimi
//sendmail_from=sähköposti

function LahetaVirheViesti()
{
    $otsikko = "Sovelluksessa sattui virhe";
    $vastaanottaja = "matti@jokuosoite.fi";
    $viesti = "Tietojen tallennus ei onnistunut, tämä on automaattinen viesti ohjelmasta";
    mail($vastaanottaja, $otsikko, $viesti);
}
?>