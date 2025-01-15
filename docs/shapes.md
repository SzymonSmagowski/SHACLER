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
- **sh:maxCount:** "1"^^xsd:integer

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
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `dcat:DatasetSeries`

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
  - `rb:hasDatasetShape`

`rb:hasDatasetShape`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:node:** (Blank Node)

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `rb:hasDistributionShape`

`rb:hasDistributionShape`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
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
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

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
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:Task`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:conformsTo`

`dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `ns2:metadata`

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
  - `dcterms:creator`

`dcterms:creator`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
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
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

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
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:Category`

#### Property: (Blank Node)

**Path:**

- Predicate path:
  - `dcterms:conformsTo`

`dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `ns2:metadata`

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

---

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

