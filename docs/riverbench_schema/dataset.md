# SHACL Shapes Documentation

## Shape: DatasetGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Dataset`

### Properties

#### Property: (Blank Node)

**Path:**

- Inverse of:
  - Predicate path:
    - `rdf:type`

^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

---

## Shape: DatasetShape

### NodeShape Constraints

- **sh:targetClass:** `rb:Dataset`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `dcat:Dataset`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:conformsTo`

`dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:hasValue:** `ns1:metadata`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:identifier`

`dcterms:identifier`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:title`

`dcterms:title`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:description`

`dcterms:description`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:issued`

`dcterms:issued`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:date`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:license`

`dcterms:license`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:pattern:** "^https://spdx.org/licenses/"

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:creator`

`dcterms:creator`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:BlankNodeOrIRI`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcat:theme`

`dcat:theme`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:pattern:** "^http://eurovoc.europa.eu/"
- **sh:node:** (Blank Node)

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `void:vocabulary`

`void:vocabulary`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:hasStreamElementCount`

`rb:hasStreamElementCount`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:integer`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `stax:hasStreamTypeUsage`

`stax:hasStreamTypeUsage`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "2"^^xsd:integer
- **sh:node:** `StreamTypeShape`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:hasStreamElementSplit`

`rb:hasStreamElementSplit`

**Constraints:**
- **sh:nodeKind:** `sh:BlankNodeOrIRI`
- **sh:node:** `StreamElementSplitShape`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:conformsToRdf11`

`rb:conformsToRdf11`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:conformsToRdfStarDraft_20211217`

`rb:conformsToRdfStarDraft_20211217`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:usesGeneralizedRdfDatasets`

`rb:usesGeneralizedRdfDatasets`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:usesGeneralizedTriples`

`rb:usesGeneralizedTriples`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:usesRdfStar`

`rb:usesRdfStar`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcat:version`

`dcat:version`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:modified`

`dcterms:modified`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcat:landingPage`

`dcat:landingPage`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcat:inSeries`

`dcat:inSeries`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcat:distribution`

`dcat:distribution`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

---

## Shape: StreamTypeShape

### NodeShape Constraints

- **sh:and:** (Blank Node)

---

## Shape: (Blank Node)

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:hasValue:** `stax:ConcreteRdfStreamType`

---

## Shape: FlatStreamTypeShape

### NodeShape Constraints

- **sh:targetNode:** `stax:flatStream`

### Properties

#### Property: (Blank Node)

**Path:**

- Sequence of:
  - One-or-more of:
    - Predicate path:
      - `skos:narrower`
  - Inverse of:
    - Predicate path:
      - `stax:hasStreamType`
  - Inverse of:
    - Predicate path:
      - `stax:hasStreamTypeUsage`

((`skos:narrower`)+)/(^`stax:hasStreamType`)/(^`stax:hasStreamTypeUsage`)

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

---

## Shape: StreamElementSplitShape

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:in:** (Blank Node)

---

## Shape: SubjectShapeShape

### NodeShape Constraints

- **sh:targetSubjectsOf:** `rb:hasSubjectShape`

