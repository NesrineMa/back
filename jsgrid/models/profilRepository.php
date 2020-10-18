<?php

include "profil.php";

class profilRepository {

    protected $db;

    public function __construct(PDO $db) {
        $this->db = $db;
    }

    private function read($row) {
        $result = new profil();
        //var_dump($result); die;
        $result->id = $row["id"];
        $result->denomination = $row["denomination"];
        $result->raison_sociale = $row["raison_sociale"];
        $result->responsable = $row["responsable"];
        $result->activites = $row["activites"];
        $result->produits = $row["produits"];
        $result->adresse_usine = $row["adresse_usine"];
        $result->gouvernorat = $row["gouvernorat"];
        $result->delegation = $row["delegation"];
        $result->telephone_siege_usine = $row["telephone_siege_usine"];
        $result->fax_siege_usine = $row["fax_siege_usine"];
        $result->email = $row["email"];
        $result->URL = $row["URL"];
        $result->regime = $row["regime"];
        $result->pays_du_participant_etranger = $row["pays_du_participant_etranger"];
        $result->entree_en_production = $row["entree_en_production"];
        $result->capital_en_DT = $row["capital_en_DT"];
        $result->emploi = $row["emploi"];
        $result->secteur = $row["secteur"];


        return $result;
    }
    public function getList() {        
    


        $sql = "SELECT * FROM profil";
        $q = $this->db->prepare($sql);
    

        $q->execute();
     $result=$q->fetchAll();
     
        return $result;
    }
    
  public function getBySecteur($secteur) {        
    


        $sql = 'SELECT * FROM profil WHERE secteur="'.$secteur.'"';
        $q = $this->db->prepare($sql);
    
        $q->execute();
     $result=$q->fetchAll();
     
        return $result;
    }



    public function getAll($filter) {        
       // $id = $filter["id"];
        $denomination = "%" . $filter["denomination"] . "%";
        $raison_sociale = "%" . $filter["raison_sociale"] . "%";
        $responsable = "%" . $filter["responsable"] . "%";
        $activites = "%" . $filter["activites"] . "%";
        $produits = "%" . $filter["produits"] . "%";
        $adresse_usine = "%" . $filter["adresse_usine"] . "%";
        $gouvernorat = "%" . $filter["gouvernorat"] . "%";
        $delegation = "%" . $filter["delegation"] . "%";
        $telephone_siege_usine = "%" . $filter["telephone_siege_usine"] . "%";
        $fax_siege_usine = "%" . $filter["fax_siege_usine"] . "%";
        $email = "%" . $filter["email"] . "%";
        $URL = "%" . $filter["URL"] . "%";
        $regime = "%" . $filter["regime"] . "%";
        $pays_du_participant_etranger = "%" . $filter["pays_du_participant_etranger"] . "%";
        $entree_en_production = "%" . $filter["entree_en_production"] . "%";
        $capital_en_DT = "%" . $filter["capital_en_DT"] . "%";
        $emploi = "%" . $filter["emploi"] . "%";
        $secteur = "%" . $filter["secteur"] . "%";


        $sql = "SELECT * FROM profil WHERE denomination LIKE :denomination 
            AND raison_sociale LIKE :raison_sociale
            AND responsable LIKE :responsable
            AND activites LIKE :activites
            AND produits LIKE :produits
            AND adresse_usine LIKE :adresse_usine
            AND gouvernorat LIKE :gouvernorat
            AND delegation LIKE :delegation
            AND telephone_siege_usine LIKE :telephone_siege_usine
            AND fax_siege_usine LIKE :fax_siege_usine
            AND email LIKE :email
            AND URL LIKE :URL
            AND regime LIKE :regime
            AND pays_du_participant_etranger LIKE :pays_du_participant_etranger
            AND entree_en_production LIKE :entree_en_production
            AND capital_en_DT LIKE :capital_en_DT
            AND emploi LIKE :emploi
            AND secteur LIKE :secteur";
        $q = $this->db->prepare($sql);
       // $q->bindParam(":id", $id);
        $q->bindParam(":denomination", $denomination);
        $q->bindParam(":raison_sociale", $raison_sociale);
        $q->bindParam(":responsable", $responsable);
        $q->bindParam(":activites", $activites);
        $q->bindParam(":produits", $produits);
        $q->bindParam(":adresse_usine", $adresse_usine);
        $q->bindParam(":gouvernorat", $gouvernorat);
        $q->bindParam(":delegation", $delegation);
        $q->bindParam(":telephone_siege_usine", $telephone_siege_usine);
        $q->bindParam(":fax_siege_usine", $fax_siege_usine);
        $q->bindParam(":email", $email);
        $q->bindParam(":URL", $URL);
        $q->bindParam(":regime", $regime);
        $q->bindParam(":pays_du_participant_etranger", $pays_du_participant_etranger);
        $q->bindParam(":entree_en_production", $entree_en_production);
        $q->bindParam(":capital_en_DT", $capital_en_DT);
        $q->bindParam(":emploi", $emploi);
        $q->bindParam(":secteur", $secteur);

        $q->execute();
        print_r($denomination);
        $rows = $q->fetchAll();
        $result = array();
        foreach($rows as $row) {
            array_push($result, $this->read($row));
        }
        return $result;
    }

   


}

?>