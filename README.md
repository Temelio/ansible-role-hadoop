# hadoop

[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-hadoop/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-hadoop)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-hadoop/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-hadoop)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-hadoop/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-hadoop/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-hadoop/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-hadoop/)
[![Ansible Role](https://img.shields.io/ansible/role/22474.svg)](https://galaxy.ansible.com/Temelio/hadoop/)

Install hadoop package.

## Requirements

This role requires Ansible 2.2 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Ubuntu Xenial

and use:
- Ansible 2.2.x
- Ansible 2.3.x
- Ansible 2.4.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

``` yaml
# Installation management
# -----------------------------------------------------------------------------
hadoop_system_dependencies: "{{ _hadoop_system_dependencies }}"
hadoop_mirrors:
  - 'http://ftp.osuosl.org/pub/apache/hadoop/core/stable2'
  - 'http://apache.rediris.es/hadoop/core/stable2'
  - 'http://ftp.cixug.es/apache/hadoop/core/stable2'
  - 'http://www-eu.apache.org/dist/hadoop/common/stable2'
hadoop_download_delay: 2
hadoop_download_retries: 5
hadoop_version: '2.9.0'
hadoop_package_name: "hadoop-{{ hadoop_version }}.tar.gz"
hadoop_paths_dirs:
  bin:
    path: '/opt/hadoop/bin'
  config:
    path: '/opt/hadoop/etc/hadoop'
  entry_point:
    path: '/opt/hadoop'
  release:
    path: "/opt/hadoop2x/hadoop-{{ hadoop_version }}"
  root:
    path: '/opt/hadoop2x'
  sbin:
    path: '/opt/hadoop/sbin'
  tmp:
    path: '/tmp'
hadoop_paths_files:
  core_site:
    path: "{{ hadoop_paths_dirs.config.path }}/core-site.xml"
  hadoop_env:
    path: "{{ hadoop_paths_dirs.config.path }}/hadoop-env.sh"
  hdfs_site:
    path: "{{ hadoop_paths_dirs.config.path }}/hdfs-site.xml"
  slaves:
    path: "{{ hadoop_paths_dirs.config.path }}/slaves"
  yarn_site:
    path: "{{ hadoop_paths_dirs.config.path }}/yarn-site.xml"


# Configuration management
# -----------------------------------------------------------------------------

# The type of the node: slave / master / resourcemanager / nodemanager / datanode / namenode
hadoop_type_of_node: 'slave'

# A dictionary with a set of properties to set in the hdfs-site.xml
hadoop_hdfs_props: {}

# A dictionary with a set of properties to set in the yarn-site.xml
hadoop_yarn_props: {}

# Hadoop java configuration
hadoop_jvm_home: "{{ _hadoop_jvm_home }}"
hadoop_jvm_options:
  - dest: "{{ hadoop_paths_files.hadoop_env.path }}"
    regexp: 'JAVA_HOME='
    line: "export JAVA_HOME={{ hadoop_jvm_home }}"

hadoop_master: ''
hadoop_slaves: []
```

### Debian OS family specific vars

``` yaml
_hadoop_system_dependencies:
  - name: 'gzip'
  - name: 'tar'
  - name: 'wget'

_hadoop_jvm_home: '/usr/lib/jvm/java-8-openjdk-amd64'
```

## Dependencies

No dependency is mandatory, because you can manage system dependencies.

**JRE dependency is not managed, you can use an external role to do it (see tests).**


## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: Temelio.hadoop }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://temelio.com
- alexandre.chaussier [at] temelio.com
