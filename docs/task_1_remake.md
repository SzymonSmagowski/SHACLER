# SHACL Shapes Documentation

## Shape: http://szymi_himym.org/ontology/entity/PersonShape

**Label:** Person Validation Shape

**Type:** NodeShape

**Description:** Validates person data in HIMYM dataset

**Target Class:** http://schema.org/Person


**Properties:**

- **sh:property:** - nb1094a4085514eb6a2bb0e76d900e244b1
- nb1094a4085514eb6a2bb0e76d900e244b2
- nb1094a4085514eb6a2bb0e76d900e244b3
- nb1094a4085514eb6a2bb0e76d900e244b4
- nb1094a4085514eb6a2bb0e76d900e244b5
- nb1094a4085514eb6a2bb0e76d900e244b6

**Nested Property Shapes:**

- Path: http://schema.org/givenName

  **Properties:**

  - **sh:path:** http://schema.org/givenName
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#string
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:pattern:** ^[A-Z][a-z]+$
- Path: http://schema.org/familyName

  **Properties:**

  - **sh:path:** http://schema.org/familyName
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#string
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:pattern:** ^[A-Z][a-z]+$
- Path: http://schema.org/birthDate

  **Properties:**

  - **sh:path:** http://schema.org/birthDate
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#date
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:minInclusive:** 1970-01-01
  - **sh:maxInclusive:** 1990-12-31
- Path: http://schema.org/homeLocation

  **Properties:**

  - **sh:path:** http://schema.org/homeLocation
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:class:** http://schema.org/Place
- Path: http://xmlns.com/foaf/0.1/nick

  **Properties:**

  - **sh:path:** http://xmlns.com/foaf/0.1/nick
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#string
  - **sh:maxCount:** 1
- Path: http://szymi_himym.org/ontology/property/frequentHangout

  **Properties:**

  - **sh:path:** http://szymi_himym.org/ontology/property/frequentHangout
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:class:** http://szymi_himym.org/ontology/entity/HangoutPlace
---

## Shape: http://szymi_himym.org/ontology/entity/PlaceShape

**Label:** Place Validation Shape

**Type:** NodeShape

**Description:** Validates place data in HIMYM dataset

**Target Class:** http://schema.org/Place


**Properties:**

- **sh:property:** - nb1094a4085514eb6a2bb0e76d900e244b7
- nb1094a4085514eb6a2bb0e76d900e244b8

**Nested Property Shapes:**

- Path: http://schema.org/name

  **Properties:**

  - **sh:path:** http://schema.org/name
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#string
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
  - **sh:minLength:** 2
  - **sh:maxLength:** 50
- Path: http://schema.org/containedInPlace

  **Properties:**

  - **sh:path:** http://schema.org/containedInPlace
  - **sh:minCount:** 0
  - **sh:maxCount:** 1
  - **sh:class:** http://schema.org/Place
---

## Shape: http://szymi_himym.org/ontology/entity/HangoutPlaceShape

**Label:** Hangout Place Validation Shape

**Type:** NodeShape

**Description:** Validates hangout places in HIMYM dataset

**Target Class:** http://szymi_himym.org/ontology/entity/HangoutPlace


**Properties:**

- **sh:property:** - nb1094a4085514eb6a2bb0e76d900e244b9
- nb1094a4085514eb6a2bb0e76d900e244b10

**Nested Property Shapes:**

- Path: http://www.w3.org/1999/02/22-rdf-syntax-ns#type

  **Properties:**

  - **sh:path:** http://www.w3.org/1999/02/22-rdf-syntax-ns#type
  - **sh:minCount:** 1
  - **sh:hasValue:** http://schema.org/Place
- Path: http://schema.org/name

  **Properties:**

  - **sh:path:** http://schema.org/name
  - **sh:datatype:** http://www.w3.org/2001/XMLSchema#string
  - **sh:minCount:** 1
  - **sh:maxCount:** 1
---

## Shape: http://szymi_himym.org/ontology/entity/FrequentHangoutPropertyShape

**Label:** Frequent Hangout Property Shape

**Type:** PropertyShape

**Description:** Validates the frequentHangout property

**Target Class:** http://schema.org/Person


**Properties:**

- **sh:path:** http://szymi_himym.org/ontology/property/frequentHangout
- **sh:minCount:** 1
- **sh:maxCount:** 1
- **sh:class:** http://szymi_himym.org/ontology/entity/HangoutPlace
- **sh:nodeKind:** http://www.w3.org/ns/shacl#IRI
---

