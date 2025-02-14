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

## Shape: TaskGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Task`

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

## Shape: TaskShape

### NodeShape Constraints

- **sh:targetNode:** `ns1:task`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:hasValue:** `rb:Task`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:conformsTo`

`dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:hasValue:** `ns2:metadata`

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
  - `dcterms:creator`

`dcterms:creator`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:nodeKind:** `sh:BlankNodeOrIRI`

---

## Shape: CategoryGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Category`

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

## Shape: CategoryShape

### NodeShape Constraints

- **sh:targetNode:** `ns1:category`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:hasValue:** `rb:Category`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:conformsTo`

`dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** `"1"^^xsd:integer`
- **sh:maxCount:** `"1"^^xsd:integer`
- **sh:hasValue:** `ns2:metadata`

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

# Exactly one category per file
:CategoryGraphShape
  a sh:NodeShape ;
  sh:targetNode rb:Category ;
  sh:property [
    sh:path [ sh:inversePath rdf:type ] ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
  ]
.

:CategoryShape
    a sh:NodeShape ;
    sh:targetNode <https://w3id.org/riverbench/temp#category> ;
    sh:property [
        sh:path rdf:type ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:hasValue rb:Category ;
    ] , [
        sh:path dcterms:conformsTo ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:hasValue <https://w3id.org/riverbench/schema/metadata> ;
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
    ]
.

```
