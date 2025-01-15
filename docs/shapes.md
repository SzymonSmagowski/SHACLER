# SHACL Shapes Documentation

## Shape: ProfileGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Profile`

### Properties

#### Property: (Blank Node)

**Path:** ^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

---

## Shape: ProfileShape

### NodeShape Constraints

- **sh:targetClass:** `rb:Profile`

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `dcat:DatasetSeries`

#### Property: (Blank Node)

**Path:** `dcterms:identifier`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:** `dcterms:title`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:description`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `rb:hasDatasetShape`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:node:** (Blank Node)

#### Property: (Blank Node)

**Path:** `rb:hasDistributionShape`

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

**Path:** ^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

---

## Shape: TaskShape

### NodeShape Constraints

- **sh:targetNode:** `ns1:task`

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:Task`

#### Property: (Blank Node)

**Path:** `dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `ns2:metadata`

#### Property: (Blank Node)

**Path:** `dcterms:identifier`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:** `dcterms:title`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:description`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:creator`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:BlankNodeOrIRI`

---

## Shape: CategoryGraphShape

### NodeShape Constraints

- **sh:targetNode:** `rb:Category`

### Properties

#### Property: (Blank Node)

**Path:** ^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

---

## Shape: CategoryShape

### NodeShape Constraints

- **sh:targetNode:** `ns1:category`

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:Category`

#### Property: (Blank Node)

**Path:** `dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:hasValue:** `ns2:metadata`

#### Property: (Blank Node)

**Path:** `dcterms:identifier`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:** `dcterms:title`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:description`

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

**Path:** ^`rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer

---

## Shape: DatasetShape

### NodeShape Constraints

- **sh:targetClass:** `rb:Dataset`

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `dcat:Dataset`

#### Property: (Blank Node)

**Path:** `dcterms:conformsTo`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:hasValue:** `ns1:metadata`

#### Property: (Blank Node)

**Path:** `dcterms:identifier`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:string`

#### Property: (Blank Node)

**Path:** `dcterms:title`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:description`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:datatype:** `rdf:langString`
- **sh:uniqueLang:** "True"^^xsd:boolean

#### Property: (Blank Node)

**Path:** `dcterms:issued`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:date`

#### Property: (Blank Node)

**Path:** `dcterms:license`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:pattern:** "^https://spdx.org/licenses/"

#### Property: (Blank Node)

**Path:** `dcterms:creator`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:BlankNodeOrIRI`

#### Property: (Blank Node)

**Path:** `dcat:theme`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`
- **sh:pattern:** "^http://eurovoc.europa.eu/"
- **sh:node:** (Blank Node)

#### Property: (Blank Node)

**Path:** `void:vocabulary`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

#### Property: (Blank Node)

**Path:** `rb:hasStreamElementCount`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:integer`

#### Property: (Blank Node)

**Path:** `stax:hasStreamTypeUsage`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "2"^^xsd:integer
- **sh:node:** `StreamTypeShape`

#### Property: (Blank Node)

**Path:** `rb:hasStreamElementSplit`

**Constraints:**
- **sh:nodeKind:** `sh:BlankNodeOrIRI`
- **sh:node:** `StreamElementSplitShape`

#### Property: (Blank Node)

**Path:** `rb:conformsToRdf11`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:** `rb:conformsToRdfStarDraft_20211217`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:** `rb:usesGeneralizedRdfDatasets`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:** `rb:usesGeneralizedTriples`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:** `rb:usesRdfStar`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:datatype:** `xsd:boolean`

#### Property: (Blank Node)

**Path:** `dcat:version`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:** `dcterms:modified`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:** `dcat:landingPage`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:** `dcat:inSeries`

**Constraints:**
- **sh:maxCount:** "0"^^xsd:integer

#### Property: (Blank Node)

**Path:** `dcat:distribution`

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

**Path:** `rdf:type`

**Constraints:**
- **sh:hasValue:** `stax:ConcreteRdfStreamType`

---

## Shape: FlatStreamTypeShape

### NodeShape Constraints

- **sh:targetNode:** `stax:flatStream`

### Properties

#### Property: (Blank Node)

**Path:** ((`skos:narrower`)+)/(^`stax:hasStreamType`)/(^`stax:hasStreamTypeUsage`)

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:maxCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

---

## Shape: StreamElementSplitShape

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:in:** (Blank Node)

---

## Shape: SubjectShapeShape

### NodeShape Constraints

- **sh:targetSubjectsOf:** `rb:hasSubjectShape`

### Properties

#### Property: (Blank Node)

**Path:** `rdf:type`

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:hasValue:** `rb:TopicStreamElementSplit`

#### Property: (Blank Node)

**Path:** `rb:hasSubjectShape`/(`sh:targetClass`|`sh:targetSubjectsOf`|`sh:targetObjectsOf`|`rb:targetCustom`)

**Constraints:**
- **sh:minCount:** "1"^^xsd:integer
- **sh:nodeKind:** `sh:IRI`

---

