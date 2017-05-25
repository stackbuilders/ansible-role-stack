# Haskell Stack

[![Build Status](https://travis-ci.org/sestrella/haskell-stack.svg?branch=master)](https://travis-ci.org/sestrella/haskell-stack)

Ansible role to install and configure Haskell Stack.

## Role Variables

| Name                            | Default          | Description
| ---                             | ---              | ---
| `haskell_stack_bin_dir`         | `/usr/local/bin` | Path where the stack binary is going to be copied.
| `haskell_stack_compilers`       | `[]`             | List of GHC compilers to install.
| `haskell_stack_global_resolver` | `lts-8.15`       | Global stack resolver to be set at `~/.stack/global-project/stack.yaml` file.

## Example Playbook

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

```YAML
- hosts: servers
  roles:
    - { role: username.rolename, x: 42 }
```

## License

MIT