### Properties

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rdf:type`

`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:TopicStreamElementSplit`

#### Property: (Blank Node)

**Path:**

- Sequence of:
  - rb:hasSubjectShape
  - Alternative of:
    - sh:targetClass
    - sh:targetSubjectsOf
    - sh:targetObjectsOf
    - rb:targetCustom

`rb:hasSubjectShape`/(`sh:targetClass`|`sh:targetSubjectsOf`|`sh:targetObjectsOf`|`rb:targetCustom`)

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

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

# Exactly one dataset per file
:DatasetGraphShape
  a sh:NodeShape ;
  sh:targetNode rb:Dataset ;
  sh:property [
    sh:path [ sh:inversePath rdf:type ] ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
  ]
.

:DatasetShape
  a sh:NodeShape ;
  sh:targetClass rb:Dataset ;
  sh:property
  [
    sh:path rdf:type ;
    sh:minCount 1 ;
    sh:hasValue dcat:Dataset ;
  ] ,
  # General metadata
  [
    sh:path dcterms:conformsTo ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:nodeKind sh:IRI ;
    sh:hasValue <https://w3id.org/riverbench/schema/metadata> ;
  ] ,
  [
    sh:path dcterms:identifier ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:string ;
  ] ,
  [
    sh:path dcterms:title ;
    sh:minCount 1 ;
    sh:datatype rdf:langString ;
    sh:uniqueLang true ;
  ] ,
  [
    sh:path dcterms:description ;
    sh:minCount 1 ;
    sh:datatype rdf:langString ;
    sh:uniqueLang true ;
  ] ,
  [
    sh:path dcterms:issued ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:date ;
  ] ,
  # Attribution
  [
    sh:path dcterms:license ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:nodeKind sh:IRI ;
    sh:pattern "^https://spdx.org/licenses/" ;
  ] ,
  [
    sh:path dcterms:creator ;
    sh:minCount 1 ;
    sh:nodeKind sh:BlankNodeOrIRI ;
  ] ,
  # Topics
  [
    sh:path dcat:theme ;
    sh:minCount 1 ;
    sh:nodeKind sh:IRI ;
    sh:pattern "^http://eurovoc.europa.eu/" ;
    sh:node [
      sh:property [
        sh:path rdf:type ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:hasValue skos:Concept ;
      ] ;
    ] ;
  ] ,
  # Technical metadata
  [
    sh:path void:vocabulary ;
    sh:minCount 1 ;
    sh:nodeKind sh:IRI ;
  ] ,
  [
    sh:path rb:hasStreamElementCount ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:integer ;
  ] ,
  [
    sh:path stax:hasStreamTypeUsage ;
    sh:minCount 1 ;
    sh:maxCount 2 ;
    sh:node :StreamTypeShape ;
  ] ,
  [
    sh:path rb:hasStreamElementSplit ;
    sh:nodeKind sh:BlankNodeOrIRI ;
    sh:node :StreamElementSplitShape ;
  ] ,
  # Conformance properties
  [
    sh:path rb:conformsToRdf11 ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:boolean ;
  ] ,
  [
    sh:path rb:conformsToRdfStarDraft_20211217 ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:boolean ;
  ] ,
  [
    sh:path rb:usesGeneralizedRdfDatasets ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:boolean ;
  ] ,
  [
    sh:path rb:usesGeneralizedTriples ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:boolean ;
  ] ,
  [
    sh:path rb:usesRdfStar ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:datatype xsd:boolean ;
  ] ,
  # Disallow version, modified, landingPage, inSeries, distribution
  [
    sh:path dcat:version ;
    sh:maxCount 0 ;
  ] ,
  [
    sh:path dcterms:modified ;
    sh:maxCount 0 ;
  ] ,
  [
    sh:path dcat:landingPage ;
    sh:maxCount 0 ;
  ] ,
  [
    sh:path dcat:inSeries ;
    sh:maxCount 0 ;
  ] ,
  [
    sh:path dcat:distribution ;
    sh:maxCount 0 ;
  ]
.

# Validate stream type annotations (RDF-STaX)
:StreamTypeShape
  a sh:NodeShape ;
  sh:and (
    # General conditions
    [
      sh:property [
        sh:path rdf:type ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:nodeKind sh:IRI ;
        sh:hasValue stax:RdfStreamTypeUsage ;
      ] , [
        sh:path stax:hasStreamType ;
        sh:minCount 1 ;
        sh:maxCount 1 ;
        sh:nodeKind sh:IRI ;
        sh:node [
          a sh:NodeShape ;
          sh:property [
            sh:path rdf:type ;
            sh:hasValue stax:ConcreteRdfStreamType ;
          ]
        ] ;
      ]
    ]
    # Either flat or grouped – specific conditions
    [
      sh:xone (
        :FlatStreamTypeUsageShape
        :GroupedStreamTypeUsageShape
      )
    ]
  )
.

# Flat stream type usage
:FlatStreamTypeUsageShape
  sh:property [
    sh:path (
      stax:hasStreamType
      [ sh:oneOrMorePath skos:broader ]
    ) ;
    sh:minCount 1 ;
    sh:hasValue stax:flatStream ;
  ]
.

# Grouped stream type usage
# The grouped stream type must be consistent with the flat stream type
:GroupedStreamTypeUsageShape
  sh:property [
    sh:path (
      stax:hasStreamType
      [ sh:oneOrMorePath skos:broader ]
    ) ;
    sh:minCount 1 ;
    sh:hasValue stax:groupedStream ;
  ] , [
    sh:path (
      stax:hasStreamType
      stax:canBeFlattenedInto
      [ sh:inversePath stax:hasStreamType ]
      [ sh:inversePath stax:hasStreamTypeUsage ]
    ) ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:nodeKind sh:IRI ;
  ]
.

# We must have exactly one flat stream type annotation
:FlatStreamTypeShape
  a sh:NodeShape ;
  sh:targetNode stax:flatStream ;
  sh:property [
    sh:path (
      [ sh:oneOrMorePath skos:narrower ]
      [ sh:inversePath stax:hasStreamType ]
      [ sh:inversePath stax:hasStreamTypeUsage ]
    ) ;
    sh:minCount 1 ;
    sh:maxCount 1 ;
    sh:nodeKind sh:IRI ;
  ]
.

:StreamElementSplitShape
  a sh:NodeShape ;
  sh:property [
    sh:path rdf:type ;
    sh:in (
      rb:TimeStreamElementSplit
      rb:StatementCountStreamElementSplit
      rb:TopicStreamElementSplit
    ) ;
  ]
.

:SubjectShapeShape
  a sh:NodeShape ;
  sh:targetSubjectsOf rb:hasSubjectShape ;
  sh:property [
    sh:path rdf:type ;
    sh:minCount 1 ;
    sh:hasValue rb:TopicStreamElementSplit ;
  ] , [
    sh:path (
      rb:hasSubjectShape
      [ sh:alternativePath (
        sh:targetClass
        sh:targetSubjectsOf
        sh:targetObjectsOf
        rb:targetCustom
      ) ]
    ) ;
    sh:minCount 1 ;
    sh:nodeKind sh:IRI ;
  ]
.

```
