from pathlib import Path

import pytest
from rdflib import BNode, Graph, Literal, Namespace

from shacl_doc_generator.models import Constraint
from shacl_doc_generator.parser import ShaclParser

EX = Namespace("http://example.org/")


@pytest.fixture
def parser():
    return ShaclParser()


fixtures_dir = Path(__file__).parent / "fixtures"


def test_simple_node_shape(parser):
    test_file = fixtures_dir / "simple_shape.ttl"
    shapes = parser.parse_file(test_file)

    assert "ex:UserShape" in shapes
    shape = shapes["ex:UserShape"]

    assert Constraint(name="sh:name", value='`"User"`') in shape.constraints
    assert Constraint(name="sh:targetClass", value="`ex:User`") in shape.constraints

    assert len(shape.properties) == 1
    prop = shape.properties[0]
    assert prop.path.items == ["`ex:email`"]
    assert (
        Constraint(name="sh:minCount", value='`"1"^^xsd:integer`') in prop.constraints
    )


def test_to_prefixed(parser):
    g = Graph()
    g.bind("ex", EX)

    assert parser.to_prefixed(g, EX.User) == "`ex:User`"

    lit = Literal("bonjour", lang="fr")
    assert parser.to_prefixed(g, lit) == '`"bonjour"@fr`'

    bnode = BNode()
    assert parser.to_prefixed(g, bnode) == "(Blank Node)"
