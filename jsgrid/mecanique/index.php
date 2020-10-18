<?php
header('Access-Control-Allow-Origin: *');
//header("Access-Control-Allow-Methods: GET, OPTIONS");
include "../models/profilRepository.php";
//include "../models/profil.php";
$config = include("../db/config.php");
$db = new PDO($config["db"], $config["username"], $config["password"]);
$profil = new profilRepository($db);


switch($_SERVER["REQUEST_METHOD"]) {
    case "GET":
       /* $result = $profil->getAll(array(
            "id" => intval($_GET["id"]),
            "denomination" => $_GET["denomination"],
            "raison_sociale" => $_GET["raison_sociale"],
            "responsable" => $_GET["responsable"],
            "activites" => $_GET["activites"],
            "produits" => $_GET["produits"],
            "adresse_usine" => $_GET["adresse_usine"],
            "gouvernorat" => $_GET["gouvernorat"],
            "delegation" => $_GET["delegation"],
            "telephone_siege_usine" => $_GET["telephone_siege_usine"],
            "fax_siege_usine" => $_GET["fax_siege_usine"],
            "email" => $_GET["email"],
            "URL" => $_GET["URL"],
            "regime" => $_GET["regime"],
            "pays_du_participant_etranger" => $_GET["pays_du_participant_etranger"],
            "entree_en_production" => $_GET["entree_en_production"],
            "capital_en_DT" => $_GET["capital_en_DT"],
            "emploi" => $_GET["emploi"],
            "secteur" => $_GET["secteur"],



        ));*/
        $result=$profil->getBySecteur("Industries mécaniques et métallurgiques");
        break;


}


header("Content-Type: application/json");
echo json_encode($result);

?>
