# Auto generated from config_model.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-05-05 14:42
# Schema: config_model
#
# id: https://linkml.org/linkml_config_model
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj import JsonObj
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
CONF = CurieNamespace('conf', 'https://linkml.org/linkml_config/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = CONF


# Types
class String(str):
    """ A character string """
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "string"
    type_model_uri = CONF.String


class Boolean(Bool):
    """ A binary (true or false) value """
    type_class_uri = XSD.boolean
    type_class_curie = "xsd:boolean"
    type_name = "boolean"
    type_model_uri = CONF.Boolean


# Class references
class ConfigModelName(extended_str):
    pass


@dataclass
class Config(YAMLRoot):
    """
    Configuration parameters for linkml model template
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = CONF.Config
    class_class_curie: ClassVar[str] = "conf:Config"
    class_name: ClassVar[str] = "Config"
    class_model_uri: ClassVar[URIRef] = CONF.Config

    model_name: Union[str, ConfigModelName] = None
    root_schema: str = None
    model_organization: str = None
    model_author: str = None
    model_author_email: str = None
    model_synopsis: str = None
    generate: Union[Union[str, "Component"], List[Union[str, "Component"]]] = None
    model_py_name: Optional[str] = None
    model_description: Optional[str] = None
    model_url: Optional[str] = None
    classifiers: Optional[Union[str, List[str]]] = empty_list()
    keywords: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.model_name is None:
            raise ValueError("model_name must be supplied")
        if not isinstance(self.model_name, ConfigModelName):
            self.model_name = ConfigModelName(self.model_name)

        if self.root_schema is None:
            raise ValueError("root_schema must be supplied")
        if not isinstance(self.root_schema, str):
            self.root_schema = str(self.root_schema)

        if self.model_organization is None:
            raise ValueError("model_organization must be supplied")
        if not isinstance(self.model_organization, str):
            self.model_organization = str(self.model_organization)

        if self.model_author is None:
            raise ValueError("model_author must be supplied")
        if not isinstance(self.model_author, str):
            self.model_author = str(self.model_author)

        if self.model_author_email is None:
            raise ValueError("model_author_email must be supplied")
        if not isinstance(self.model_author_email, str):
            self.model_author_email = str(self.model_author_email)

        if self.model_synopsis is None:
            raise ValueError("model_synopsis must be supplied")
        if not isinstance(self.model_synopsis, str):
            self.model_synopsis = str(self.model_synopsis)

        if self.generate is None:
            raise ValueError("generate must be supplied")
        elif not isinstance(self.generate, list):
            self.generate = [self.generate]
        elif len(self.generate) == 0:
            raise ValueError(f"generate must be a non-empty list")
        self.generate = [v if isinstance(v, Component) else Component(v) for v in self.generate]

        if self.model_py_name is not None and not isinstance(self.model_py_name, str):
            self.model_py_name = str(self.model_py_name)

        if self.model_description is not None and not isinstance(self.model_description, str):
            self.model_description = str(self.model_description)

        if self.model_url is not None and not isinstance(self.model_url, str):
            self.model_url = str(self.model_url)

        if self.classifiers is None:
            self.classifiers = []
        if not isinstance(self.classifiers, list):
            self.classifiers = [self.classifiers]
        self.classifiers = [v if isinstance(v, str) else str(v) for v in self.classifiers]

        if self.keywords is None:
            self.keywords = []
        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords]
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        super().__post_init__(**kwargs)


# Enumerations
class Component(EnumDefinitionImpl):
    """
    LinkML Component to generate
    """
    graphql = PermissibleValue(text="graphql",
                                     description="Emit model schema in GraphQL")
    json = PermissibleValue(text="json",
                               description="Emit model schema in JSON")
    jsonld_context = PermissibleValue(text="jsonld_context",
                                                   description="Emit JSON-LD contexts for model instance to RDF transformations")
    json_schema = PermissibleValue(text="json_schema",
                                             description="Emit JSON Schema rendering of the model")
    owl = PermissibleValue(text="owl",
                             description="Emit OWL representation of model schema")
    rdf = PermissibleValue(text="rdf",
                             description="Emit RDF representation of model schema")
    shex = PermissibleValue(text="shex",
                               description="Emit ShEx representation of model schema")

    _defn = EnumDefinition(
        name="Component",
        description="LinkML Component to generate",
    )

# Slots

