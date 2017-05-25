# Haskell Stack

[![Build Status](https://travis-ci.org/sestrella/haskell-stack.svg?branch=master)](https://travis-ci.org/sestrella/haskell-stack)

A brief description of the role goes here.

## Requirements

Any pre-requisites that may not be covered by Ansible itself or the role should
be mentioned here. For instance, if the role uses the EC2 module, it may be a
good idea to mention in this section that the boto package is required.

## Role Variables

| Name                            | Default          | Description
| ---                             | ---              | ---
| `haskell_stack_bin_dir`         | `/usr/local/bin` | Path where the stack binary is going to be copied.
| `haskell_stack_global_resolver` | `lts-8.15`       | Global stack resolver to be set at `~/.stack/global-project/stack.yaml` file.

## Dependencies

A list of other roles hosted on Galaxy should go here, plus any details in
regards to parameters that may need to be set for other roles, or variables
that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```YAML
- hosts: servers
  roles:
    - { role: username.rolename, x: 42 }
```

## License

MIT

## Author Information

An optional section for the role authors to include contact information, or a
website (HTML is not allowed).
