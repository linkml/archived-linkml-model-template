import argparse
import keyword
import os
import sys
from argparse import ArgumentParser
from dataclasses import dataclass
from io import StringIO
from typing import Dict, Optional, List
from warnings import warn

import yaml
from hbreader import hbread
from jsonasobj import as_dict
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.yamlutils import DupCheckYamlLoader

from config.config_model import Config, Component

CWD = os.path.dirname(__file__)
SETUP_BASE = os.path.abspath(os.path.join('..', CWD))
MODEL_ROOT = os.path.abspath(os.path.join(SETUP_BASE, '..'))
DEFAULT_CONF_FILE = os.path.join(SETUP_BASE, 'CONFIG.yaml')

TEMPLATES_DIR = os.path.join(SETUP_BASE, 'templates')
ACTIONS_TEMPLATE_DIR = os.path.join(TEMPLATES_DIR, '.github', 'workflows')
MAKEFILE_TEMPLATE = os.path.join(TEMPLATES_DIR, 'Makefile')

MKDOCS_YAML = os.path.join(MODEL_ROOT, 'mkdocs.yaml')
SETUP_CFG = os.path.join(MODEL_ROOT, 'setup.cfg')
GITHUB_WORKFLOWS_DIR = os.path.join(MODEL_ROOT, '.github', 'workflows')
MAKEFILE = os.path.join(MODEL_ROOT, 'Makefile')

# ================
#  DEFAULTS
# ================
default_keywords = [
    'linkml',
    'LOD',
    'Modeling',
    'Linked',
    'open',
    'data',
    'model']

default_classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Healthcare Industry',
    'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
]


def strip_config_comments(txt: str) -> str:
    return '\n'.join([line for line in txt.split('\n') if not line.startswith(';')])


def build_github_actions(config: Config, hard_reset: bool):
    for action_file in os.listdir(ACTIONS_TEMPLATE_DIR):
        target_action_filename = os.path.join(GITHUB_WORKFLOWS_DIR, action_file)
        if hard_reset or not os.path.exists(target_action_filename):
            action_yaml = hbread(os.path.join(ACTIONS_TEMPLATE_DIR, action_file)).format(**as_dict(config))
            os.makedirs(GITHUB_WORKFLOWS_DIR, exist_ok=True)
            with open(target_action_filename, 'w') as f:
                f.write(action_yaml)
            print(f"{target_action_filename} written")


def build_makefile(config: Config, hard_reset: bool):
    if hard_reset or not os.path.exists(MAKEFILE):
        makefile = hbread(MAKEFILE_TEMPLATE).\
            format(generate_targets=' '.join([entry.code.text for entry in config.generate]), **as_dict(config))
        with open(MAKEFILE, 'w') as f:
            f.write(makefile)
        print(f"{MAKEFILE} written")


def build_setup_cfg(config: Config, hard_reset: bool):
    conf_dict = as_dict(config)

    def build_data_files() -> str:
        template = "{model_py_name}/{{component}} = {model_py_name}/{{component}}/*".format(**conf_dict)
        filelist = [template.format(component="model")]
        for entry in config.generate:
            filelist.append(template.format(component=entry.code.text))
        return '\n    '.join(filelist)

    def build_keywords() -> str:
        return '\n    ' + '\n    '.join(config.keywords)

    def build_classifiers() -> str:
        return '\n    ' + '\n    '.join(config.classifiers)

    if hard_reset or not os.path.exists(SETUP_CFG):
        setup_cfg = hbread(os.path.join(TEMPLATES_DIR, 'setup.cfg'))

        setup_cfg = strip_config_comments(
            setup_cfg.format(data_files = build_data_files(),
                             classifiers_ = build_classifiers(),
                             keywords_ = build_keywords(),
                             **(as_dict(config))))
        with open(SETUP_CFG, 'w') as f:
            f.write(setup_cfg)
        print(f"{SETUP_CFG} written")

def build_httpd_rules(config: Config, hard_reset: bool):
    pass

def build_mkdocs_yaml(config: Config, hard_reset: bool):
    if hard_reset or not os.path.exists(MKDOCS_YAML):
        mkdocs_yaml = hbread(os.path.join(TEMPLATES_DIR, 'mkdocs.yaml'))
        mkdocs_yaml = mkdocs_yaml.format(**(as_dict(config)))
        with open(MKDOCS_YAML, 'w') as f:
            f.write(mkdocs_yaml)
        print(f"{MKDOCS_YAML} written")


def massage_config_file(config: Config, hard_reset: bool) -> None:
    if not config.model_py_name:
        config.model_py_name = config.model_name.replace('-', '_')
    if not config.model_py_name.isidentifier():
        warn(f"model_py_name ({config.model_py_name}) is not a valid identifier")
    if keyword.iskeyword(config.model_py_name):
        warn(f"model_py_name ({config.model_py_name}) is a python keyword")
    if not config.model_url:
        config.model_url = f"https://github.com/{config.model_organization}/{config.model_name}"
    if not config.classifiers:
        config.classifiers = default_classifiers
    if not config.keywords:
        config.keywords = default_keywords


def proc_conf_file(conf_file_location, hard_reset: bool) -> int:
    config = yaml_loader.load(conf_file_location, Config)
    massage_config_file(config, hard_reset)
    build_github_actions(config, hard_reset)
    build_makefile(config, hard_reset)
    build_setup_cfg(config, hard_reset)
    build_httpd_rules(config, hard_reset)
    build_mkdocs_yaml(config, hard_reset)
    return 0


def genargs() -> ArgumentParser:
    """
    Generate an input string parser
    :return: parser
    """
    parser = ArgumentParser(description="Configure a LinkML model repository")
    parser.add_argument("-c", "--conffile", help="Configuration file location", default=DEFAULT_CONF_FILE,
                        type=argparse.FileType('r'))
    parser.add_argument("--reset", help="Hard reset -- regenerate all files from scratch", action="store_true")
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    opts = genargs().parse_args(argv)
    return proc_conf_file(opts.conffile, opts.reset)


if __name__ == '__main__':
    sys.exit(main())
