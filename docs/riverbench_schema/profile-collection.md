# SHACL Shapes Documentation

## Shape: ProfileGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Profile`

### Properties

#### Property: (Blank Node)

**Path:**

- Inverse of:
  - Predicate path:
    - `rdf:type`

^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer

---

## Shape: ProfileShape

### NodeShape Constraints

- **sh:targetClass:** `rb:Profile`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:isSupersetOfProfile`

`rb:isSupersetOfProfile`

**Constraints:**
- **sh:nodeKind:** `sh:IRI`
- **sh:node:** (Blank Node)

---


## Original SHACL File

```turtle
@prefix : <https://w3id.org/riverbench/schema/dataset-shacl#> .
@prefix sh: <http://www.w3.org/ns/shacl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix rb: <https://w3id.org/riverbench/schema/metadata#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix stax: <https://w3id.org/stax/ontology#> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix void: <http://rdfs.org/ns/void#> .

# Shape file to validate entire profile collections.

# At least one profile per collection
:ProfileGraphShape
  a sh:NodeShape ;
  sh:targetNode rb:Profile ;
  sh:property [
    sh:path [ sh:inversePath rdf:type ] ;
    sh:minCount 1 ;
  ]
.

# Profile shape
:ProfileShape
    a sh:NodeShape ;
    sh:targetClass rb:Profile ;
    # Check if the children profiles exist
    sh:property [
        sh:path rb:isSupersetOfProfile ;
        sh:nodeKind sh:IRI ;
        sh:node [
            sh:property [
                sh:path rdf:type ;
                sh:hasValue rb:Profile ;
            ]
        ]
    ]
.

```
