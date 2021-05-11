#<span style="color:red">Still under development -- not yet ready for prime time</span>



# Template for LinkML based schema's

## What is this?

This is a GitHub template for a [LinkML](https://github.com/linkml/) based projects.

It allows you to create a project for your schema as quickly as
possible. It takes care of generating a beautiful readthedocs themed
site, as well as downstream artefacts, including:

 * JSON-Schema
 * ShEx
 * OWL
 * RDF (direct mapping)
 * JSON-LD Contexts
 * SQL DDL (TODO)
 * TSV/CSV reports (TODO)

## Quickstart

 1. Click the big green "Use this template" button on this page
 2. Name your repo according to your schema, e.g. my-awsome-project-model, and clone it
 3. Rename the schema file in [model/schema](model/schema). Keep the `.yaml` suffix
 4. Modify the schema, add your own classes and slots.
 5. Edit `model/CONFIG.yaml` to set your specific parameters. The details on the parameters can be found in
    the [LinkML Template Configuration Model](https://linkml.github.io/template-config-model/) directory.  
    (_Note that the Template Configuration Model was built using this very template._)
 6. Run the [template-configurator](https://linkml.github.io/template-configurator/) program:
    1) `pip(env) install template-configurator`
    2) `pip(env run) configure`
    
    This will generate a number of files that can be used to make, test, and distribute your final model.  Note
    that the template-configurator only needs to be run once as a rule.  You can, however, re-generate all of
    the target artifacts with `pip(env run) configure --reset`
 7. Type `make` to build your downstream artefacts (jsonschema, owl, etc)
 8. Once satisfied, commit your new project to github, which will rerun the make process.
 9. To install the package in pypi...


## How it works

This repo is a GitHub "template" repo. When you "Use this template" it will make a copy for your project.

Everything is orchestrated by a generic single [Makefile](Makefile). For this to work you should follow certain conventions:

 * Keep your schema in src/schema
 * Use the `.yaml` suffix for all schema files
 * Use the suggested directory layout here.

To run the Makefile you will need Python (>=3.7):
