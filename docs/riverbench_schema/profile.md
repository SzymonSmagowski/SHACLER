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
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`

---

## Shape: ProfileShape

### NodeShape Constraints

- **sh:targetClass:** `rb:Profile`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:hasValue:** `dcat:DatasetSeries`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:identifier`

`dcterms:identifier`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:title`

`dcterms:title`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** `"True"^^xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:description`

`dcterms:description`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** `"True"^^xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:hasDatasetShape`

`rb:hasDatasetShape`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:node:** (Blank Node)

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:hasDistributionShape`

`rb:hasDistributionShape`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:nodeKind:** `sh:BlankNodeOrIRI`

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

# Shape file to validate single profile files.
# See also profile-collection.ttl for shapes to validate profile collections,
# i.e., all profiles in a benchmark category.

# Exactly one profile per file
:ProfileGraphShape
  a sh:NodeShape ;
  sh:targetNode rb:Profile ;
  sh:property [
    sh:path [ sh:inversePath rdf:type ] ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
  ]
.

# We can't easily validate this in SHACL... but the ID should match the filename
# and URI.
:ProfileShape
    a sh:NodeShape ;
    sh:targetClass rb:Profile ;
    sh:property [
        sh:path rdf:type ;
        sh:minCount 1 ;
        sh:hasValue dcat:DatasetSeries ;
    ] , [
        sh:path dcterms:identifier ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:datatype xsd:string ;
    ] , [
        sh:path dcterms:title ;
        sh:minCount 1 ;
        sh:datatype rdf:langString ;
        sh:uniqueLang true ;
    ] , [
        sh:path dcterms:description ;
        sh:minCount 1 ;
        sh:datatype rdf:langString ;
        sh:uniqueLang true ;
    ] , [
        sh:path rb:hasDatasetShape ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:node [
            sh:property [
                sh:path sh:targetClass ;
                sh:minCount 1 ;
                sh:maxCount 1 ;
                sh:hasValue rb:Dataset ;
            ] , [
                sh:path sh:property ;
                sh:minCount 1 ;
                sh:nodeKind sh:BlankNodeOrIRI ;
            ]
        ]
    ] , [
        sh:path rb:hasDistributionShape ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:nodeKind sh:BlankNodeOrIRI ;
    ]
.

```
