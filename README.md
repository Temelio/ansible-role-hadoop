# hadoop

[![Build Status](https://travis-ci.org/infOpen/ansible-role-hadoop.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-hadoop)

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
